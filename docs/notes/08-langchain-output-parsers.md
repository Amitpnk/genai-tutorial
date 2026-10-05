# LangChain — Output Parsers

Video 6 of the LangChain playlist, and a direct sequel to
[07-langchain-structured-output.md](07-langchain-structured-output.md). Read that one first — this
note assumes it.

---

## 0. Recap

An LLM's reply is **text**, and text is unstructured — which is why you can't hand it straight to a
database or an API. **Structured output** forces the model to reply in a defined format (JSON, say),
and once it does, the LLM can talk to other systems.

There are two kinds of models:

| | **Can** give structured output | **Cannot** |
| --- | --- | --- |
| What they are | Fine-tuned for it — OpenAI's GPT models | Most open-source models |
| The tool | `with_structured_output()` — covered last video | **Output parsers** — this video |

---

## 1. What are output parsers?

> Output parsers in LangChain help convert raw LLM responses into structured formats like JSON, CSV,
> Pydantic models and more. They ensure consistency, validation, and ease of use in applications.

They're classes shipped with LangChain that let you derive structured output from **any** model.

**Important — don't get confused here:** output parsers work with *both* kinds of model. Use them
with an open-source model that can't do structured output natively, and use them with a GPT model
that can. This note shows both.

### The four we'll cover

LangChain ships many parsers; four cover most real use cases:

1. **StrOutputParser**
2. **JsonOutputParser**
3. **StructuredOutputParser**
4. **PydanticOutputParser**

---

## 2. StrOutputParser

The simplest one. It takes the LLM response and gives you back a **string**. That's all it does.

### Why bother?

You already know that a chat model returns more than text — it returns a message object carrying
metadata (token usage, completion tokens, and so on), which is why you always write
`result.content`. So if `result.content` works, what's the parser for?

**The answer is chains.** Here's the use case that makes it obvious:

```
topic ──▶ LLM ──▶ detailed report ──▶ LLM ──▶ 5-line summary
```

Two calls to the same model: first write a detailed report on a topic, then summarise that report in
five lines.

### Without the parser

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic'],
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text'],
)

prompt1 = template1.invoke({'topic': 'black hole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})
result1 = model.invoke(prompt2)

print(result1.content)
```

It works — but notice how much manual wiring there is: invoke, extract `.content`, build the next
prompt, invoke again, extract again.

### With the parser

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})
print(result)
```

One pipeline, one `invoke`. Reading the chain left to right: template1 builds the prompt → the model
answers → **the parser pulls the text out of all that metadata** → template2 takes that text →
the model answers again → the parser extracts the final string.

**That middle parser is the point.** Without it you couldn't form a single chain — you'd have to
break out of the pipeline to extract `result.content` and start a second chain. The parser lets the
text flow straight into the next stage.

> Chains get a dedicated video later. For now, the `|` syntax is enough: each stage's output becomes
> the next stage's input.

### A practical note on free APIs

The video first writes this against Hugging Face's inference API with TinyLlama and hits a
`ReadTimeout` — the free API simply doesn't respond. That's the reality of free tiers: **not
reliable.** Swapping in `ChatOpenAI` makes it run; later, a different Hugging Face model
(a Gemma-based one) works fine too.

The code itself is model-agnostic. If TinyLlama times out for you, try another model rather than
assuming the code is wrong.

---

## 3. JsonOutputParser

Forces the model to reply in JSON. The quickest possible way to get JSON out of an LLM.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()},
)

prompt = template.format()
result = model.invoke(prompt)
final_result = parser.parse(result.content)

