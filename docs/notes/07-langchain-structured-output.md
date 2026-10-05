# LangChain — Structured Output

## 1. What is structured output?

### Start with *unstructured* output

Talk to any LLM and the shape is always the same: you send text (the prompt), the model processes
it, and you get **text** back.

```
"What is the capital of India?"  →  LLM  →  "New Delhi is the capital of India."
```

Because the response is plain text, it has **no structure**. That's unstructured output, and it's
the default for every LLM conversation.

### Now ask for structure

Prompt: *"Can you create a one-day travel itinerary for Paris?"*

An ordinary reply is prose — "Here's a suggested itinerary: morning, visit the Eiffel Tower;
afternoon, visit a museum; evening, have dinner." Useful to read, useless to a program.

What if the model returned this instead?

```json
[
  { "time": "morning",   "activity": "Visit the Eiffel Tower" },
  { "time": "afternoon", "activity": "Visit a museum" },
  { "time": "evening",   "activity": "Have dinner" }
]
```

Same information, but now it follows a **structure** — three objects, each with the same two keys.
That's structured output.

> In LangChain, **structured output** refers to the practice of having language models return
> responses in a **well-defined data format** (for example, JSON) instead of free-form text. This
> makes the model output easier to parse and work with programmatically.

---

## 2. Why do we need it?

Three use cases — there are many more.

### a) Data extraction

You're building a job portal. Candidates upload résumés, and you want to store the useful fields in
a database: name, last company, 10th and 12th marks, college marks.

```
résumé PDF → extract text → LLM (structured output) → JSON → INSERT into database
```

Without structure you'd be regex-ing prose. With it, the LLM hands you fields you can write
straight into a table, for every candidate.

### b) Building an API

Product reviews on a site like Amazon are long and unstructured. Feed one to an LLM and pull out:

- **topics** the review discusses (battery, display, processor…)
- **pros**
- **cons**
- **overall sentiment**

Wrap that in Flask or FastAPI and you have an API anyone can call — because the output has a fixed
shape, it can be serialised, documented, and consumed.

### c) Building agents

An agent is a *chatbot with tools* — see [04-langchain-components.md](04-langchain-components.md).
Suppose your agent has a **calculator** tool and the user says:

> "Find the square root of 2"

You cannot pass that sentence to the calculator — a calculator expects **numbers**. So you run
structured output over the prompt first and extract the two pieces the tool actually needs:

```json
{ "operation": "square_root", "value": 2 }
```

*Then* the tool can run. **Every tool an agent calls needs structured input.** This is why the topic
matters so much later on.

### The one-line summary

Until now, LLMs could talk to **humans** — humans send text, the LLM sends text back, and both
understand each other. Because that output was unstructured, the LLM could **not** be connected to
other systems: databases, APIs, tools.

Structured output gives the response a data format, and with that, **LLMs can talk to machines too.**

---

## 3. Two kinds of models

| | Model **can** produce structured output | Model **cannot** |
| --- | --- | --- |
| Examples | OpenAI's GPT models — trained for it | Many smaller open-source models |
| How you get structure | **`with_structured_output()`** | **Output parsers** |
| Covered in | This note | The next video |

Both paths exist in LangChain, so you can get structured output from *any* model. This note is
almost entirely about `with_structured_output`.

---

## 4. `with_structured_output()`

The flow you already know, with **one extra call** before `invoke`:

```python
structured_model = model.with_structured_output(schema)
result = structured_model.invoke(prompt)
```

That's the only difference. The interesting part is how you define `schema`, and there are **three
ways**:

1. **TypedDict**
2. **Pydantic**
3. **JSON Schema**

---

## 5. TypedDict

### What it is

> `TypedDict` is a way to define a dictionary in Python where you specify what keys and what value
> types should exist. It helps ensure your dictionary follows a specific structure.

Normally you'd build a dictionary on the fly. The problem: on a shared codebase, another programmer
might put a string where you expected a number, and you'd only find out at runtime.

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'Nitish', 'age': 35}
print(new_person)
```

Hover over `name` in your editor and it tells you it must be a `str`. That's the benefit — the
editor communicates the intended type to whoever touches the code next.

### ⚠️ The catch: no validation

`TypedDict` only *describes*. Write `{'name': 'Nitish', 'age': '35'}` with a string age and **the
code still runs** — no error, no complaint. It tells you what the type should be; it does not
enforce it.

### Using it as a schema

The worked example for the rest of this note: send a **phone review** to the LLM, get back a
dictionary with a `summary` and a `sentiment`.

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model = ChatOpenAI()

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated...""")

print(result)
print(result['summary'])
print(result['sentiment'])
```

