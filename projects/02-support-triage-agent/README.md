# Project 02 — Support Triage Agent

Classify incoming support tickets, enrich them with account context, and route
them — with a decision trail a human can audit.

**Builds on:** lessons 02 (structured output), 03 (tool use), 06 (agents)

## Definition of done

- [ ] Returns a validated structured verdict: category, severity, owning team,
      and a confidence score
- [ ] Calls at least two tools (account lookup, similar-ticket search)
- [ ] Escalates to a human when confidence is low, rather than guessing
- [ ] Logs every tool call and the reasoning behind the final routing
- [ ] Measured against 30 labelled tickets, with a confusion matrix

## The hard part

Auditability. When triage routes a ticket wrongly, someone has to be able to
answer *why* — which tools were called, what they returned, what tipped the
decision. Design the log format before you write the agent; retrofitting it is
much worse.

Also worth deciding early: is this actually an agent, or a workflow with two
lookups? Lesson 06's four questions apply. If a fixed sequence works, use it.

## Suggested structure

```
02-support-triage-agent/
├── README.md
├── schema.py        # the Pydantic verdict model
├── tools.py         # account lookup, similar-ticket search
├── triage.py        # the loop, with logging
└── evals/tickets.jsonl
```