print(final_result)
print(type(final_result))   # <class 'dict'>
```

### The two new ideas

**`get_format_instructions()`** — the parser tells you what to say to the LLM. Print the prompt and
you'll see your own text, then a line the parser appended: *"Return a JSON object."* You could have
written that yourself, but every parser from here on uses this same pattern, so it's worth learning
once.

**`partial_variables`** — `format_instruction` isn't filled at runtime by the user; it's filled
*before* runtime by that function call. That's what makes it a *partial* variable rather than an
input variable.

### The chain version

```python
chain = template | model | parser
result = chain.invoke({})
print(result)
```

`parse()` is called for you behind the scenes. Note the **empty dictionary** — `invoke` always
expects one, even when the template has no input variables. Omit it and you get a
`missing 1 required positional argument` error.

### ⚠️ The limitation: no schema enforcement

You get JSON, but you **cannot dictate its shape.** Ask for five facts about black holes and the
model might return one key holding a list:

```json
{ "facts_about_black_holes": ["...", "...", "..."] }
```

...when you wanted:

```json
{ "fact_1": "...", "fact_2": "...", "fact_3": "..." }
```

You can hint at the structure in the prompt, but there's no guarantee. **JsonOutputParser does not
enforce a schema** — which is exactly what the next parser fixes.

---

## 4. StructuredOutputParser

Extracts structured JSON from LLM responses **based on predefined field schemas**. Same as
`JsonOutputParser`, except you now declare the shape up front and the model follows it.

```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({'topic': 'black hole'})
print(result)
```

Now the output has `fact_1`, `fact_2` and `fact_3` as separate keys — the schema is enforced.

### Note the import

`StructuredOutputParser` comes from **`langchain.output_parsers`**, not `langchain_core`. Every
other parser here lives in core. Why the difference?

- **`langchain`** is the umbrella library — everything lives under it.
- **`langchain_core`** holds the most important, most reusable components.

`StructuredOutputParser` wasn't deemed as broadly reusable as `JsonOutputParser`, so it stayed in the
main library. Worth remembering when an import fails.

### ⚠️ The limitation: no data validation

You can dictate the *structure*, but not the *types*. Ask for a person's name, age and city
expecting age to be an integer, and the model may return `"35 years"` — a string. Nothing stops it.
You either accept it or clean it up manually afterwards.

Which brings us to the last parser.

---

## 5. PydanticOutputParser

> A structured output parser in LangChain that uses **Pydantic models** to enforce schema validation
> when processing LLM responses.

Because the schema is a Pydantic object, you get schema enforcement **and** validation.

| Core feature | What it buys you |
| --- | --- |
| Strict schema enforcement | Declare data types and constraints, and they're followed |
| Type safety | Slightly wrong types get coerced |
| Easy validation | Constraints like "age must be over 18" are checked |
| Seamless integration | Plugs into chains like everything else |

```python
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()},
)

chain = template | model | parser
final_result = chain.invoke({'place': 'sri lankan'})
print(final_result)
```

### What actually gets sent

Print the prompt and you'll see your own instruction, followed by a substantial block the parser
generated: an explanation that the output must be a JSON instance conforming to a given JSON schema,
an example, and then the schema derived from your Pydantic class — including which fields are
required. That block is why the model complies.

---

## 6. The four, side by side

| Parser | Gives you | Enforces schema? | Validates data? |
| --- | --- | --- | --- |
| **StrOutputParser** | A plain string | — | — |
| **JsonOutputParser** | JSON (a dict) | ❌ | ❌ |
| **StructuredOutputParser** | JSON in *your* shape | ✅ | ❌ |
| **PydanticOutputParser** | A validated Pydantic object | ✅ | ✅ |

- **StrOutputParser** — when you want the text out, and especially inside chains.
- **JsonOutputParser** — when you just need JSON and don't care about its exact shape.
- **StructuredOutputParser** — when the shape matters.
- **PydanticOutputParser** — when the shape *and* the values matter.

And the point worth repeating: **all four work with any LLM** — OpenAI, Claude, Gemini, or an
open-source model from Hugging Face.

---

## 7. There are more

`langchain.output_parsers` contains plenty of others worth browsing in the docs:

- `CommaSeparatedListOutputParser`, `ListOutputParser`, `NumberedListOutputParser`
- `MarkdownListOutputParser`, `XMLOutputParser`
- `EnumOutputParser`, `DatetimeOutputParser`
- `OutputFixingParser` — for retrying when the response doesn't come back right the first time

The goal here wasn't to cover every parser but to establish the pattern. With these four understood,
the rest are readable from the documentation.

---

## Key takeaways

1. **Output parsers turn raw LLM text into structured formats** — and unlike
   `with_structured_output`, they work with models that have no native structured-output support.
2. **They work with *both* kinds of model.** Not a fallback only for weak models.
3. **StrOutputParser exists for chains.** `result.content` does the same job in isolation; the
   parser is what lets text flow from one stage of a pipeline into the next.
4. **`template | model | parser` is the shape** you'll write from here on — one `invoke`, no manual
   extraction.
5. **`get_format_instructions()` is the common pattern.** The parser writes the instruction that
   tells the LLM what format to return, and you slot it into the prompt.
6. **`partial_variables` vs `input_variables`:** partials are filled before runtime (by the parser),
   inputs are filled at runtime (by the user).
7. **`chain.invoke({})` needs the empty dict** even when the template takes no variables.
8. **The four parsers form a ladder:** string → JSON → JSON with a schema → JSON with a schema *and*
   validation. Pick the lowest rung that meets your need.
9. **`StructuredOutputParser` imports from `langchain`, not `langchain_core`** — core holds only the
   most reusable components.
10. **Free inference APIs are unreliable.** A `ReadTimeout` from Hugging Face usually means the API,
    not your code — swap the model and try again.
