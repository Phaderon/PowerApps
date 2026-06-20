#!/usr/bin/env python3
"""Build and query a local Power Apps / Power Platform docs index."""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / ".cache" / "powerapps-bible.sqlite"
DEFAULT_ROOTS = [
    ROOT / "reference",
    ROOT / ".sources" / "powerapps-docs",
    ROOT / ".sources" / "power-platform",
]
EXTENSIONS = {".md", ".yml", ".yaml"}


@dataclass(frozen=True)
class Doc:
    path: Path
    source: str
    title: str
    body: str


def title_from_text(path: Path, text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    yaml_title = re.search(r"^title:\s*(.+)$", text, flags=re.MULTILINE)
    if yaml_title:
        return yaml_title.group(1).strip().strip('"')
    return path.stem.replace("-", " ").replace("_", " ").title()


def source_for(path: Path) -> str:
    try:
        rel = path.relative_to(ROOT / ".sources")
        return rel.parts[0]
    except ValueError:
        pass
    try:
        path.relative_to(ROOT / "reference")
        return "local-reference"
    except ValueError:
        return "local"


def iter_docs() -> list[Doc]:
    docs: list[Doc] = []
    for root in DEFAULT_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.suffix.lower() not in EXTENSIONS:
                continue
            if any(part in {".git", "node_modules", "media", "images"} for part in path.parts):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            rel = path.relative_to(ROOT)
            docs.append(Doc(rel, source_for(path), title_from_text(path, text), text))
    return docs


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def rebuild() -> None:
    docs = iter_docs()
    with connect() as db:
        db.executescript(
            """
            DROP TABLE IF EXISTS docs;
            DROP TABLE IF EXISTS docs_fts;
            CREATE TABLE docs (
              id INTEGER PRIMARY KEY,
              path TEXT NOT NULL UNIQUE,
              source TEXT NOT NULL,
              title TEXT NOT NULL,
              body TEXT NOT NULL
            );
            CREATE VIRTUAL TABLE docs_fts USING fts5(
              title,
              body,
              content='docs',
              content_rowid='id'
            );
            """
        )
        db.executemany(
            "INSERT INTO docs(path, source, title, body) VALUES (?, ?, ?, ?)",
            [(str(doc.path), doc.source, doc.title, doc.body) for doc in docs],
        )
        db.execute("INSERT INTO docs_fts(rowid, title, body) SELECT id, title, body FROM docs")
    print(f"Indexed {len(docs)} documents into {DB_PATH}")


def snippet(text: str, terms: list[str], length: int = 260) -> str:
    lowered = text.lower()
    positions = [lowered.find(term.lower()) for term in terms if lowered.find(term.lower()) >= 0]
    start = max(min(positions) - 80, 0) if positions else 0
    chunk = re.sub(r"\s+", " ", text[start : start + length]).strip()
    return chunk


def fts_query(raw: str) -> tuple[str, list[str]]:
    terms = re.findall(r"[A-Za-z0-9_]+", raw)
    if not terms:
        return raw, []
    return " AND ".join(terms), terms


def search(query: str, limit: int) -> int:
    if not DB_PATH.exists():
        print("Index missing. Run: python3 tools/index-msdocs.py --rebuild", file=sys.stderr)
        return 2
    normalized_query, terms = fts_query(query)
    with connect() as db:
        rows = db.execute(
            """
            SELECT docs.path, docs.source, docs.title, docs.body, bm25(docs_fts) AS rank
            FROM docs_fts
            JOIN docs ON docs.id = docs_fts.rowid
            WHERE docs_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (normalized_query, limit),
        ).fetchall()
    for idx, (path, source, title, body, _rank) in enumerate(rows, start=1):
        print(f"{idx}. [{source}] {title}")
        print(f"   {path}")
        print(f"   {snippet(body, terms)}")
    if not rows:
        print("No matches.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build/search the local PowerApps Bible documentation index.")
    parser.add_argument("query", nargs="?", help="FTS query, for example: ItemDisplayText Combo box")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild the SQLite FTS index.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum search results.")
    args = parser.parse_args()

    if args.rebuild:
        rebuild()
    if args.query:
        return search(args.query, args.limit)
    if not args.rebuild:
        parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
