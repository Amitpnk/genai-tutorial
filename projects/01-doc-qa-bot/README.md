# Project 01 — Document Q&A Bot

Answer questions over a document set you supply, with citations, and refuse
when the answer is not in the corpus.

**Builds on:** lessons 04 (chunking, embeddings), 05 (RAG), 07 (evaluation)

## Definition of done

- [ ] Ingests a directory of PDFs or markdown files into a persisted index
- [ ] Answers with inline citations pointing at source and location
- [ ] Says "not covered by these documents" rather than improvising — verified
      by at least five deliberately out-of-corpus eval cases
- [ ] A 20-case eval suite runs in under a minute with a scored report
- [ ] Reports token cost per question

## The hard part

Refusal. A system that answers everything scores well on the questions you
thought to test and fails silently on the ones you did not. Build the
out-of-corpus cases *first*, before the happy path — otherwise you will tune
the system to be confident and only discover the cost later.

## Suggested structure

```
01-doc-qa-bot/
├── README.md
├── ingest.py        # directory -> chunks -> index
├── answer.py        # question -> (answer, citations)
├── evals/cases.yaml
└── app.py           # CLI or minimal web UI
```
