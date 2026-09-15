#!/usr/bin/env python3
"""Audit Power Fx formula blocks for known-bad patterns this Bible has actually hit
live, plus structural sanity checks. Runs against markdown files (```-fenced blocks)
and guide HTML files (<pre id="...">...</pre> blocks, HTML-unescaped before checking).

Extends tools/audit-guide.py, which only checks HTML guide prose/YAML - this tool is
for the Power Fx formula content itself, wherever it lives (a project's local
src/formulas/*.md, or a guide page's copy-ready code cards).

Usage:
    python3 tools/audit-formulas.py path/to/file.md path/to/guide.html ...
    python3 tools/audit-formulas.py --diff path/to/local.md path/to/guide.html
        (checks that every fenced block in the .md appears, byte-for-byte after
        HTML-unescaping, somewhere in the guide's <pre> blocks - catches drift
        between a local formula file and what actually got published)
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

# Windows consoles default stdout to cp1252, which can't encode every character
# a finding message might contain (e.g. a bullet copied from formula text).
# Confirmed live, 2026-09-15: a UnicodeEncodeError here crashed the tool entirely
# instead of just printing the finding - fixed by forcing UTF-8 with lossy
# replacement rather than letting print() raise.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass  # older Python without TextIOWrapper.reconfigure - not expected here, but don't crash over it


def extract_md_blocks(text: str) -> list[tuple[int, str]]:
    """Returns (line_number, code) for every ```-fenced block."""
    out = []
    for m in re.finditer(r"```\n(.*?)\n```", text, flags=re.DOTALL):
        line = text.count("\n", 0, m.start()) + 1
        out.append((line, m.group(1)))
    return out


def extract_html_pre_blocks(text: str) -> list[tuple[int, str, str]]:
    """Returns (line_number, id, code) for every <pre id="...">...</pre> block,
    HTML-unescaped back to the real Power Fx source."""
    out = []
    for m in re.finditer(r'<pre id="([^"]*)">(.*?)</pre>', text, flags=re.DOTALL):
        line = text.count("\n", 0, m.start()) + 1
        code = html.unescape(m.group(2))
        out.append((line, m.group(1), code))
    return out


def check_addcolumns_groupby_quoted_names(code: str) -> list[str]:
    """AddColumns/GroupBy's column-name arguments must be bare identifiers, never
    quoted strings. Confirmed broken live twice in this Bible (Policy Tracker
    Overview build; Cadets Org Chart Phase 2, 2026-09-11 - 'Expected identifier
    name')."""
    findings = []
    for fn in ("AddColumns", "GroupBy"):
        for m in re.finditer(rf"{fn}\s*\(\s*[A-Za-z_][A-Za-z0-9_.']*\s*,\s*\"", code):
            findings.append(f"{fn}(...) column-name argument is a quoted string - must be a bare identifier (confirmed 'Expected identifier name' error)")
    return findings


def check_base64(code: str) -> list[str]:
    """Base64() confirmed not a real function in this tenant, 2026-09-11 ('unknown
    or unsupported function'). EncodeUrl() is the confirmed-working replacement for
    building a data URI from a generated string."""
    if re.search(r"\bBase64\s*\(", code):
        return ["Base64(...) used - confirmed this is not a real function here ('unknown or unsupported function'); use EncodeUrl() instead"]
    return []


def check_udf_table_param(code: str) -> list[str]:
    """A User Defined Function with a `: Table` parameter type. Confirmed broken
    live, 2026-09-11 ('Unknown type Table')."""
    findings = []
    for m in re.finditer(r"\w+\s*:\s*Table\b", code):
        findings.append("UDF parameter typed as `Table` - confirmed 'Unknown type Table' error; no working table-parameter syntax is confirmed in this Bible, inline the logic instead")
    return findings


def check_udf_definition_shape(code: str) -> list[str]:
    """A UDF definition (Name(params): Type = ...) mixed into what looks like an
    imperative block (contains Set(/ClearCollect( elsewhere in the same block) -
    likely destined for OnStart by mistake. UDF definitions belong in the App's
    separate `Formulas` property, never OnStart. Confirmed live, 2026-09-11
    ("Name isn't valid. 'paramName' isn't recognized" when a definition was pasted
    into OnStart)."""
    findings = []
    has_udf_def = re.search(r"^[A-Za-z_]\w*\([\w\s:,\[\]]+\)\s*:\s*[A-Za-z]+\s*=", code, flags=re.MULTILINE)
    has_imperative = re.search(r"\b(Set|ClearCollect|Collect|Navigate)\s*\(", code)
    if has_udf_def and has_imperative:
        findings.append("This block mixes a UDF definition (Name(params): Type = ...) with imperative statements (Set/ClearCollect/...) - UDF definitions must be pasted into the App's separate Formulas property, never OnStart or a button's OnSelect, or Studio throws a misleading error at the parameter name")
    return findings


def check_unescaped_ampersand_in_markup_strings(code: str) -> list[str]:
    """A literal & inside a Power Fx string literal that is building HTML/SVG/XML
    markup, not followed by a real XML entity, produces invalid XML when that
    string ends up as element text content. Confirmed live, 2026-09-11 (Media &
    Comms / Policy & Pers department names broke SVG parsing before being fixed to
    &amp;). Only flags string literals that look like markup (contain '<' or a
    common tag), to avoid false positives on ordinary data/business logic strings."""
    findings = []
    entity_ok = re.compile(r"&(amp|lt|gt|quot|apos|nbsp|mdash|ndash|hellip|rarr|larr|middot|times|#\d+|#x[0-9a-fA-F]+);")
    for sm in re.finditer(r'"((?:[^"\\]|\\.)*)"', code):
        literal = sm.group(1)
        if "<" not in literal and not re.search(r"\b(rect|text|svg|line|path|g)\b", literal):
            continue
        for am in re.finditer(r"&", literal):
            tail = literal[am.start():am.start() + 12]
            if not entity_ok.match(tail):
                snippet = literal[max(0, am.start() - 20):am.start() + 20]
                findings.append(f"Bare '&' inside a markup-shaped string literal (not a valid XML entity) - will break XML parsing: ...{snippet}...")
    return findings


def _find_matching_brace(code: str, open_pos: int) -> int | None:
    """code[open_pos] must be '{'. Returns the index of its matching '}',
    respecting Power Fx's ""-doubled-quote string literals so braces inside
    strings never affect the count."""
    depth = 0
    i = open_pos
    in_str = False
    while i < len(code):
        c = code[i]
        if in_str:
            if c == '"':
                if i + 1 < len(code) and code[i + 1] == '"':
                    i += 2
                    continue
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return None


def _split_top_level(text: str, sep: str) -> list[str]:
    """Splits text on sep only at nesting depth 0 - tracks (), {}, [] and ""
    strings so a separator inside any of those is never treated as a split
    point."""
    parts = []
    depth = 0
    in_str = False
    start = 0
    i = 0
    while i < len(text):
        c = text[i]
        if in_str:
            if c == '"':
                if i + 1 < len(text) and text[i + 1] == '"':
                    i += 2
                    continue
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c in "({[":
                depth += 1
            elif c in ")}]":
                depth -= 1
            elif depth == 0 and text.startswith(sep, i):
                parts.append(text[start:i])
                i += len(sep)
                start = i
                continue
        i += 1
    parts.append(text[start:])
    return parts


def check_with_record_self_reference(code: str) -> list[str]:
    """A field inside a single With({...}, body) record can only see the
    ENCLOSING scope in its own definition, never a sibling field defined in
    that same record - regardless of nesting depth or bracket placement.
    Confirmed broken live twice in this Bible under two different guises:
    Phase 10's first run (_fillColor referencing sibling _cat, 2026-09-14)
    and Cadets Org Chart Phase 12's first run (_panelY referencing sibling
    _dept, 2026-09-15 - 'Name isn't valid. \'_dept\' isn't recognized.').
    Both were regressions of an already-known rule, not new discoveries -
    this check exists so a third occurrence gets caught before Studio, not
    after."""
    findings = []
    for m in re.finditer(r"\bWith\s*\(", code):
        # find the record literal - the first non-whitespace char after '(' must be '{'
        j = m.end()
        while j < len(code) and code[j] in " \t\r\n":
            j += 1
        if j >= len(code) or code[j] != "{":
            continue
        close = _find_matching_brace(code, j)
        if close is None:
            continue
        record_text = code[j + 1:close]
        fields = {}
        for field in _split_top_level(record_text, ","):
            parts = _split_top_level(field, ":")
            if len(parts) < 2:
                continue
            name = parts[0].strip()
            expr = ":".join(parts[1:])
            if re.fullmatch(r"[A-Za-z_]\w*", name):
                fields[name] = expr
        if len(fields) < 2:
            continue
        for name, expr in fields.items():
            for other in fields:
                if other == name:
                    continue
                if re.search(rf"\b{re.escape(other)}\b", expr):
                    findings.append(
                        f"With({{...}}) field '{name}' appears to reference sibling field '{other}' defined in the "
                        f"same record - only the enclosing scope is visible here, never another field in this record "
                        f"(confirmed live twice: Phase 10's _fillColor/_cat, Cadets Org Chart Phase 12's _panelY/_dept)"
                    )
    return findings


def check_balance(code: str) -> list[str]:
    findings = []
    for openc, closec, name in [("(", ")", "parentheses"), ("{", "}", "braces")]:
        o, c = code.count(openc), code.count(closec)
        if o != c:
            findings.append(f"Unbalanced {name}: {o} '{openc}' vs {c} '{closec}'")
    return findings


CHECKS = [
    check_addcolumns_groupby_quoted_names,
    check_base64,
    check_udf_table_param,
    check_udf_definition_shape,
    check_unescaped_ampersand_in_markup_strings,
    check_with_record_self_reference,
    check_balance,
]


def audit_block(code: str) -> list[str]:
    findings = []
    for check in CHECKS:
        findings.extend(check(code))
    return findings


def audit_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    total_findings = 0
    if path.suffix == ".md":
        blocks = [(line, None, code) for line, code in extract_md_blocks(text)]
    else:
        blocks = extract_html_pre_blocks(text)

    if not blocks:
        print(f"{path}: no code blocks found")
        return 0

    for line, block_id, code in blocks:
        findings = audit_block(code)
        label = f"line {line}" + (f" (id={block_id})" if block_id else "")
        if findings:
            print(f"{path} [{label}]: {len(findings)} finding(s)")
            for f in findings:
                print(f"  - {f}")
            total_findings += len(findings)
    return total_findings


def diff_md_against_html(md_path: Path, html_path: Path) -> int:
    md_text = md_path.read_text(encoding="utf-8")
    html_text = html_path.read_text(encoding="utf-8")
    md_blocks = [code for _, code in extract_md_blocks(md_text)]
    # A <pre id="...">CODE\n</pre> block's content includes a trailing newline before
    # the closing tag that a ```-fenced block's captured content does not - harmless
    # (copy-paste into Studio ignores trailing whitespace), so normalise it away
    # rather than flag every single block as "drifted" over nothing.
    html_blocks = [code.rstrip("\n") for _, _, code in extract_html_pre_blocks(html_text)]

    missing = 0
    for i, code in enumerate(md_blocks):
        if code.rstrip("\n") not in html_blocks:
            print(f"{md_path}: fenced block #{i+1} not found verbatim anywhere in {html_path}'s <pre> blocks - local file and published guide have drifted")
            missing += 1
    if not missing:
        print(f"OK: every fenced block in {md_path} appears verbatim in {html_path}")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Power Fx formula blocks in .md/.html files.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--diff", action="store_true", help="Treat the two given paths as (local .md, published .html) and check for drift instead of pattern-auditing each.")
    args = parser.parse_args()

    if args.diff:
        if len(args.paths) != 2:
            print("error: --diff requires exactly two paths (local .md, published .html)", file=sys.stderr)
            return 2
        missing = diff_md_against_html(args.paths[0], args.paths[1])
        return 1 if missing else 0

    total = 0
    for p in args.paths:
        if not p.exists():
            print(f"error: {p} does not exist", file=sys.stderr)
            return 2
        total += audit_file(p)

    if total:
        print(f"\n{total} total finding(s) across {len(args.paths)} file(s)")
        return 1
    print(f"\nAll clear across {len(args.paths)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
