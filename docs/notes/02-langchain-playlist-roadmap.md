# LangChain Playlist — Roadmap and Curriculum

## 1. Where this sits in the bigger picture

This is the **first playlist** of the end-to-end Generative AI roadmap — the first concrete step
after the curriculum-planning video.

### Quick recap of the previous video

All of Generative AI splits into two sides:

- **Builder's side** — developing foundation models (transformer architecture, types of
  transformers, pre-training, fine-tuning, optimization)
- **User's side** — using ready-made foundation models to build applications

The user-side curriculum was:

1. How to build LLM-based applications
2. Three ways to improve the response coming out of an LLM — **prompt engineering**, **RAG**,
   **fine-tuning**
3. **Agentic AI** — a completely new field emerging out of all this
4. **LLMOps**
5. Miscellaneous topics

**This playlist covers item 1** — building LLM applications, using LangChain. It is the starting
point (the "origin") of the user side of the GenAI curriculum. The remaining topics get covered
gradually afterwards.

---

## 2. What is LangChain?

In the simplest terms: **a framework for building any LLM-based application** — chatbots, agents,
and so on.

**Formal definition used in the video:**

> LangChain is an open-source framework that helps in building LLM-based applications. It provides
> modular components and end-to-end tools that help developers build complex AI applications such
> as chatbots, question-answering systems, RAG-based applications, autonomous agents, and much more.

### Why LangChain became so popular — five core features

1. **Supports almost all major LLMs**
   Open-source or closed-source, it doesn't matter — an integration exists for each. OpenAI's GPT
   models, Anthropic's Claude models, Google's models, and the rest.

2. **Simplifies developing LLM-based applications**
   It ships concepts — most notably **chains** — that let you assemble complex applications out of
   simpler pieces without wiring everything by hand.

3. **Many integrations available**
   Building an LLM app means connecting to lots of other things: your database, a remote data
   source, deployment targets. LangChain provides wrappers for these tools and services, so you
   don't write much boilerplate.

4. **Free and open source**
   A major driver of adoption. It's actively developed — **three different versions shipped within
   one-to-two years**, and new components get added on an almost daily basis.

5. **Supports all major GenAI use cases**
   Chatbots, agents, RAG-based applications — it's an all-rounder.

---

## 3. Why LangChain first?

Because it gives you a **holistic view** of the whole user-side landscape early. Learning LangChain
first means you get a flavour of nearly everything else on the list:

| Topic | How LangChain exposes you to it |
| --- | --- |
| Open-source **and** closed-source LLMs | Work with both from the same framework |
| LLM APIs | Direct API integrations |
| Hugging Face | Integration available |
| Ollama | Integration available |
| Prompt engineering | You get a working flavour of it while building |
| RAG | You can develop RAG applications directly |
| AI agents | You can build them directly |
| LLMOps | A partial flavour, shown along the way |

**The plan:** take the holistic view first via LangChain, then revisit each topic in depth in its
own dedicated playlist afterwards —

- A complete playlist on **prompt engineering**
- Later, a complete playlist on **RAG and advanced RAG techniques**

---

## 4. Playlist curriculum

The playlist is mentally divided into **three parts**. Roughly **17 videos** total (a couple more
may get added over time).

### Part 1 — Fundamentals (the most important part; nothing later makes sense without it)

1. **What is LangChain** — detailed overview, technical aspects, and most importantly *why*
   LangChain is needed at all
2. **Components of LangChain** — overview video discussing every component in detail
3. **Models** — from here onwards it gets practical. All the model types available in LangChain,
   how to integrate with them, how to get responses back
4. **Prompts** — different prompting techniques within LangChain
5. **Output parsing** — the various ways to parse what comes out of an LLM
6. **Runnables and LCEL** (LangChain Expression Language) — a technical aspect of the framework
7. **Chains** — an important one; the concept mentioned earlier
8. **Memory** — how to integrate the memory concept into chatbots and similar apps

### Part 2 — RAG

9. Document loaders
10. Text splitters
11. Embeddings
12. Vector databases
13. Retrievers
14. **Build a RAG application from scratch**

### Part 3 — AI Agents

15. Tools and toolkits
16. Tool calling
17. **Build an AI agent**

---

## 5. Focus areas for the playlist

1. **Most up-to-date information**
   LangChain's site currently shows three versions (0.1, 0.2, 0.3), and the three are quite
   different from each other — learn 0.1 and parts of 0.3 may not make sense. The entire playlist
   will be based on the **latest version (0.3)**, with some guidance about 0.1 and 0.2 along the
   way.

2. **Clarity**
   A lot of existing LangChain content lets you code along and get a working application without
   ever understanding *how it works behind the scenes*. This playlist targets that conceptual
   clarity instead — so videos will be detailed, likely **30–40 minutes each** despite there being
   17 of them.

3. **Conceptual understanding**
   LangChain is a practical framework, but it has real concepts inside it — runnables, chains, and
   so on. Understanding those means that when version 0.4 eventually replaces 0.3, learning it
   won't be painful.

4. **Cover ~80% of LangChain, not 100%**
   Not all of it is useful. The playlist targets the most useful 80%. If other parts become
   important later, the playlist gets updated.

---

## Key takeaways

1. **LangChain is the entry point to the user side of GenAI** — not because it's the only tool, but
   because it touches every other topic on the list at least a little.
2. **Chains are the central idea** for composing complex applications out of simple parts.
3. **Version matters** — 0.1, 0.2, and 0.3 differ significantly; learn against 0.3.
4. **Aim for concepts, not copy-paste** — runnables and chains are what carry across framework
   versions.
5. **Three parts:** Fundamentals → RAG → Agents, with a build-from-scratch project ending each of
   the last two.
