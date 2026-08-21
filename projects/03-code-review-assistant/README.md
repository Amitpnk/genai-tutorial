# Project 03 — Code Review Assistant

Review a diff and post findings worth reading.

**Builds on:** lessons 03 (tool use), 06 (agents), 08 (caching, cost)

## Definition of done

- [ ] Takes a git diff or PR number and produces file/line-anchored findings
- [ ] Reads surrounding context, not just the diff hunk — a change that looks
      wrong in isolation is often fine, and vice versa
- [ ] Ranks findings by severity and drops anything below a threshold
- [ ] Caches the repository context so repeated runs are cheap
- [ ] Reports cost per review

## The hard part

Signal-to-noise. An assistant that reports fifteen findings per PR, twelve of
them style nits, gets muted within a week. The engineering is mostly in what
you *suppress*: findings the linter already catches, findings about unchanged
code, and findings the model is not actually confident about.

Measure precision, not recall. Ten reviews, human-labelled: what fraction of
reported findings were worth someone's time? Below about 70%, the tool is a
net negative regardless of what it catches.

## Suggested structure

```
03-code-review-assistant/
├── README.md
├── context.py       # gather + cache repo context
├── review.py        # the review pass
├── filters.py       # severity threshold, dedupe, suppression rules
└── cli.py
```
