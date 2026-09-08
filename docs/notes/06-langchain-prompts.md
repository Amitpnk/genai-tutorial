# LangChain — The Prompts Component

Video 4 of the LangChain playlist, covering the second of the six components: **Prompts**. The
topic is easy but genuinely confusing in places, so this note keeps to the video's approach — for
every class introduced, establish *why it is needed* before showing how it works.

---

## 0. Recap

| Video | Covered |
| --- | --- |
| 1 | What LangChain is and why the framework is needed |
| 2 | The six components, with real-life examples |
| 3 | Deep dive on component #1 — [Models](05-langchain-models.md) |
| **4** | **Component #2 — Prompts (this note)** |

---

## 0.5 Correction: what `temperature` actually does

A student pointed out in the comments that the previous video's explanation of `temperature` was
incomplete, and the correction is worth having up front.

The earlier framing was "0 = deterministic, 2 = creative". The **precise** property is
*reproducibility for the same input*:

| temperature | Behaviour |
| --- | --- |
| `0` | The **same input produces exactly the same output, every single run.** |
| `~0.5` | Slight variation between runs on the same input. |
| `1.5 – 2` | Substantially different, more creative output each run. |

Run "write a five-line poem on cricket" twice at `temperature=0` and you get identical text both
times. Raise it and the two runs diverge.

**How to choose:** if your application must give the same answer every time it's asked the same
thing, keep temperature near 0. If you want variety on repeated identical inputs, go towards 1.5.

---

## 1. What a prompt is

**A prompt is the message you send to an LLM.** Nothing new — every `invoke()` call in the previous
video passed a prompt; the word just wasn't used.

```python
model.invoke("Write a five-line poem on cricket")   # ← this string is the prompt
```

Prompts can be **multimodal** — an image you ask questions about, an audio clip whose singer you
want identified, a video. This note is about **text prompts**, which is 99% of the work today.

Prompts matter because **LLM output is hypersensitive to them.** Change a prompt slightly and the
output can change a lot. That sensitivity is why an entire job profile — *prompt engineering* —
grew around it, and why LangChain gives prompts a dedicated component.

---

## 2. Static vs. dynamic prompts

### The problem with how we've been writing prompts

Everything so far has looked like this:

```python
model.invoke("Write a five-line poem on cricket")
```

**Is that the right way to send a prompt?** No. In a real application, *you the programmer* don't
write the prompt — your **user** does, and you forward it to the LLM.

### A worked example: a research assistant tool

The app: a web page where a user can summarise any research paper. A text box, a Summarize button,
and the LLM's answer rendered below.

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOpenAI()

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
```

Run it with `streamlit run prompt_ui.py`. Type *"Summarize the Attention Is All You Need paper in
simple fashion"*, click Summarize, and it works. Type a different prompt for a different paper, and
that works too.

**This is a static prompt** — the user writes the entire thing, every time.

### Why static prompts are a bad idea

Handing the user the whole prompt hands them **all the control**, and LLM output is extremely
sensitive to prompt wording. Concretely:

- The user may not know the paper's exact name, types it wrong, and the LLM — which must return
  *something* — hallucinates a summary of a paper that doesn't exist.
- One user writes "in five lines", another writes "maths heavy", another "code heavy". Same tool,
  wildly different experiences.
- If your tool's selling point is that it explains papers with great analogies, you **cannot
  guarantee that** when the user supplies the whole prompt.

Ideally every user gets a **consistent experience**. That is what a dynamic prompt buys you.

### The dynamic version

Write the prompt yourself, as a template with blanks, and ask the user only to fill the blanks:

```
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with:
"Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
```

Now the UI asks for three things via dropdowns instead of one free-text box:

| Field | Options |
| --- | --- |
| `paper_input` | A fixed list of papers — **no scope for spelling mistakes** |
| `style_input` | Beginner-Friendly / Technical / Code-Oriented / Mathematical |
| `length_input` | Short / Medium / Long |

**That's a dynamic prompt:** you own the prompt's structure and quality; the user supplies only the
variables. One template covers every paper, in every style, at every length.

---

## 3. `PromptTemplate`

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""Please summarize the research paper titled "{paper_input}" with the
following specifications: ... """,
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
)

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})

result = model.invoke(prompt)
st.write(result.content)
```

