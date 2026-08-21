"""Structural checks on the lessons.

These are cheap and catch the things that actually break a tutorial: a
notebook that will not open, a lesson missing from the syllabus, or a stray
API key pasted into a cell.
"""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))


def test_notebooks_exist():
    assert NOTEBOOKS, "no notebooks found"


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_is_valid_json_with_cells(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    assert nb["nbformat"] == 4
    assert nb["cells"], f"{path.name} has no cells"


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_has_no_committed_outputs(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            assert not cell.get("outputs"), f"{path.name} cell {i} has outputs; run `make strip`"


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_contains_no_api_key(path):
    assert not re.search(r"sk-ant-[A-Za-z0-9_-]{8,}", path.read_text(encoding="utf-8")), (
        f"{path.name} looks like it contains a real API key"
    )


def test_every_notebook_is_in_the_syllabus():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing = [p.name for p in NOTEBOOKS if p.name not in readme]
    assert not missing, f"not listed in README syllabus: {missing}"