The result is a plain Python dictionary, so you index into it normally.

### How does it know what "summary" means?

It looks like magic — the prompt never asks for a summary or a sentiment. Behind the scenes,
`with_structured_output` **generates a system prompt** from your schema, roughly:

> You are an AI assistant that extracts structured insights from text. Given a product review,
> extract `summary` (a brief overview of the main points) and `sentiment` (overall tone of the
> review: positive, neutral, negative). Return the response in JSON format.

Your review is appended to that, the whole thing goes to the model, and since the model is trained
to return JSON, you get JSON back — which Python shows you as a dictionary.

### `Annotated` — describing each field

A single word like `summary` is usually enough, but not always. `Annotated` lets you attach a
description so the model has no room to guess:

```python
from typing import TypedDict, Annotated

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review — either negative, positive or neutral"]
```

Now both the type *and* an instruction reach the LLM.

### A fuller schema

Adding lists, optional fields, and a restricted set of values:

```python
from typing import TypedDict, Annotated, Optional, Literal

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
```

| Helper | What it does |
| --- | --- |
| `list[str]` | The field is a list of strings — multiple themes, pros, cons |
| `Optional[...]` | The field may be absent (some reviews have no cons, no reviewer name) |
| `Literal["pos", "neg"]` | The value must be one of these exact strings — useful when a database column expects `pos`/`neg` rather than "positive"/"negative" |

A practical observation from the video: `Optional` is a hint, not a guarantee. Remove the cons from
a review and the model may still invent some, because it found something negative in the text. If
you need it suppressed, say so explicitly in the annotation.

### The limitation

`TypedDict` **cannot validate**. If you declare `summary: str` there is no guarantee a string comes
back, and if you want a rule like "only return the rating when it's above 3", there's nowhere to
put it. For that you need Pydantic.

---

## 6. Pydantic

> Pydantic is a **data validation and data parsing** library for Python. It ensures that the data
> you work with is correct, structured, and type-safe.

If you've used FastAPI, you've used Pydantic — API code cares deeply about data arriving in the
right shape.

### The basics

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student = {'name': 'Nitish'}
student = Student(**new_student)
print(student)
```

Same shape as `TypedDict`, except you inherit from `BaseModel` — and now pass an `int` where a `str`
was declared and it **raises an error**: *input should be a valid string*. That validation is the
whole point.

### The features worth knowing

**Default values**

```python
class Student(BaseModel):
    name: str = 'Nitish'
```

**Optional fields** — you must supply the default explicitly:

```python
from typing import Optional

class Student(BaseModel):
    name: str = 'Nitish'
    age: Optional[int] = None
```

**Type coercion.** Pydantic is smart enough to convert when it safely can. Declare `age: int` and
pass the string `'32'` — you get back the integer `32`.

**Built-in validators**

```python
from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    email: EmailStr
```

Pass `abc` and it refuses; pass a properly formed address and the object is created.

**The `Field` function** — constraints, defaults, descriptions, even regex:

```python
from pydantic import BaseModel, Field

class Student(BaseModel):
    cgpa: float = Field(
        gt=0, lt=10,
        default=5,
        description='A decimal value representing the CGPA of the student',
    )
```

Pass `12` and it errors on the constraint. Pass `5` and it's fine. The `description` does the same
job here that `Annotated` did for `TypedDict` — it reaches the LLM and guides it.

**Converting the result.** The object you get is a Pydantic object, but it converts:

```python
student_dict = student.model_dump()   # → Python dictionary
student_json = student.model_dump_json()  # → JSON string
```

> Older tutorials use `.dict()` and `.json()`. Those are deprecated — Pydantic v2 wants
> `model_dump()` and `model_dump_json()`.

### The review schema in Pydantic

Same fields as before, expressed the Pydantic way:

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal

class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model = model.with_structured_output(Review)
result = structured_model.invoke(review_text)
```

**One gotcha:** the result is a **Pydantic object**, not a dictionary. `result['name']` fails —
use attribute access, `result.name`, or convert first with `model_dump()`.

