"""Shared helpers for the GenAI tutorial notebooks.

Lessons import from here so cells stay short and focused on the concept
being taught rather than on client boilerplate.
"""

from genai_tutorial.client import DEFAULT_MODEL, ask, get_client, stream_text, usage_line

__all__ = ["DEFAULT_MODEL", "ask", "get_client", "stream_text", "usage_line"]
