# Troubleshooting

## `ModuleNotFoundError: No module named 'genai_tutorial'`

The package is not installed into the kernel you are running. Either run
`pip install -e .` inside the active environment, or check that JupyterLab is
using `.venv` — in the notebook, `import sys; print(sys.executable)` should
point inside `.venv`.

## `AuthenticationError: invalid x-api-key`

The key in `.env` is wrong, revoked, or has stray whitespace/quotes around it.
Copy it fresh from the console. `.env` values need no quotes:
`ANTHROPIC_API_KEY=sk-ant-...`

## The key is set but not picked up

`load_dotenv()` looks upward from the working directory. If you launched
Jupyter from somewhere other than the repo root, it may not find `.env`. Launch
with `make lab`, or set the variable in your shell before starting Jupyter.

## `NotFoundError: model not found`

Check the model ID for typos. Current IDs carry no date suffix —
`claude-opus-5`, not `claude-opus-5-20260101`.

## `RateLimitError` / HTTP 429

You are over your rate or spend limit. The SDK retries automatically (twice by
default) with backoff; persistent 429s mean the limit itself needs raising, or
a loop is calling far more than you intended. Check the `retry-after` header
value before retrying by hand.

## `cache_read_input_tokens` is always 0

Something in the cached prefix changes between calls. The usual culprits:

- a timestamp, UUID, or counter in the system prompt
- `json.dumps()` on a dict without `sort_keys=True`
- a tool list built from a set, so ordering varies per process
- a prefix under ~1024 tokens, which is below the minimum cacheable size

Render order is `tools` → `system` → `messages`. Everything volatile goes
*after* the last cache breakpoint.

## The agent loops forever / the bill jumps

You did not cap iterations. Add a `max_iterations` guard and log every tool
call. Set a monthly spend limit in the console as a backstop — see
`docs/setup.md` step 4.

## RAG answers are confidently wrong

Before touching the prompt, print the retrieved chunks. If the right passage
was never retrieved, the fix is in chunking or embedding, and no prompt change
will help. If it *was* retrieved and the answer still contradicts it, then the
fix is in the prompt.

## A notebook cell hangs

Long non-streaming requests with a large `max_tokens` can approach the HTTP
timeout. Switch to `stream_text()` — that is the actual fix, not a workaround.

## Installing the `rag` extras fails on Windows

`chromadb` needs C++ build tools. Install the "Desktop development with C++"
workload from the Visual Studio Build Tools, or use WSL for lessons 04–05.
