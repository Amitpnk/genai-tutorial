# Usage: make setup, make lab, make test, make lint
# Windows without make? The equivalent commands are in docs/setup.md.

PYTHON ?= python
VENV   ?= .venv
BIN    := $(VENV)/bin
ifeq ($(OS),Windows_NT)
BIN    := $(VENV)/Scripts
endif

.PHONY: help setup lab test test-live lint fmt clean strip

help:
	@echo "setup      Create .venv and install the package with all extras"
	@echo "lab        Launch JupyterLab in notebooks/"
	@echo "test       Run the offline test suite (no API calls)"
	@echo "test-live  Run tests that hit the real API (costs money)"
	@echo "lint       Ruff check + format check"
	@echo "fmt        Ruff autofix + format"
	@echo "strip      Strip outputs from all notebooks before committing"

setup:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/python -m pip install --upgrade pip
	$(BIN)/pip install -e ".[rag,notebooks,dev]"
	$(BIN)/nbstripout --install
	@echo "Done. Copy .env.example to .env and add your API key."

lab:
	$(BIN)/jupyter lab --notebook-dir=notebooks

test:
	$(BIN)/pytest

test-live:
	$(BIN)/pytest -m live

lint:
	$(BIN)/ruff check .
	$(BIN)/ruff format --check .

fmt:
	$(BIN)/ruff check --fix .
	$(BIN)/ruff format .

strip:
	$(BIN)/nbstripout notebooks/*.ipynb solutions/*.ipynb

clean:
	rm -rf .pytest_cache .ruff_cache .index build dist *.egg-info
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
