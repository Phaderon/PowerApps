#!/usr/bin/env python3
"""Audit Power Apps HTML guides for known bad patterns."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_PATTERNS: list[tuple[str, str]] = [
    (r"ScreenTransition\.Back", "Use Back() or a valid ScreenTransition enum; ScreenTransition.Back is invalid."),
    (r"\bThisItem\.ItemIndex\b", "Do not use gallery row index properties."),
    (r"\bsame technique as\b", "Avoid vague cross-reference instructions."),
    (r"\bsee above\b", "Avoid vague cross-reference instructions."),
    (r"duplicate from previous screen", "Avoid duplicate-by-reference instructions."),
    (r"group these controls", "Avoid instructions that depend on unavailable/fragile grouping."),
    (r"\[\]", "Avoid schema-less empty table literals."),
    (r"\bScreenTransition\.(?!Fade\b|None\b|Cover\b|UnCover\b)\w+", "Check this ScreenTransition enum against Microsoft Learn/editor."),
    (r"\bSortByColumns\([^<]*(?<!SortOrder\.)Ascending\b", "Use SortOrder.Ascending, not bare Ascending."),
    (r"\bSortByColumns\([^<]*(?<!SortOrder\.)Descending\b", "Use SortOrder.Descending, not bare Descending."),
    (r"\bTimeUnit\.Days\b", "Training Tracker day filters should preserve the verified quoted unit \"Days\" unless rechecked."),
    (r"DisplayMode=View\b", "Use DisplayMode=DisplayMode.View for copy/paste-safe enum syntax."),
    (r"\btgl[A-Za-z0-9_]*\.Value\b", "Modern Toggle-like controls should be read with .Checked, not .Value."),
    (r"<p><strong>[^<]+</strong>\s*(?:—|-|&mdash;).*?\b(?:X|W|H)=", "Control property instructions should be table rows, not long inline paragraphs."),
]


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def strip_code_note_sections(text: str) -> str:
    """Keep the audit practical by not matching the final known-bad-pattern prose."""
    return text


def find_combo_placeholder_errors(text: str) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []
    for row in re.finditer(r"<tr>.*?</tr>", text, flags=re.IGNORECASE | re.DOTALL):
        row_text = row.group(0)
        if re.search(r"Combo box \(modern", row_text, flags=re.IGNORECASE):
            if re.search(r"(?<!InputText)Placeholder\s*=", row_text):
                errors.append((line_for_offset(text, row.start()), "Modern Combo box uses Placeholder; use InputTextPlaceholder."))
            if "SelectMultiple" not in row_text:
                errors.append((line_for_offset(text, row.start()), "Modern Combo box row should state SelectMultiple explicitly."))
            if "ItemDisplayText" not in row_text:
                errors.append((line_for_offset(text, row.start()), "Modern Combo box row should state ItemDisplayText explicitly."))
    return errors


def find_text_input_hinttext_errors(text: str) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []
    for row in re.finditer(r"<tr>.*?</tr>", text, flags=re.IGNORECASE | re.DOTALL):
        row_text = row.group(0)
        if re.search(r"Text input \(modern", row_text, flags=re.IGNORECASE):
            if "HintText" in row_text:
                errors.append((line_for_offset(text, row.start()), "Modern Text input uses Placeholder, not HintText."))
    return errors


def find_dropdown_errors(text: str) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []
    for row in re.finditer(r"<tr>.*?</tr>", text, flags=re.IGNORECASE | re.DOTALL):
        row_text = row.group(0)
        if re.search(r"Dropdown \(modern", row_text, flags=re.IGNORECASE):
            line = line_for_offset(text, row.start())
            if "Table(" in row_text and "ItemDisplayText" not in row_text:
                errors.append((line, "Modern Dropdown with table-shaped Items should state ItemDisplayText explicitly."))
            if "displayed value field" in row_text.lower() or "value field" in row_text.lower():
                errors.append((line, "Use ItemDisplayText for modern Dropdown display text instead of old value-field wording."))
    return errors


def find_radius_shape_errors(text: str) -> list[tuple[int, str]]:
    """Rectangle and Label do not support any Radius* property in this app family, confirmed
    three separate times (2026-06-23, 2026-07-04 issue #7, 2026-07-06 this guide's ChipBg/dots).
    Classic Button with DisplayMode.View is the only confirmed-working rounded-shape substitute."""
    errors: list[tuple[int, str]] = []
    for row in re.finditer(r"<tr>.*?</tr>", text, flags=re.IGNORECASE | re.DOTALL):
        row_text = row.group(0)
        cells = re.findall(r"<td>(.*?)</td>", row_text, flags=re.IGNORECASE | re.DOTALL)
        if len(cells) < 2:
            continue
        control_type_cell = cells[1]
        is_rectangle = bool(re.search(r"\bRectangle\b", control_type_cell, re.IGNORECASE))
        is_label = bool(re.search(r"^\s*Label\b", control_type_cell, re.IGNORECASE))
        is_button_workaround = bool(re.search(r"Classic\s*/?\s*Button", control_type_cell, re.IGNORECASE))
        has_radius = bool(re.search(r"radius", row_text, re.IGNORECASE))
        if (is_rectangle or is_label) and not is_button_workaround and has_radius:
            errors.append((
                line_for_offset(text, row.start()),
                "Rectangle/Label row mentions radius - neither control supports Radius* properties. "
                "Use Classic Button with DisplayMode.View + Text=blank instead.",
            ))
    return errors


def find_radius_shape_errors_yaml(text: str) -> list[tuple[int, str]]:
    """Same rule as find_radius_shape_errors but for real pasteable YAML code blocks
    (Control: Rectangle@2.3.0 / Control: Label@2.5.1 ...) rather than <table> guide rows.
    Added 2026-07-10 after this exact mistake shipped in the Thursday Date Picker guide --
    the table-row checker above only ever looked inside <tr> rows and had no way to see a
    control type that only appears as a bare `Control: X@Y` line inside a <pre> block."""
    errors: list[tuple[int, str]] = []
    for block in re.finditer(r"<pre>(.*?)</pre>", text, flags=re.IGNORECASE | re.DOTALL):
        block_text = block.group(1)
        block_start = block.start(1)
        pending_type: str | None = None
        pending_offset = 0
        for line_match in re.finditer(r"[^\n]*\n?", block_text):
            line = line_match.group(0)
            if not line:
                continue
            ctrl_match = re.search(r"Control:\s*(Rectangle|Label|Classic\s*/\s*Button|[A-Za-z]+)@", line)
            if ctrl_match:
                pending_type = ctrl_match.group(1).replace(" ", "")
                pending_offset = block_start + line_match.start()
                continue
            if pending_type and pending_type.lower() in ("rectangle", "label") and re.search(r"\bRadius(TopLeft|TopRight|BottomLeft|BottomRight)?\s*:", line):
                errors.append((
                    line_for_offset(text, block_start + line_match.start()),
                    f"YAML block: Control: {pending_type}@... (around line {line_for_offset(text, pending_offset)}) followed by a Radius* property -- neither Rectangle nor Label supports Radius. Use Classic/Button@2.2.0 with DisplayMode.View, or GroupContainer/ModernText if text-bearing.",
                ))
    return errors


def find_missing_fillportions_errors(text: str) -> list[tuple[int, str]]:
    """A GroupContainer/control with an explicit Height or Width, nested directly under a
    Variant: AutoLayout container's Children, needs FillPortions stated explicitly (0 for
    fixed-size, 1+ for the one region meant to stretch) or it silently ignores its own
    Height/Width and expands to fill the parent's remaining space -- confirmed root cause,
    ViewItem_1 conTopBar1/conWarningBar1/conCompactStepper1 (2026-07-05) and again on
    ThursdayPickerModal1's conThuModalCard1 (2026-07-10), both times the working reference
    pattern (DeleteItemModal1: FillPortions: =0 on its fixed conModalData1/conHeaderPopUp1,
    FillPortions: =1 on the one stretchy txtModalText1) was already available and not copied
    over. Uses a real YAML parse of each <pre> block rather than regex, since this needs
    actual parent/child structure, not line-adjacency guessing."""
    import yaml

    errors: list[tuple[int, str]] = []

    def walk(node, in_autolayout_children: bool, block_start: int, block_text: str):
        if isinstance(node, list):
            for item in node:
                if isinstance(item, dict):
                    for ctrl_name, ctrl_def in item.items():
                        if not isinstance(ctrl_def, dict):
                            continue
                        props = ctrl_def.get("Properties", {}) or {}
                        if in_autolayout_children:
                            has_size = any(k in props for k in ("Height", "Width"))
                            has_fillportions = "FillPortions" in props
                            if has_size and not has_fillportions:
                                marker = f"{ctrl_name}:"
                                pos = block_text.find(marker)
                                offset = block_start + (pos if pos >= 0 else 0)
                                errors.append((
                                    line_for_offset(text, offset),
                                    f"{ctrl_name} has Height/Width but no FillPortions, and its parent is Variant: AutoLayout -- "
                                    "will silently ignore its own size and stretch to fill remaining space. State FillPortions "
                                    "explicitly (0 to hold the fixed size, 1+ if this is the one region meant to stretch).",
                                ))
                        child_variant = ctrl_def.get("Variant")
                        child_is_autolayout = child_variant == "AutoLayout"
                        children = ctrl_def.get("Children")
                        if children is not None:
                            walk(children, child_is_autolayout, block_start, block_text)

    for block in re.finditer(r"<pre>(.*?)</pre>", text, flags=re.IGNORECASE | re.DOTALL):
        block_text = block.group(1)
        block_start = block.start(1)
        stripped = block_text.strip()
        if not stripped.startswith("-"):
            continue
        try:
            parsed = yaml.safe_load(block_text)
        except Exception:
            continue
        if not isinstance(parsed, list):
            continue
        walk(parsed, False, block_start, block_text)

    return errors


def find_table_concat_errors(text: str) -> list[tuple[int, str]]:
    """`&` only concatenates Text/Number/Date/etc scalars, never two tables. A Table({...})
    literal immediately followed by `&` and an identifier is almost always someone trying to
    union two tables the wrong way - confirmed on Policy Tracker Main, 2026-07-06."""
    errors: list[tuple[int, str]] = []
    for match in re.finditer(r"Table\(\s*\{[^{}]*\}\s*\)\s*&amp;\s*[A-Za-z_]", text):
        errors.append((
            line_for_offset(text, match.start()),
            "Table({...}) & identifier - & cannot concatenate two tables. "
            "Use ClearCollect(coll, {newRow}) then Collect(coll, existingTableOrForAll) instead.",
        ))
    return errors


def find_toggle_errors(text: str) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []
    for row in re.finditer(r"<tr>.*?</tr>", text, flags=re.IGNORECASE | re.DOTALL):
        row_text = row.group(0)
        if re.search(r"Toggle \(modern", row_text, flags=re.IGNORECASE):
            line = line_for_offset(text, row.start())
            if re.search(r"\bDefault\s*=", row_text):
                errors.append((line, "Modern Toggle state should use Checked in this guide family, not Default."))
            if re.search(r"\bText\s*=", row_text):
                errors.append((line, "Modern Toggle caption should use Label, not Text."))
            if re.search(r"\.Value\b", row_text):
                errors.append((line, "Modern Toggle formulas should read .Checked, not .Value."))
    return errors


def audit(path: Path) -> list[tuple[int, str, str]]:
    text = path.read_text(encoding="utf-8")
    findings: list[tuple[int, str, str]] = []

    for pattern, message in TEXT_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            findings.append((line_for_offset(text, match.start()), match.group(0)[:120].replace("\n", " "), message))

    for line, message in find_combo_placeholder_errors(text):
        findings.append((line, "Combo box row", message))

    for line, message in find_text_input_hinttext_errors(text):
        findings.append((line, "Text input row", message))

    for line, message in find_dropdown_errors(text):
        findings.append((line, "Dropdown row", message))

    for line, message in find_toggle_errors(text):
        findings.append((line, "Toggle row", message))

    for line, message in find_radius_shape_errors(text):
        findings.append((line, "Radius on Rectangle/Label", message))

    for line, message in find_radius_shape_errors_yaml(text):
        findings.append((line, "Radius on Rectangle/Label (YAML block)", message))

    for line, message in find_table_concat_errors(text):
        findings.append((line, "Table & concat", message))

    for line, message in find_missing_fillportions_errors(text):
        findings.append((line, "Missing FillPortions in AutoLayout", message))

    return sorted(findings, key=lambda item: item[0])


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a Power Apps guide HTML file for known bad patterns.")
    parser.add_argument("path", type=Path, help="Path to guide index.html")
    args = parser.parse_args()

    if not args.path.exists():
        print(f"error: {args.path} does not exist", file=sys.stderr)
        return 2

    findings = audit(args.path)
    if findings:
        print(f"{args.path}: {len(findings)} finding(s)")
        for line, snippet, message in findings:
            print(f"  line {line}: {message}")
            print(f"    matched: {snippet}")
        return 1

    print(f"{args.path}: audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
