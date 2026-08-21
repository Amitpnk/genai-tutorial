# Setup

## 1. Python

You need **Python 3.10 or newer**. Check what you have:

```bash
python --version
```

If that reports 3.9 or older, install a newer Python before continuing —
several dependencies and the type syntax used throughout `src/` require 3.10+.
On Windows, [python.org](https://www.python.org/downloads/) or `winget install
Python.Python.3.12`; on macOS, `brew install python@3.12`.

## 2. Install

With `make`:

```bash
make setup
```

Without `make` (Windows PowerShell shown; drop the `.exe`/`Scripts` for Unix):

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\pip.exe install -e ".[rag,notebooks,dev]"
.venv\Scripts\nbstripout.exe --install
```

The `-e` (editable) install matters: edits you make in `src/genai_tutorial/`
during the exercises take effect without reinstalling.

## 3. API key

Get a key at [console.anthropic.com](https://console.anthropic.com/settings/keys),
then:

```bash
cp .env.example .env
```

and put the key in `.env`. That file is gitignored. Do not paste a key into a
notebook cell — notebook outputs and cell source both end up in git history,
and a leaked key is someone else's bill.

Verify:

```bash
python -c "from genai_tutorial import ask; print(ask('Say OK and nothing else.'))"
```

## 4. Set a spending limit

Before your first run, set a monthly limit in the console under Billing →
Limits. The whole tutorial costs $1–2, but a runaway loop in lesson 06 can
spend more than that in a minute. A limit turns a bad afternoon into a 429.

## 5. Launch

```bash
make lab
```

or `jupyter lab --notebook-dir=notebooks`. Start at
`00-setup-and-hello-claude.ipynb`.

## Optional: choose a cheaper model

Add to `.env`:

```
GENAI_TUTORIAL_MODEL=claude-haiku-4-5
```

Every lesson reads this. Haiku is markedly cheaper and fine for lessons 00–05;
switch back to `claude-opus-5` for the agent and evaluation lessons, where the
difference in reasoning quality is part of what you are observing.
