#!/usr/bin/env python3
"""Generate a curated defaults reference from fresh Power Apps lab exports."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCES = [
    ("Classic fresh-control lab", ROOT / ".sources" / "default-lab" / "LabClassic.txt"),
    ("Modern fresh-control lab", ROOT / ".sources" / "default-lab" / "LabModern.txt"),
]
DEFAULT_OUTPUT = ROOT / "reference" / "powerapps-control-defaults.md"
LAYOUT_PLACEMENT_PROPS = {"X", "Y"}


@dataclass
class Control:
    source: str
    name: str
    path: tuple[str, ...]
    depth: int
    control: str = ""
    variant: str = ""
    layout: str = ""
    properties: dict[str, str] = field(default_factory=dict)


def clean_value(value: str) -> str:
    return value.strip()


def parse_export(source_name: str, path: Path) -> list[Control]:
    controls: list[Control] = []
    stack: list[tuple[int, Control]] = []
    props_for: Control | None = None
    props_indent = -1

    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw.rstrip("\r\n")
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        control_match = re.match(r"^\s*-\s+([^:]+):\s*$", line)
        if control_match:
            while stack and stack[-1][0] >= indent:
                stack.pop()
            parent_path = stack[-1][1].path if stack else ()
            name = control_match.group(1).strip()
            control = Control(
                source=source_name,
                name=name,
                path=parent_path + (name,),
                depth=len(stack),
            )
            controls.append(control)
            stack.append((indent, control))
            props_for = None
            props_indent = -1
            continue

        current = None
        for item_indent, candidate in reversed(stack):
            if item_indent < indent:
                current = candidate
                break
        if current is None:
            props_for = None
            continue

        if props_for is not None and indent <= props_indent:
            props_for = None
            props_indent = -1

        key_value = re.match(r"^\s*([A-Za-z0-9_.]+):\s*(.*)$", line)
        if not key_value:
            continue

        key, value = key_value.group(1), clean_value(key_value.group(2))
        if key == "Control":
            current.control = value
        elif key == "Variant":
            current.variant = value
        elif key == "Layout":
            current.layout = value
        elif key == "Properties":
            props_for = current
            props_indent = indent
        elif key == "Children":
            props_for = None
            props_indent = -1
        elif props_for is current and indent > props_indent:
            current.properties[key] = value

    return controls


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def prop_pairs(properties: dict[str, str], include_layout: bool) -> list[tuple[str, str]]:
    pairs = []
    for key, value in sorted(properties.items(), key=lambda item: item[0].lower()):
        if not include_layout and key in LAYOUT_PLACEMENT_PROPS:
            continue
        pairs.append((key, value))
    return pairs


def prop_summary(properties: dict[str, str]) -> str:
    pairs = prop_pairs(properties, include_layout=False)
    if not pairs:
        return "`none beyond placement`"
    return "; ".join(f"`{key}` -> `{md_escape(value)}`" for key, value in pairs)


def control_heading(control: Control) -> str:
    bits = [f"`{control.name}`", f"`{control.control or 'unknown'}`"]
    if control.variant:
        bits.append(f"variant `{control.variant}`")
    if control.layout:
        bits.append(f"layout `{control.layout}`")
    return " - ".join(bits)


def generate_markdown(controls: list[Control], source_paths: list[tuple[str, Path]]) -> str:
    lines: list[str] = []
    lines.extend(
        [
            "# Power Apps Control Defaults",
            "",
            "Last checked: 2026-06-20",
            "",
            "This reference is generated from fresh controls inserted into the live Power Apps editor without manual edits.",
            "",
            "## Source Evidence",
            "",
        ]
    )
    for label, path in source_paths:
        rel = path.relative_to(ROOT)
        count = sum(1 for control in controls if control.source == label)
        lines.append(f"- {label}: `{rel}` ({count} parsed controls)")
    lines.extend(
        [
            "",
            "## Interpretation Rules",
            "",
            "- Treat these as observed defaults from the user's tenant/editor, not universal Microsoft documentation.",
            "- A serialized property means the fresh control export explicitly contained that property.",
            "- An omitted property means the fresh control did not serialize it; do not invent a literal default value from absence alone.",
            "- `X` and `Y` came from the repeated insert positions in the lab. Do not use them as default evidence.",
            "- `Width`, `Height`, theme colors, font values, generated gallery children, and generated template formulas can be useful evidence, but still check whether the guide is intentionally changing behavior.",
            "- Future guide rows should use this file to remove or label default-only properties as `leave default` or `default/safety check`.",
            "",
            "## Quick Summary",
            "",
            "| Source | Control | Example | Variant/Layout | Serialized properties excluding X/Y |",
            "|---|---|---|---|---|",
        ]
    )

    for control in controls:
        variant_layout = ", ".join(part for part in [control.variant, control.layout] if part) or "-"
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(control.source),
                    f"`{md_escape(control.control or 'unknown')}`",
                    f"`{md_escape(control.name)}`",
                    md_escape(variant_layout),
                    prop_summary(control.properties),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Full Parsed Details", ""])
    for source in dict.fromkeys(control.source for control in controls):
        lines.extend([f"### {source}", ""])
        for control in [item for item in controls if item.source == source]:
            lines.extend(
                [
                    f"#### {control_heading(control)}",
                    "",
                    f"- Path: `{' > '.join(control.path)}`",
                    f"- Depth: `{control.depth}`",
                    "",
                ]
            )
            pairs = prop_pairs(control.properties, include_layout=True)
            if not pairs:
                lines.extend(["No serialized properties.", ""])
                continue
            lines.extend(["| Property | Observed fresh value | Note |", "|---|---|---|"])
            for key, value in pairs:
                note = "placement from lab insert order; ignore as default evidence" if key in LAYOUT_PLACEMENT_PROPS else ""
                lines.append(f"| `{md_escape(key)}` | `{md_escape(value)}` | {md_escape(note)} |")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate reference/powerapps-control-defaults.md")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    controls: list[Control] = []
    missing = [path for _label, path in DEFAULT_SOURCES if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing source: {path}")
        return 2

    for label, path in DEFAULT_SOURCES:
        controls.extend(parse_export(label, path))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generate_markdown(controls, DEFAULT_SOURCES), encoding="utf-8")
    print(f"Wrote {args.output.relative_to(ROOT)} from {len(controls)} parsed controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