### "Why not just use an f-string?"

A completely valid doubt — and yes, this whole thing works with f-strings. Three reasons to use
`PromptTemplate` anyway:

**1. Validation.** Set `validate_template=True` and LangChain checks that the placeholders in the
template and the names in `input_variables` match. Forget one, or add an extra, and you get an
error **at development time** rather than a mystery failure in production.

**2. Reusability.** A long template inline makes the surrounding code bulky, and gets worse when
several pages need the same prompt. Save it to disk instead:

```python
# prompt_generator.py — run once
template.save("template.json")
```

```python
# anywhere that needs it
from langchain_core.prompts import load_prompt
template = load_prompt("template.json")
```

The application file no longer contains the template at all. Any other file can load the same JSON.

**3. It fits the LangChain ecosystem.** This is the big one. `PromptTemplate` plugs directly into
**chains**, so the two-step "build prompt, then call model" collapses into one `invoke`:

```python
chain = template | model
result = chain.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})
st.write(result.content)
```

One `invoke` instead of two. The template forms the prompt, the prompt flows into the model, and
the result comes back — the previous stage's output becomes the next stage's input automatically.
**An f-string cannot go into a chain.** (Chains get their own video later.)

---

## 4. A console chatbot — and the context problem

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI:", result.content)
```

An infinite loop, `exit` to quit. It works — until this happens:

```
You: which one is greater, 2 or 0?
AI:  2 is greater than 0.
You: now multiply the bigger number by 10
AI:  The bigger number is x. Multiplying x by 10, we get 10x.
```

The answer should be 20. **The chatbot has no context** — it doesn't remember the previous
messages, because we never coded that.

### Fix attempt: keep a chat history

```python
chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(chat_history)      # send the whole history
    chat_history.append(result.content)
    print("AI:", result.content)

print(chat_history)
```

`invoke` is flexible enough to accept a single message *or* a list of messages. Now the same
exchange gives **20**, because the model can read what came before.

### But the history is still broken

Print it and you get a flat list of strings:

```
['hi', 'Hello! How can I assist you today?', 'which one is greater, 2 or 0?', ...]
```

**Who said what?** That information is gone. As the history grows, it gets harder for the LLM to
tell its own messages from the user's, and conversations start going wrong.

You'd want something labelled — user said this, AI said that. LangChain solved this already.

---

## 5. Messages

LangChain has **exactly three message types**:

| Message type | What it is |
| --- | --- |
| **SystemMessage** | A system-level instruction set at the very start of the conversation — *"You are a helpful assistant"*, *"You are a knowledgeable doctor, answer medical queries efficiently"* |
| **HumanMessage** | What the user sends to the LLM |
| **AIMessage** | What the LLM sends back |

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain"),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
```

The printed list now carries a labelled `SystemMessage`, `HumanMessage` and `AIMessage`, each with
its content plus metadata.

### Wiring it into the chatbot

```python
chat_history = [
    SystemMessage(content="You are a helpful AI assistant"),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(chat_history)
```

Every message is now labelled by sender. However long the conversation gets, the LLM always knows
who said what. **This is the pattern to use for any chatbot going forward.**

---

## 6. Where everything fits — the mental model

```
                          model.invoke( … )
                                 │
              ┌──────────────────┴──────────────────┐
              ▼                                     ▼
     A SINGLE MESSAGE                        A LIST OF MESSAGES
   single-turn, standalone query           multi-turn conversation
   (e.g. summarize this paper)             (e.g. a chatbot)
              │                                     │
       ┌──────┴──────┐                       ┌──────┴──────┐
       ▼             ▼                       ▼             ▼
    static       dynamic                  static       dynamic
   a plain    → PromptTemplate         SystemMessage  → ChatPromptTemplate
   string                              HumanMessage
                                       AIMessage
```

Everything so far covers three of the four boxes. The missing one — **dynamic, multi-message** — is
`ChatPromptTemplate`.

---

## 7. `ChatPromptTemplate`

Use it when you're working with a **list of messages** and need placeholders inside them. For
example, a system message whose domain isn't known ahead of time, and a human message whose topic
isn't either:

