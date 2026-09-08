# LangChain — The Six Components


## 1. The six components

```
                         ┌──────────────┐
                         │  LangChain   │
                         └──────┬───────┘
       ┌───────────┬────────────┼────────────┬───────────┬──────────┐
       ▼           ▼            ▼            ▼           ▼          ▼
   ┌────────┐ ┌─────────┐  ┌────────┐  ┌─────────┐ ┌─────────┐ ┌────────┐
   │ MODELS │ │ PROMPTS │  │ CHAINS │  │ MEMORY  │ │ INDEXES │ │ AGENTS │
   └────────┘ └─────────┘  └────────┘  └─────────┘ └─────────┘ └────────┘
```

| # | Component | One-liner |
| --- | --- | --- |
| 1 | **Models** | A standardised interface for talking to any AI model |
| 2 | **Prompts** | Tools for building the input you send to an LLM |
| 3 | **Chains** | Pipelines — the output of one stage feeds the next automatically |
| 4 | **Memory** | Gives stateless LLM API calls a conversation history |
| 5 | **Indexes** | Connect your app to external knowledge (PDFs, sites, databases) |
| 6 | **Agents** | Chatbots with reasoning + tool access, so they can *act* |

Understand these six and you understand the majority of LangChain.

---

## 2. Models

> In LangChain, models are the **core interface through which you interact with AI models.**

That definition means little on its own, so here is the back story.

### The two old NLP problems

The most wanted NLP application has always been the **chatbot**. Building one faced two big
problems:

1. **Natural Language Understanding (NLU)** — making the bot understand what the user meant when
   they typed "Hi, can you check my email?"
2. **Context-aware text generation** — even if it understood the question, producing a reply.

Enormous effort went into both. Eventually **LLMs arrived and solved both at once**, because they
were trained on almost the entire internet: language understanding *and* context-aware generation
emerged together.

### New problem #1 — size

Training on the whole internet means **billions of parameters**, which means huge model files. Good
models on the market are **> 100 GB**. No ordinary person can run that on their computer, and even
small companies can't afford the cloud bill to host it.

**Solution: APIs.** The big providers (OpenAI, Google, Anthropic, …) host the models themselves and
expose an API. Anyone in the world can hit that API with a query; the API talks to the LLM and
returns the response. You never host the model — you pay only for the queries you send.

```
   You ──query──▶ Provider API ──▶ LLM
   You ◀─answer── Provider API ◀──┘
```

### New problem #2 — no standardisation

Every provider wrote their API differently. If your application needs two different LLMs, you write
two different styles of code. And if you built on OpenAI and later want to switch to Claude because
it's cheaper, you have to rewrite that part of the codebase. Different request shapes, different
response shapes, different parsing. **Standardisation became the challenge.**
Here are the two provider SDKs side by side — the same job, written two different ways:

```python
# OpenAI — create a human-like response to a prompt
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
```

```python
# Anthropic — claude_quickstart.py
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)

print(message.content)
```

Look at what differs: the client object (`OpenAI()` vs `anthropic.Anthropic()`), the call itself
(`client.chat.completions.create` vs `client.messages.create`), where the system instruction goes
(inside `messages` vs its own `system` argument), the shape of the message content (a plain string
vs a list of typed blocks), and how you dig the answer out (`completion.choices[0].message` vs
`message.content`). Switching providers means rewriting all of it.

**LangChain's Models component fixes exactly this.** It is an interface that lets you talk to any
provider's model in a standardised way. Switching providers is a **two-line change** — import a
different package, name a different model. The way you call it is identical, the way you print the
result is identical, and the responses come back similar enough that parsing barely changes.

```python
# Before: raw provider SDKs → two different shapes of code
# After: LangChain → same shape, swap two lines

from langchain_openai import ChatOpenAI                    # ← line 1
model = ChatOpenAI(model="gpt-4")                          # ← line 2
result = model.invoke("What is the capital of India?")
print(result.content)

from langchain_anthropic import ChatAnthropic              # ← line 1
model = ChatAnthropic(model="claude-3-5-sonnet-20241022")  # ← line 2
result = model.invoke("What is the capital of India?")
print(result.content)
```

### Two kinds of models

| | **Language models** | **Embedding models** |
| --- | --- | --- |
| Input | Text | Text |
| Output | Text | A vector |
| Philosophy | text-in → text-out | text-in → vector-out |
| Used for | Chatbots, AI agents | **Semantic search** |

Example of a language model: "How are you today?" → "I'm good, how about you?"

LangChain talks to both kinds.

### Worth exploring in the docs

