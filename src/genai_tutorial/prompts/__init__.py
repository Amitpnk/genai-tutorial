"""Prompt templates kept as files, not inline strings.

Treating prompts as versioned assets is the point: `git log` on this directory
becomes the change history for your system's behaviour, and lesson 07 diffs
eval scores across those versions.
"""

from pathlib import Path

PROMPT_DIR = Path(__file__).parent


def load(name: str) -> str:
    """Load a prompt template by stem, e.g. load("triage_system")."""
    path = PROMPT_DIR / f"{name}.md"
    if not path.exists():
        available = sorted(p.stem for p in PROMPT_DIR.glob("*.md"))
        raise FileNotFoundError(f"No prompt named {name!r}. Available: {available}")
    return path.read_text(encoding="utf-8")
