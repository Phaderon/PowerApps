"""Structural checks on generated Power Fx, beyond the balance check.

The balance check (parens/quotes) passes happily on a record with a trailing comma --
`{a: 1, b: 2,}` -- which Studio rejects with "contains 'CurlyClose' where 'Ident' is
expected". That shipped once, so it is checked explicitly here now, along with the
equivalent dangling separators before a close paren or bracket.
"""
import re, sys

FILES = sys.argv[1:] or ["phase12_onstart.txt", "phase12_recalc.txt"]


def strip_strings(s):
    """Blank out "" string literals (Power Fx escapes a quote by doubling it) so the
    structural checks never trip over punctuation that lives inside a label."""
    out, i, n, instr = [], 0, len(s), False
    while i < n:
        c = s[i]
        if c == '"':
            if instr and i + 1 < n and s[i + 1] == '"':
                out.append("  ")
                i += 2
                continue
            instr = not instr
            out.append('"')
        else:
            out.append(" " if instr and c not in "\r\n" else c)
        i += 1
    return "".join(out)


bad = 0
for f in FILES:
    src = open(f, encoding="utf-8").read()
    code = strip_strings(src)

    for label, pattern in (
        ("trailing comma before }", r",\s*\}"),
        ("trailing comma before )", r",\s*\)"),
        ("trailing comma before ]", r",\s*\]"),
        ("empty record {}", r"\{\s*\}"),
        ("doubled comma", r",\s*,"),
    ):
        for m in re.finditer(pattern, code):
            line = code[:m.start()].count("\n") + 1
            print(f"  {f}:{line}  {label}: {src.splitlines()[line-1].strip()[:90]}")
            bad += 1

    depth = code.count("(") - code.count(")")
    braces = code.count("{") - code.count("}")
    if depth or braces:
        print(f"  {f}: unbalanced -- parens {depth:+d}, braces {braces:+d}")
        bad += 1
    if code.count('"') % 2:
        print(f"  {f}: odd number of quote delimiters")
        bad += 1

print("FORMULA STRUCTURE:", "OK" if not bad else f"{bad} PROBLEM(S)")
sys.exit(1 if bad else 0)