- The [Chat Models](https://docs.langchain.com/oss/python/integrations/chat) page lists every provider you can talk to — ChatAnthropic, ChatMistralAI,
  AzureChatOpenAI, ChatVertexAI, ChatBedrock (AWS), ChatHuggingFace, and many more. It also shows a feature matrix per model: tool calling (needed when you build agents), structured / JSON output, local execution, multimodal input.
- The [Embedding Models](https://docs.langchain.com/oss/python/integrations/embeddings) page lists the embedding providers — OpenAI, Mistral AI, IBM, Llama, 

**In a nutshell:** Models is an interface for talking to AI models, and its main job is to
standardise a world where every LLM API sang its own tune.

---

## 3. Prompts

**A prompt is the input you send to an LLM.** When you ask ChatGPT "What is campus X?", that string is the prompt.

Prompts matter enormously, because **LLM output is extremely sensitive to them.** Change one word and the output changes a lot:

- "Explain linear regression in an **academic** tone"
- "Explain linear regression in a **fun** tone"

Same question, one word different, very different answers.

An entire field of study — **prompt engineering** — has grown around this in the last couple of
years, with real job profiles ("prompt engineer") attached, despite the mockery it gets on social
media. LangChain recognised this and built a dedicated component for handling prompts.

### What you can build with it

**a) Dynamic and Reusable prompts.** You don't know in advance what topic or tone a user will ask
for, so leave placeholders:

```
"Summarize {topic} in {emotion} tone."
```

One user fills it with *cricket / fun*, the next with *biology / serious*. Same template, reused.

In code:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template('Summarize {topic} in {emotion} tone')

print(prompt.format(topic='Cricket', emotion='fun'))
```

The two placeholders in the template — `{topic}` and `{emotion}` — are the names you pass to
`format()`. They must match: the template declares `{emotion}`, so the call passes `emotion='fun'`.
Pass a name that isn't in the template and you get a `KeyError`.

**b) Role-based prompts.** A system-level message plus a user-level message, both templated:

```
system: "Hi, you are an experienced {profession}."
user:   "Tell me about {topic}."
```

→ *experienced doctor* + *viral fever*, or *experienced engineer* + *developing bridges*. You are
guiding the LLM into a persona before it answers.

In code:

```python
from langchain_core.prompts import ChatPromptTemplate

# Define the ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Hi you are a experienced {profession}"),
    ("user", "Tell me about {topic}"),
])

# Format the prompt with the variables
formatted_messages = chat_prompt.format_messages(
    profession="Doctor",
    topic="Viral Fever",
)
```

Each message is a `(role, template)` tuple, and `format_messages()` fills every placeholder across
all of them at once, returning a list of ready-to-send messages.

> Note: the screenshot shows `ChatPromptTemplate.from_template([...])`. That won't run —
> `from_template` builds a template from a *single string*; the list-of-messages form is
> **`from_messages`**, used above.

**c) Few-shot prompts.** Show the LLM some examples first, then ask your real question. For a
customer-support classifier:

| Example ticket | Category |
| --- | --- |
| "I was charged twice for my subscription this month." | Billing Issue |
| "The app crashes every time I try to log in." | Technical Problem |
| "Can you explain how to upgrade my plan?" | General Inquiry |

You define an example template (`Ticket: … → Category: …`), hand LangChain the examples plus that
template, and it assembles a single prompt: instructions ("classify the following customer support
ticket into one of the following categories: billing issue, technical problem, general inquiry") →
all the examples → the new query, with the category left for the LLM to fill in.

The point here is not the code (that comes later in the playlist) but the range: many different
prompting techniques are implementable through this one component.

In code, it comes together in three steps:

```python
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# Step 1: the labelled examples
examples = [
    {"input": "I was charged twice for my subscription this month.", "output": "Billing Issue"},
    {"input": "The app crashes every time I try to log in.", "output": "Technical Problem"},
    {"input": "Can you explain how to upgrade my plan?", "output": "General Inquiry"},
    {"input": "I need a refund for a payment I didn't authorize.", "output": "Billing Issue"},
]

# Step 2: create an example template — the shape each example is rendered in
example_template = """
Ticket: {input}
Category: {output}
"""

# Step 3: build the few-shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template=example_template,
    ),
    prefix=(
        "Classify the following customer support tickets into one of the categories: "
        "'Billing Issue', 'Technical Problem', or 'General Inquiry'.\n\n"
    ),
    suffix="\nTicket: {user_input}\nCategory:",
    input_variables=["user_input"],
)
```

The three arguments that do the assembling: **`prefix`** is the instruction that goes on top,
**`examples` + `example_prompt`** render every example through the same template, and **`suffix`**
appends the new ticket with `Category:` left dangling for the model to complete.

Given a new ticket, the fully rendered prompt looks like this:

```text
Classify the following customer support tickets into one of the categories: 'Billing Issue',
'Technical Problem', or 'General Inquiry'.

Ticket: I was charged twice for my subscription this month.
Category: Billing Issue

Ticket: The app crashes every time I try to log in.
Category: Technical Problem

