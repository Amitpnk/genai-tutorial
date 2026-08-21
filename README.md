# GenAI Tutorial

A hands-on course in building generative AI applications with Claude. Nine
notebook lessons take you from a first API call to a retrieval-augmented,
evaluated, cost-instrumented system, followed by three capstone projects.

Everything runs against the real Claude API. Working through all nine lessons
costs roughly **$1–2** in API usage.

## Quick start

```bash
git clone <your-repo-url> && cd genai-tutorial
make setup                    # creates .venv, installs the package + extras
cp .env.example .env          # then add your ANTHROPIC_API_KEY
make lab                      # opens JupyterLab in notebooks/
```

No `make`? The equivalent commands are in [docs/setup.md](docs/setup.md).

Start with `notebooks/00-setup-and-hello-claude.ipynb`.

## Syllabus

| # | Lesson | You will be able to | Cost |
|---|--------|---------------------|------|
| 00 | [Setup and Hello Claude](notebooks/00-setup-and-hello-claude.ipynb) | Make your first API call; read content blocks and usage | < $0.01 |
| 01 | [Prompting Fundamentals](notebooks/01-prompting-fundamentals.ipynb) | Use system prompts, examples, and effort deliberately | ~$0.05 |
| 02 | [Structured Output](notebooks/02-structured-output.ipynb) | Get schema-valid JSON instead of parsing prose | ~$0.05 |
| 03 | [Tool Use](notebooks/03-tool-use.ipynb) | Define tools and run the agentic loop | ~$0.10 |
| 04 | [Embeddings and Vector Search](notebooks/04-embeddings-and-vector-search.ipynb) | Chunk, embed, index, and retrieve | ~$0.05 |
| 05 | [Building a RAG Pipeline](notebooks/05-rag-pipeline.ipynb) | Ground answers in retrieved context, with citations | ~$0.15 |
| 06 | [Agents and Loops](notebooks/06-agents-and-loops.ipynb) | Decide whether you need an agent, then bound it | ~$0.30 |
| 07 | [Evaluation](notebooks/07-evaluation.ipynb) | Measure changes instead of guessing at them | ~$0.20 |
| 08 | [Production Concerns](notebooks/08-production-concerns.ipynb) | Cache, stream, handle errors, track spend | ~$0.15 |

Then pick a capstone from [`projects/`](projects/).

## Repository layout

```
notebooks/     Guided lessons. Run top to bottom; exercises are marked TODO.
solutions/     Completed exercises. Try first, then compare.
src/           The genai_tutorial package the notebooks import.
projects/      Capstone builds, each self-contained with its own README.
data/raw/      Small sample corpus used by the retrieval lessons.
docs/          Setup, glossary, troubleshooting.
tests/         Offline tests that keep the examples from rotting.
```

The `src/` package exists so lesson cells stay short. Client setup, chunking,
tool definitions, and scorers live there; the notebooks import them and spend
their cells on the idea being taught.

## Requirements

- Python 3.10 or newer
- An Anthropic API key ([console.anthropic.com](https://console.anthropic.com/settings/keys))
- About 6 hours for the lessons, plus project time

Lessons 04 and 05 need the retrieval extras: `pip install -e ".[rag]"`.

## Model

Lessons default to `claude-opus-5`. To cut costs while iterating, set
`GENAI_TUTORIAL_MODEL=claude-haiku-4-5` in `.env` — every lesson honours it.
Lesson 01 has you compare output across models and effort levels, which is
worth doing before you settle on a default for your own work.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The main rule: strip notebook outputs
before committing (`make strip`, or install the hook via `make setup`).

## Licence

MIT — see [LICENSE](LICENSE).
