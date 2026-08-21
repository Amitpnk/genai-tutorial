# Glossary

Terms in the order you meet them, not alphabetical — read it top to bottom the
first time.

**Token** — The unit models read and bill in. Roughly ¾ of an English word.
Both input and output are billed, at different rates.

**Context window** — How many tokens a model can consider at once, input and
output together. Current Claude models hold 1M tokens; running out is a design
problem, not a hardware one.

**System prompt** — Instructions that apply for the whole conversation: role,
constraints, tone. Distinct from the user turn, which carries the request.

**Content block** — A response is a *list* of typed blocks (`text`,
`thinking`, `tool_use`), not a string. Check `block.type` before reading it.

**Effort** — A request parameter (`low` → `max`) trading cost against depth of
reasoning. Lower effort means fewer tokens and faster answers.

**Adaptive thinking** — The model decides for itself how much to reason before
answering. On by default on Claude Opus 5. It replaces the older fixed
"thinking budget" idea.

**Structured output** — Constraining the response to a schema so it parses
reliably, rather than asking for JSON in the prompt and hoping.

**Tool / function calling** — Giving the model callable functions. The model
returns a `tool_use` block; *your* code runs the function and returns a
`tool_result`. The model never executes anything itself.

**Agentic loop** — Repeating call → tool → result → call until the model stops
requesting tools. Bound it, or it will not bound itself.

**Embedding** — A vector representation of text where distance approximates
semantic similarity. "Approximates" is load-bearing.

**Chunk** — A slice of a document sized for retrieval. Chunk badly and no
amount of model quality rescues you.

**RAG** — Retrieval-Augmented Generation: fetch relevant text, put it in the
prompt, answer from it. Most "the model hallucinated" complaints in a RAG
system are actually retrieval failures.

**Grounding** — Requiring answers to come from provided context, including the
option to say the context does not cover the question.

**Prompt caching** — Reusing the computation for a repeated prompt *prefix*.
Any byte change in the prefix invalidates everything after it.

**Eval** — A repeatable scored test set. The difference between "this prompt
feels better" and knowing.

**LLM-as-judge** — Using a model to score another model's output. Useful for
open-ended text, but it has its own biases and variance — validate it against
human labels before trusting it.

**Streaming** — Receiving the response incrementally. Better perceived latency,
and it avoids HTTP timeouts on long generations.

**Workflow vs. agent** — A workflow has control flow you wrote; an agent has
control flow the model chooses. Most production systems should be workflows.