Ticket: Can you explain how to upgrade my plan?
Category: General Inquiry

Ticket: I need a refund for a payment I didn't authorize.
Category: Billing Issue

Ticket: I am unable to connect to the internet using your service.
Category:
```

The pattern is established four times over, then broken off mid-pattern — so the most natural
continuation for the model is exactly the label you want.

---

## 4. Chains

The component LangChain is *named after*.

> **Chains let you build pipelines in LangChain.**

Any LLM application can be shaped as a pipeline, and chains are how you build that pipeline.

### Worked example — English text → Hindi summary

Requirement: the user gives ~1000 words of English text; you return a Hindi summary in under 100
words.

```
   English text (1000 words)
            │
            ▼
      ┌──────────┐
      │  LLM 1   │  translate → Hindi
      └────┬─────┘
           │ Hindi text
           ▼
      ┌──────────┐
      │  LLM 2   │  summarize in < 100 words
      └────┬─────┘
           ▼
    Hindi summary (< 100 words)
```

**Without chains** you design this pipeline manually: take the input, call LLM 1, tell it to
translate, collect the Hindi output, carry it to LLM 2, ask for a summary, collect the final
output. At every stage you pull the output out by hand and feed it into the next stage's input.

**With chains** you pass the English text in, call the chain, and the whole thing executes behind
the scenes. You never worry about routing LLM 1's output into LLM 2. Chains do that heavy lifting.

### Beyond simple sequential chains

The example above is a **sequential chain** — one stage after another. Chains also compose into
more complex pipelines:

**Parallel chains.** Say the user types a topic ("9/11 incident") and you want a detailed report
combining multiple LLMs:

```
                   ┌──────► LLM 1 (report) ──────┐
   input (topic) ──┤                             ├──► LLM 3 (combine) ──► output
                   └──────► LLM 2 (report) ──────┘
```

Both LLMs work on the same input simultaneously; a third merges the two reports into the final
answer shown to the user.

**Conditional chains.** Processing branches on a condition. An AI agent that collects user feedback:

```
   user feedback ──► LLM (process / classify)
                          │
              good ───────┴─────── bad
               │                    │
               ▼                    ▼
        reply "thank you"    email the customer
                             support team
```

Plenty of other complex pipelines are possible. The chains component is beautifully designed and
removes a lot of manual work. Covered in more detail later in the playlist.

---

## 5. Indexes

> **Indexes connect your application to external knowledge** — such as PDFs, websites, and
> databases.

### The four pieces

1. **Document Loader** — bring the data in from wherever it lives
2. **Text Splitter** — break it into chunks
3. **Vector Store** — store the embeddings
4. **Retriever** — find the relevant chunks at query time

### Why you need them

ChatGPT answers most questions because it was trained on the whole internet. But it cannot answer:

- "What is the leave policy of my company XYZ?"
- "What is the notice period policy of my company XYZ?"

Those questions are about **private data it never saw during training**. This is the everyday
problem: you can't ask about the things you actually work on.

The solution: **connect an LLM to an external knowledge source** — e.g. hand it your company's rule
book. Then general questions ("Who is the Prime Minister of India?") still work from its training,
and private questions work from the attached source.

### How such a system is built

```
   Rule book PDF (1000 pages, sitting on Google Drive)
            │  ① DOCUMENT LOADER — fetch it
            ▼
   Document in memory
            │  ② TEXT SPLITTER — break into chunks
            ▼                    (by page / paragraph / chapter)
   1000 chunks
            │  ③ embedding model → 1000 embedding vectors
            ▼     stored in a VECTOR STORE (vector database)
   ┌────────────────────┐
   │   vector database  │◀────── semantic search ──────┐
   └────────────────────┘                              │
                                                       │
   user query "What is the leave policy?"              │
            │  ④ RETRIEVER — embed the query ──────────┘
            ▼
   relevant chunks + original query ──► LLM ──► answer
```

Step by step:

1. **Document loader** fetches the PDF from wherever it is stored (Google Drive, disk, a URL).
2. **Text splitter** breaks the 1000-page book into chunks so semantic search can work over it —
   split by page, and 1000 pages become 1000 chunks.
3. Each chunk is turned into an **embedding** using an embedding model, and the vectors are stored
   in a **vector store** (a vector database) so they survive between searches — you might query
   today, the day after, or ten days from now.
4. When a query arrives, the **retriever** embeds the query with an embedding model, runs a
   semantic search against the database, gets the relevant results, and hands *those results plus
   the original query* to the LLM, which replies.

**In simple terms:** indexes are how you build LLM applications that have access to an external
knowledge source. That source can be a PDF, a website, or a company database — it's fully flexible.
The playlist builds proper projects around this later, and LangChain makes it require very little
code.

---

## 6. Memory

> **LLM API calls are stateless.**

Every request is independent — the model has no memory of the previous one.

### The demonstration

```
   Request 1:  "Who is Narendra Modi?"
   Response 1: "Narendra Modi is an Indian politician who is the current
                Prime Minister of India."

   Request 2:  "How old is he?"
   Response 2: "As an AI, I don't have access to personal data about
                individuals unless it has been shared with me."
