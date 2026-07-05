#!/usr/bin/env python3
"""
Consolidate every reference/*.md file into one page: reference/database.html.

Run this after editing any reference/*.md file to republish the single
consolidated database page. Requires the `markdown` package:
    pip install --user markdown
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "reference"

ORDER = [
    ("powerapps-bible.md", "Overview & Entry Point"),
    ("known-bad-patterns.md", "Known Bad Patterns"),
    ("verified-control-reference.md", "Verified Control Reference"),
    ("powerapps-control-defaults.md", "Control Defaults (Fresh-Control Lab)"),
    ("live-build-lessons.md", "Live Build Lessons"),
    ("real-build-quirks.md", "Real Build Quirks"),
    ("ui-patterns.md", "UI Patterns"),
    ("powerfx-patterns.md", "Power Fx Patterns"),
    ("sharepoint-office365users.md", "SharePoint & Office365Users"),
    ("yaml-validation-checklist.md", "YAML Validation Checklist"),
    ("builder-system.md", "Builder System"),
    ("project-repo-workflow.md", "Project Repo Workflow"),
    ("guide-authoring-rules.md", "Guide Authoring Rules"),
    ("output-format.md", "Output Format"),
    ("future-guide-template.md", "Future Guide Template"),
    ("README.md", "Reference Pack README"),
]


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def build() -> str:
    md = markdown.Markdown(extensions=["fenced_code", "tables", "toc"])
    sections = []
    toc_items = []
    for fname, title in ORDER:
        p = REF / fname
        if not p.exists():
            print("MISSING:", fname)
            continue
        text = p.read_text()
        md.reset()
        body_html = md.convert(text)
        anchor = slugify(fname)
        sections.append(
            f'<section id="{anchor}">\n<div class="src-tag">{html.escape(fname)}</div>\n'
            f"<h1>{html.escape(title)}</h1>\n{body_html}\n</section>"
        )
        toc_items.append(
            f'<li><a href="#{anchor}">{html.escape(title)}</a> <code>{html.escape(fname)}</code></li>'
        )

    toc = "\n".join(toc_items)
    sections_html = "\n<hr/>\n".join(sections)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Power Apps Bible — Consolidated Database</title>
<style>
:root {{
  --bg: #f6efe4;
  --paper: #fffaf1;
  --ink: #2b2118;
  --muted: #725f4d;
  --line: #dfcdb3;
  --line-strong: #c5a56d;
  --brass: #b9852f;
  --brass-dark: #75501b;
  --blue: #1c3352;
  --blue-soft: #e7eef7;
  --code-bg: #1e1a14;
  --code-ink: #f0e6d2;
  --sans: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --mono: "Cascadia Code", "Consolas", ui-monospace, monospace;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: linear-gradient(180deg, #fbf5eb 0%, var(--bg) 48%, #efe1cf 100%);
  color: var(--ink);
  font-family: var(--sans);
  line-height: 1.6;
}}
a {{ color: var(--blue); }}
.page {{ width: min(980px, 100%); margin: 0 auto; padding: 28px; }}
.back {{ display: inline-flex; margin-bottom: 16px; color: var(--brass-dark); font-weight: 850; text-decoration: none; }}
.hero {{ border: 1px solid var(--line); background: rgba(255,250,241,.92); box-shadow: 0 18px 45px rgba(49,34,20,.12); padding: 32px; border-radius: 20px; margin-bottom: 24px; }}
.eyebrow {{ display: inline-flex; margin-bottom: 12px; border: 1px solid rgba(185,133,47,.35); background: rgba(185,133,47,.12); color: var(--brass-dark); border-radius: 999px; padding: 4px 9px; font-size: .76rem; font-weight: 850; letter-spacing: .08em; text-transform: uppercase; }}
h1 {{ margin: 0 0 8px; color: var(--blue); }}
.intro {{ color: var(--muted); max-width: 760px; }}
.toc {{ border: 1px solid var(--line); background: var(--paper); border-radius: 16px; padding: 20px 24px; margin-bottom: 32px; }}
.toc h2 {{ margin-top: 0; color: var(--blue); font-size: 1.1rem; }}
.toc ol {{ margin: 0; padding-left: 22px; }}
.toc li {{ margin-bottom: 6px; }}
.toc code {{ color: var(--muted); font-size: .82em; }}
section {{ background: var(--paper); border: 1px solid var(--line); border-radius: 16px; padding: 28px 32px; margin-bottom: 20px; }}
.src-tag {{ display: inline-block; font-family: var(--mono); font-size: .72rem; color: var(--brass-dark); background: rgba(185,133,47,.12); border: 1px solid rgba(185,133,47,.3); border-radius: 999px; padding: 2px 10px; margin-bottom: 10px; }}
section h1 {{ font-size: 1.6rem; border-bottom: 2px solid var(--line-strong); padding-bottom: 8px; }}
section h2 {{ color: var(--blue); font-size: 1.25rem; margin-top: 28px; }}
section h3 {{ color: var(--brass-dark); font-size: 1.05rem; }}
section p, section li {{ color: var(--ink); }}
section code {{ font-family: var(--mono); background: rgba(43,33,24,.08); padding: 1px 5px; border-radius: 4px; font-size: .88em; }}
section pre {{ background: var(--code-bg); color: var(--code-ink); padding: 14px 16px; border-radius: 10px; overflow-x: auto; font-size: .85rem; }}
section pre code {{ background: none; padding: 0; color: inherit; }}
section table {{ border-collapse: collapse; width: 100%; margin: 14px 0; font-size: .88rem; }}
section th, section td {{ border: 1px solid var(--line); padding: 6px 10px; text-align: left; vertical-align: top; }}
section th {{ background: var(--blue-soft); color: var(--blue); }}
hr {{ border: none; }}
.footer-note {{ color: var(--muted); font-size: .85rem; margin-top: 24px; }}
</style>
</head>
<body>
<main class="page">
  <a class="back" href="index.html">← Reference pack</a>
  <section class="hero" style="margin-bottom:0;">
    <span class="eyebrow">Single Point of Truth</span>
    <h1>Power Apps Bible — Consolidated Database</h1>
    <p class="intro">Every reference document in this repo, concatenated onto one page in reading order, so any future session — human or AI — can fetch this single URL and have the entire accumulated Power Apps knowledge base for this project family, instead of guessing which of 16 separate files to check. Each section is tagged with its source filename — edit that file directly, then re-run the consolidation build to republish this page.</p>
  </section>

  <div class="toc">
    <h2>Contents (in order below)</h2>
    <ol>
{toc}
    </ol>
  </div>

{sections_html}

  <p class="footer-note">Generated from <code>reference/*.md</code> in <a href="https://github.com/Phaderon/PowerApps">Phaderon/PowerApps</a>. Source markdown files remain the editable originals — this page is a build artifact, not hand-maintained.</p>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    out = build()
    dest = REF / "database.html"
    dest.write_text(out)
    print(f"Written {dest} — {len(out)} bytes")