---

## 7. JSON Schema

Use this when your project **isn't only Python**. A Python backend with a JavaScript frontend both
needing the same schema can't share a `TypedDict` or a Pydantic model — but JSON is a universal
format that any language understands.

A schema has five parts:

| Key | Purpose |
| --- | --- |
| `title` | Name of the schema |
| `description` | Optional, but useful here — it reaches the LLM |
| `type` | The overall data type; a dictionary-shaped schema is an `object` |
| `properties` | Every attribute and its type |
| `required` | Which attributes must be present (the inverse of `Optional`) |

A minimal one:

```json
{
  "title": "Student",
  "description": "Schema about students",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" }
  },
  "required": ["name"]
}
```

For the review, the mapping from the Python versions is direct:

| Python | JSON Schema |
| --- | --- |
| `list[str]` | `"type": "array"` with `"items": {"type": "string"}` |
| `Optional[list[str]]` | `"type": ["array", "null"]` |
| `Literal["pos", "neg"]` | `"enum": ["pos", "neg"]` |
| `Annotated` / `Field(description=…)` | `"description"` inside the property |

Pass the schema dictionary straight in:

```python
structured_model = model.with_structured_output(json_schema)
```

Like `TypedDict`, the result comes back as a **Python dictionary**.

---

## 8. Which one should you use?

| | TypedDict | Pydantic | JSON Schema |
| --- | --- | --- | --- |
| Type hints for the editor | ✅ | ✅ | ✅ |
| **Data validation** | ❌ | ✅ | ✅ |
| Default values | ❌ | ✅ | ❌ |
| Automatic type conversion | ❌ | ✅ | ❌ |
| Cross-language compatibility | ❌ | ❌ | ✅ |
| Returns | dictionary | Pydantic object | dictionary |

- **TypedDict** — pure Python, you only need type hints, no validation required. Rare in real
  projects.
- **Pydantic** — you need validation, defaults, or type coercion. **This is the default choice**,
  and what the playlist uses from here on.
- **JSON Schema** — the schema must be shared across languages, or you don't want extra Python
  dependencies.

---

## 9. The `method` parameter

`with_structured_output` takes a `method` argument with two possible values:

| `method` | When to use |
| --- | --- |
| `"json_mode"` | You want the structured output as JSON — true most of the time. Use with Claude, Gemini and similar models |
| `"function_calling"` | The structured output exists so you can call a **function/tool** with it — the agent case. The default for OpenAI models |

Rule of thumb: OpenAI models → function calling (already the default); other providers → JSON mode.

---

## 10. When the model supports neither

Some models can't do structured output at all. Take the TinyLlama open-source model from the
[models note](05-langchain-models.md) — swap `ChatOpenAI` for `ChatHuggingFace` with that model,
call `with_structured_output`, and the code **throws an error**. Neither JSON mode nor function
calling is available for it.

For those models you apply **output parsers** yourself — the subject of the next video.

---

## Key takeaways

1. **Unstructured output is the default.** Text in, text out — readable by humans, unusable by
   programs.
2. **Structured output = a well-defined data format**, usually JSON, which makes the response
   parseable programmatically.
3. **The real unlock is machine-to-machine.** LLMs could always talk to humans; structure is what
   lets them talk to databases, APIs and tools.
4. **Every agent tool needs structured input** — a calculator takes numbers, not the sentence "find
   the square root of 2". Remember this when agents arrive.
5. **`with_structured_output(schema)` is one extra call** before `invoke`. That's the whole API.
6. **It works by generating a system prompt from your schema** behind the scenes — that's why the
   model knows what `summary` means without you asking.
7. **Three ways to declare a schema:** TypedDict, Pydantic, JSON Schema.
8. **TypedDict describes but never enforces.** Declaring `age: int` and passing `"35"` runs fine.
9. **Pydantic validates** — constraints, defaults, optional fields, type coercion, `EmailStr`,
   `Field(...)`. Use it unless you have a reason not to.
10. **Mind the return type:** TypedDict and JSON Schema give you a dictionary (`result['name']`);
    Pydantic gives you an object (`result.name`).
11. **JSON Schema is for crossing language boundaries** — a Python backend and a JS frontend sharing
    one schema.
12. **Not every model can do this.** When it can't, output parsers take over — next video.