```

The second call cannot decode "he", because it never saw the first call. **And this is a big
problem** — a chatbot built on a stateless system is frustrating to talk to; you would have to
remind it of the context in every single message.

LangChain's **Memory** component solves this: it adds memory to the whole conversation.

### Types of memory

| Type | What it stores | Trade-off |
| --- | --- | --- |
| **Conversation buffer memory** (most used) | The entire chat so far, sent along with every new API call | Simple, but a long chat means a huge history and a large token bill |
| **Conversation buffer window memory** | Only the last N interactions (e.g. the last 100 messages), constantly updated | Bounded cost; older context is lost |
| **Summarizer-based memory** | A generated *summary* of the chat history so far | Much less text, so cheaper; some detail is lost |
| **Custom memory** | Very specific pieces of information — user preferences, facts and figures you always want available | For advanced use cases |

An advanced but very practical topic; discussed in detail later in the playlist.

---

## 7. Agents

The component that makes building AI agents easy — and the topic everyone has been talking about
for the last six months ("AI agents are the next big thing").

### Chatbot vs. agent

LLMs have two strengths: **NLU** and **text generation**. So the obvious first use case was the
chatbot — and people built plenty of them (ChatGPT, today's most popular AI application, is itself
a chatbot). Then came the thought: if the bot understands me and can reply, it could also *do*
things.

Example — a chatbot on a travel website:

- *"What are the best travel destinations in India in summer?"* → "Shimla, Manali" — a chatbot can
  do this, because that information was in its training data.
- *"What is the cheapest flight from Delhi to Shimla on 24 January?"* → an **agent** hits an API
  and fetches the real answer ("this IndiGo flight is the cheapest").
- *"Can you book that flight?"* → an **agent** goes and books it.

> **An AI agent is a chatbot with superpowers.** A chatbot can talk to you; an agent can also get
> work done for you.

### What an agent has that a chatbot doesn't

1. **Reasoning capability**
2. **Access to tools**

### Worked example

Give an agent two tools — a **calculator** and a **weather API** — then ask:

> "Can you multiply today's temperature of Delhi with 3?"

```
   Query: "multiply today's temperature of Delhi with 3"
            │
            ▼  ① REASONING (e.g. chain-of-thought prompting):
               break the query down step by step
               → "I need Delhi's temperature today"
               → "then I can multiply it by 3"
            │
            ▼  ② which tool gives me Delhi's temperature?
      ┌─────────────┐
      │ Weather API │  input: "Delhi"  →  25°C
      └─────┬───────┘
            │
            ▼  ③ now I need 25 × 3 — which tool does that?
      ┌─────────────┐
      │ Calculator  │  input: 25, 3, multiply  →  75
      └─────┬───────┘
            ▼
          Output: 75
```

Reasoning happens through various techniques; a very popular one is **chain-of-thought prompting**,
where the agent breaks the query down step by step and reasons through it.

**Summary:** the only difference between an agent and a chatbot is *reasoning capacity* and *access
to tools*. An AI agent is an evolved form of a chatbot that can perform actions.

All the big companies and good AI researchers seem to be converging on this topic, and a lot of
progress is expected over the next year to eighteen months. LangChain makes building agents much
easier, and the playlist builds one.

---

## 8. What's next

The next video takes the **first component — Models — in detail.** After that the playlist works
through the remaining components one by one, with real code and projects.

---

## Key takeaways

1. **Six components — Models, Prompts, Chains, Memory, Indexes, Agents.** Learn these and you have
   the majority of LangChain; the rest of the playlist is just these in depth.
2. **Models exists because of standardisation**, not because talking to an LLM is hard. Every
   provider's API sang a different tune; LangChain makes them all look the same, so switching
   providers is a two-line change.
3. **Two model families:** language models (text → text) and embedding models (text → vector, for
   semantic search).
4. **Prompts deserve a component** because LLM output is hypersensitive to input — dynamic
   templates, role-based prompts, and few-shot prompts all fall out of it.
5. **Chains = pipelines**, and their beauty is that the previous stage's output automatically
   becomes the next stage's input. Sequential, parallel, and conditional shapes are all supported.
6. **Indexes = external knowledge**, made of document loader → text splitter → vector store →
   retriever. This is how you ask an LLM about your own private data.
7. **LLM API calls are stateless**, which is fatal for a chatbot; memory (buffer / window /
   summarizer / custom) is the fix, and each variant is a cost-vs-detail trade-off.
8. **Agent = chatbot + reasoning + tools.** That's the whole difference.