```
system: "You are a helpful {domain} expert"
human:  "Explain in simple terms, what is {topic}"
```

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}"),
])

prompt = chat_template.invoke({"domain": "cricket", "topic": "Dusra"})
print(prompt)
```

### ⚠️ The gotcha worth remembering

The intuitive version — passing `SystemMessage(content="You are a helpful {domain} expert")` —
**does not work.** It runs without error, but the placeholders come out **unfilled**, printed
literally as `{domain}` and `{topic}`.

This is genuinely inconsistent with how `PromptTemplate` behaves, and it trips people up. The
library is still maturing and has a few rough edges like this.

**The fix:** pass each message as a **tuple of `(role, template_string)`** — `("system", "...")`,
`("human", "...")` — as shown above. Those get treated as templates and interpolated properly;
message *objects* are passed through as-is.

> You'll also see `ChatPromptTemplate.from_messages([...])` in the wild. It produces the same
> result and is widely used in LangChain's own documentation, so treat both as valid — the direct
> constructor is simply what the video recommends.

`ChatPromptTemplate` does exactly what `PromptTemplate` does. The only difference:
**`PromptTemplate` for single-turn messages, `ChatPromptTemplate` for multi-turn conversations.**

---

## 8. `MessagePlaceholder`

> A `MessagePlaceholder` is a special placeholder used inside a `ChatPromptTemplate` to
> **dynamically insert chat history or a list of messages at runtime.**

### Why it exists — a customer support example

Imagine building a chatbot for an airline:

```
Day 1  User: I want to request a refund for my order #12345
       Bot:  Your refund request for order #12345 has been initiated.
             It will be processed in 3–5 business days.

       … conversation ends, history saved to a database …

Day 3  User: Where is my refund?
```

"Where is my refund?" is meaningless on its own. To answer it, the new session must **load the
previous conversation** and place it into the prompt. `MessagePlaceholder` is the slot you leave
for it.

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 1. chat template with a placeholder between the system and human messages
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}"),
])

# 2. load past conversation (from a database in reality; a text file here)
chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

# 3. build the final prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?",
})

print(prompt)
```

The final prompt is a message list in this order:

1. the system message,
2. **everything from the loaded chat history**, expanded in place,
3. today's human message.

The LLM now has full context for "Where is my refund?".

**In short:** `MessagePlaceholder` reserves a slot for a *set* of messages, and its usual job is
retrieving and inserting stored chat history.

---

## 9. What's next

Everything LangChain requires around prompts is covered. A separate **prompt engineering** playlist
is planned for the techniques themselves — few-shot templates, chain-of-thought prompting, and
general knowledge around prompting.

---

## Key takeaways

1. **`temperature=0` means reproducible, not just "boring."** The same input returns the same
   output every run — which is the property you actually want to reason about when choosing a value.
2. **A prompt is just the input to an LLM**, and LLM output is hypersensitive to it. That
   sensitivity justifies the whole component.
3. **Never let the user write the entire prompt.** Static prompts hand away control over quality,
   invite typos that cause hallucination, and make the experience inconsistent across users.
4. **Dynamic prompts = you own the template, the user fills the blanks.** Dropdowns instead of a
   free-text box eliminates a whole class of failure.
5. **`PromptTemplate` beats f-strings for three reasons:** template validation at development time,
   save/load reuse as JSON, and — most importantly — it plugs into chains.
6. **`template | model` collapses two `invoke` calls into one.** An f-string cannot do that.
7. **LLM calls are stateless, so a chatbot needs a chat history** — and that history must record
   *who said what*, or the model loses track as the conversation grows.
8. **Three message types, that's all:** `SystemMessage` (the instruction up front), `HumanMessage`
   (the user), `AIMessage` (the model).
9. **`PromptTemplate` for single-turn, `ChatPromptTemplate` for multi-turn.** Same idea, different
   shape of input.
10. **Inside `ChatPromptTemplate`, use `("system", "...")` tuples, not message objects** — objects
    skip interpolation and leave your placeholders unfilled.
11. **`MessagesPlaceholder` is how stored chat history gets back into a prompt** — the foundation of
    any chatbot that must remember a conversation from days ago.
