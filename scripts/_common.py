#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from typing import Optional


MARKER = "learning-workspace.yaml"
ALLOWED_STATES = {"planned", "active", "completed", "maintenance", "archived"}


def find_workspace(start: Optional[str] = None) -> Path:
    current = Path(start or ".").resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / MARKER).is_file():
            return candidate
    raise SystemExit(f"No {MARKER} found from {current}")


def parse_simple_yaml(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    if not path.exists():
        return data
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        if value == "":
            parsed: object = ""
        elif value.lower() in {"true", "false"}:
            parsed = value.lower() == "true"
        elif re.fullmatch(r"-?\d+", value):
            parsed = int(value)
        else:
            parsed = value
        data[key.strip()] = parsed
    return data


def config(root: Path) -> dict[str, object]:
    defaults: dict[str, object] = {
        "learning_root": "learning",
        "inbox_root": "inbox",
        "active_course_limit": 4,
        "minimum_minutes_per_course": 90,
        "weekly_buffer_percent": 15,
        "weekly_minutes": 600,
    }
    defaults.update(parse_simple_yaml(root / MARKER))
    return defaults


def learning_dir(root: Path, cfg: dict[str, object]) -> Path:
    return root / str(cfg["learning_root"])


def course_dir(root: Path, cfg: dict[str, object], course_id: str) -> Path:
    return learning_dir(root, cfg) / "courses" / course_id


def read_frontmatter(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    data: dict[str, object] = {}
    for raw in text[4:end].splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        if value == "":
            parsed: object = ""
        elif value.lower() in {"true", "false"}:
            parsed = value.lower() == "true"
        elif re.fullmatch(r"-?\d+", value):
            parsed = int(value)
        else:
            parsed = value
        data[key.strip()] = parsed
    return data


def replace_frontmatter_value(path: Path, key: str, value: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    replacement = f"{key}: {value}"
    if pattern.search(text):
        text = pattern.sub(replacement, text, count=1)
    else:
        end = text.find("\n---", 4)
        if end < 0:
            raise SystemExit(f"Invalid frontmatter: {path}")
        text = text[:end] + f"\n{replacement}" + text[end:]
    path.write_text(text, encoding="utf-8")


def valid_course_id(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value))


def today() -> str:
    return dt.date.today().isoformat()


def append_unique(path: Path, line: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if line not in text:
        with path.open("a", encoding="utf-8") as handle:
            if text and not text.endswith("\n"):
                handle.write("\n")
            handle.write(line + "\n")


def update_portfolio_status(root: Path, cfg: dict[str, object], course_id: str, status: str) -> None:
    path = learning_dir(root, cfg) / "portfolio.md"
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = False
    for index, line in enumerate(lines):
        if line.startswith(f"| {course_id} |"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 3:
                cells[2] = status
                lines[index] = "| " + " | ".join(cells) + " |"
                changed = True
    if changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
