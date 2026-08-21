# Contributing

## Setup

```bash
make setup     # venv, editable install, nbstripout hook
make test      # offline suite, no API calls
make lint
```

## The one rule about notebooks

**Strip outputs before committing.** Notebook outputs make diffs unreadable and
occasionally leak API keys or customer data from whatever you were testing
against. `make setup` installs the `nbstripout` git hook, which handles this
automatically; `make strip` does it manually.

## Adding a lesson

1. Number it to match its place in the sequence — the filesystem order *is*
   the curriculum.
2. Open with the standard header: title, "You will be able to", prerequisites,
   estimated API cost. Learners budget both time and money.
3. Put shared code in `src/genai_tutorial/`, not in the notebook. If a cell is
   more than ~20 lines of plumbing, it belongs in the package.
4. End every exercise with a completed version in `solutions/`, same filename.
5. Add a row to the syllabus table in `README.md`.

## Writing style

Explain *why*, not only *how*. A learner can get "call this function" from the
API reference; what they cannot get there is which mistakes cost money, which
abstractions leak, and when the obvious approach is the wrong one.

Prefer showing a failure before its fix. The caching lesson demonstrates a
cache miss before explaining prefix invalidation, because the zero in the
output is what makes the rule stick.

## Tests

Tests that hit the real API are marked `@pytest.mark.live` and excluded by
default. CI runs the offline suite on every PR; the live suite runs manually.

Keep the offline suite genuinely offline — mock the client rather than skipping
the test. A test that skips without an API key silently stops protecting you.
