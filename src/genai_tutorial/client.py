"""A single configured Anthropic client, shared by every lesson.

Why this file exists: without it, each notebook repeats key loading, model
selection, and error handling. Keeping it here means a lesson cell shows the
one idea it is teaching.
"""

from __future__ import annotations

import os
from typing import Any, Iterator

import anthropic
from dotenv import load_dotenv

load_dotenv()

# Claude Opus 5 is the default across the tutorial. Override per-run with
# GENAI_TUTORIAL_MODEL=claude-haiku-4-5 while iterating to keep costs down.
DEFAULT_MODEL = os.getenv("GENAI_TUTORIAL_MODEL", "claude-opus-5")

# Non-streaming default. Streaming calls raise this (see stream_text) because
# HTTP timeouts stop being the binding constraint once you stream.
DEFAULT_MAX_TOKENS = 16_000

_client: anthropic.Anthropic | None = None


def get_client() -> anthropic.Anthropic:
    """Return a lazily-created, process-wide client.

    Credentials resolve from the environment (ANTHROPIC_API_KEY, or an
    `ant auth login` profile) — we never take a key as an argument, so no
    lesson can accidentally hardcode one.
    """
    global _client
    if _client is None:
        if not os.getenv("ANTHROPIC_API_KEY") and not os.getenv("ANTHROPIC_AUTH_TOKEN"):
            # Not fatal: an `ant auth login` profile also works. Warn, don't block.
            print("No ANTHROPIC_API_KEY found in the environment. See docs/setup.md.")
        _client = anthropic.Anthropic()
    return _client


def ask(
    prompt: str,
    *,
    system: str | None = None,
    model: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    effort: str = "high",
    **kwargs: Any,
) -> str:
    """Send one prompt, return the text of the reply.

    The simplest possible call — lesson 01 starts here. Thinking is adaptive by
    default on Claude Opus 5, so we do not pass a `thinking` parameter.
    """
    params: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "output_config": {"effort": effort},
        "messages": [{"role": "user", "content": prompt}],
    }
    if system is not None:
        params["system"] = system
    params.update(kwargs)

    response = get_client().messages.create(**params)
    return "".join(block.text for block in response.content if block.type == "text")


def stream_text(
    prompt: str,
    *,
    system: str | None = None,
    model: str = DEFAULT_MODEL,
    max_tokens: int = 64_000,
    **kwargs: Any,
) -> Iterator[str]:
    """Yield response text as it arrives.

    Use this for anything long — it is what keeps a chat UI responsive, and it
    sidesteps HTTP timeouts on large max_tokens values.
    """
    params: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system is not None:
        params["system"] = system
    params.update(kwargs)

    with get_client().messages.stream(**params) as stream:
        yield from stream.text_stream


def usage_line(response: Any) -> str:
    """One-line token accounting, printed after calls in the cost lessons.

    Cache columns are the ones to watch in lesson 08: if `cache_read` stays at 0
    across repeated calls with the same prefix, something is invalidating it.
    """
    u = response.usage
    return (
        f"in={u.input_tokens} out={u.output_tokens} "
        f"cache_write={getattr(u, 'cache_creation_input_tokens', 0)} "
        f"cache_read={getattr(u, 'cache_read_input_tokens', 0)}"
    )
