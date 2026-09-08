# GenAI Roadmap — The Builder vs. User Mental Model

## 1. Why this video exists

The speaker planned to make GenAI videos but found it genuinely hard to teach: the field moves so
fast that a new model, paper, tool, or term shows up almost daily, which makes designing a stable
curriculum difficult. He spent ~3 months on research, planning, and curriculum design. This video
is not just an announcement — it walks through the thought process, the mental model he built, and
the resulting two-track curriculum.

---

## 2. What Generative AI is

**Definition used in the video:** a type of AI that creates new content — text, images, music, even
code — by learning patterns from existing data, mimicking human creativity.

### Historical context

- AI research is ~60–70 years old; many techniques came and went:
  - Symbolic AI / expert systems (popular in the 1980s)
  - Fuzzy logic
  - Evolutionary algorithms
  - NLP and Computer Vision as separate fields
- **Machine Learning** turned out to be the most impactful: feed a mathematical/statistical model
  lots of data, let it extract patterns, then use it to predict on new data. Still relevant, still
  hiring.

### What classical ML was used for

| Problem type | Example |
| --- | --- |
| Regression (predict a number) | Tomorrow's stock price for a company |
| Classification (pick a category) | Is this photo a cat or a dog? |
| Ranking / recommendation | Given a product, rank the most similar products |

**What ML was *not* used for:** anything requiring human creativity. GenAI broke that assumption.
Two-to-three years ago the common line was "AI won't replace human creativity" — within two years
that statement stopped being true.

### Where GenAI sits (the nested-circles mental model)

```
AI  ⊃  Machine Learning  ⊃  Deep Learning  ⊃  Generative AI
```

- **AI** — the umbrella (symbolic AI, expert systems, fuzzy logic, …)
- **ML** — statistics- and model-based learning from data
- **DL** — neural-network-based models
- **GenAI** — emerged from DL once the **Transformer architecture** arrived

---

## 3. Four areas where GenAI has already made an impact

1. **Customer support**
   Handling customers at scale used to mean call centres full of agents — expensive. Now a chatbot
   forms the *first layer*; only unresolved queries escalate to humans. Where 10 people were
   needed, 2–3 may now suffice. This pattern is spreading across the industry.

2. **Content creation**
   Text (blogs, websites), video (YouTube), and social content all have GenAI tooling now. The
   speaker notes he can no longer reliably tell whether a Medium article was written by a human or
   an AI — the output quality is that good.

3. **Education**
   Since ChatGPT-style tools appeared, how people study has changed: planning a curriculum,
   getting unstuck, generating practice questions. It is effectively **a personal tutor available
   all the time**. Schools themselves are being forced to rethink teaching methods.

4. **Software development**
   Coding was assumed to be safely "creative + intellectual" work. But generative models are
   genuinely good at writing code — including production-ready code. Tools now let you change an
   application by writing a prompt. Where 5 programmers were needed, 2–3 may now be enough.

---

## 5. The mental model

### Step 1 — Put one term at the centre: **Foundation Models**

**What foundation models are:**

- Very large-scale AI models
- Trained on a huge amount of data (roughly "everything on the internet")
- Need enormous hardware (many GPUs) and cost crores of rupees to train
- **Key property:** they are *generalised*, not *specialised*

**Generalised vs. specialised:** a classical ML model is task-specific — a stock-price predictor
predicts stock prices, it will not also predict cricket scores. A foundation model can do many
tasks, because (a) the architecture is huge, with a very large number of parameters, and (b) it is
fed an enormous amount of data. *Analogy: a very smart person made to read a very large number of
books will naturally solve problems across several domains.*

**Example — LLMs (Large Language Models)**, the backbone of GenAI today. One LLM can do text
generation, sentiment analysis, summarisation, question answering. Training it to predict the next
word incidentally taught it all of those.

Foundation models also include **LMMs (Large Multimodal Models)** — models that work with images,
video, and audio, not just text. That is why the diagram says "Foundation Models" rather than
"LLMs" — but you can mentally substitute LLM to keep things simple.

### Step 2 — Split everything into two perspectives

```
                     +----------------------+
   USER'S            |  FOUNDATION MODELS   |            BUILDER'S
 PERSPECTIVE  <------|      (the core)      |------>   PERSPECTIVE
 use a ready-made    +----------------------+     build & deploy the
 foundation model                                  foundation model
```

**The claim:** every term, tool, and technology in GenAI belongs on one of the two sides — either
you are *using* a ready-made foundation model, or you are *building* one.

### Step 3 — Play the classification game

Whenever a new term shows up: look it up, then decide which side it belongs to.

| Term | Side | Why |
| --- | --- | --- |
| Prompt engineering | **User** | Refining the input you send to an existing LLM to get better answers |
| RLHF (Reinforcement Learning from Human Feedback) | **Builder** | Modifies/safeguards an LLM's behaviour during its creation |
| RAG (Retrieval-Augmented Generation) | **User** | Question-answering over your own private documents with an existing LLM |
| Pre-training | **Builder** | Training a foundation model on world-scale data on big hardware |
| Quantization | **Builder** | Optimising the model so it can run in different environments |
| AI agents | **User** | Software built on an LLM that also *does* things (e.g. books a ticket) |
| Vector databases | **User** | Needed when implementing RAG |
| **Fine-tuning** | **Both** | Done while building an LLM *and* while using one |

The speaker ran this game for ~6–8 months on every new term he encountered; the two curricula below
are the result.

---

## 8. Curriculum A — Builder's Perspective

*Building a foundation model and deploying it so the world can use it. More technical; closer to
what ML/DL practitioners already do.*

**Prerequisites:**
- Machine Learning fundamentals
- Deep Learning fundamentals
- A DL framework — TensorFlow or PyTorch (PyTorch preferred)

**Modules:**

1. **Transformer architecture** — every current foundation model is built on it. Encoder side,
   decoder side, embeddings, self-attention, layer normalisation, the language-modelling concept.

2. **Types of transformers** — encoder-only, decoder-only, encoder–decoder. Architectures of BERT,
   GPT, and other well-known transformers.

3. **Pre-training** — training objectives (different models use different ones), tokenization
   strategies, training strategies (local machine vs. cloud, single machine vs. distributed
   training), the challenges of training at this scale and their solutions, plus evaluation of how
   well pre-training went.

4. **Optimization** — foundation models are too large for normal hardware. Optimisations during
   training, model compression (quantization, knowledge distillation), and inference-time
   optimisation to reduce prediction latency.

5. **Fine-tuning** — adapting the generalised model to a specific task or task-type so it performs
   better there. Task-specific tuning, instruction tuning, continual pre-training (further
   pre-training in a particular domain), RLHF, and PEFT.

6. **Evaluation** — thorough evaluation across metrics before deployment. This is also what powers
   the LLM leaderboards you keep hearing about ("model X beat model Y").

7. **Deployment** — the last but essential step; an undeployed model is of no use.

> This is the pipeline a data scientist at an organisation that actually builds foundation models
> would run through.

---

## 8. Curriculum B — User's Perspective

*Using a ready-made foundation model. Less technical and, in the speaker's view, easier and more
fun than the builder side — you get to build interesting things.*

1. **Building basic LLM apps**
   - What models are available: closed-source vs. open-source
   - Closed-source → use via **API**
   - Open-source → run locally / on your server via tools like **Hugging Face** or **Ollama**
   - Frameworks like **LangChain** for building LLM-based applications

2. **Improving the LLM's response** — three techniques:
   - **Prompt engineering** — the art and science of writing prompts (a prompt = the input you send
     to a foundation model). Already a large body of work to study.
   - **RAG** — LLMs are trained on their own data and know nothing about *your* data. RAG lets you
     show an LLM your private data and do question-answering over it. A large field of study on its
     own.
   - **Fine-tuning** — also exists here, but at a shallower level than the builder-side version,
     which goes into deeper layers of the model.

3. **AI agents** — a rapidly growing field. An LLM app is usually a chatbot; an *agent* is a
   chatbot that can also perform actions for you. Example: ask for the best tourist destinations in
   India, it says Goa, and you then tell it to book a hotel — and it does. Mechanically: you give
   the LLM **tools** it can call. **Chatbot + tools = AI agent.**

4. **LLMOps** — the umbrella term for everything involved in taking an LLM-based application to
   production: deployment, evaluation, improvements, and the technical handling around it. Many
   libraries now exist to help.

5. **Miscellaneous** — multimodal foundation models (audio in, video out, etc.), diffusion-based
   models like Stable Diffusion.

---

## 9. Should you learn both sides?

**Yes — but the weighting depends on your target role.**

- **Builder side** → research scientist / data scientist work; also needs ML engineering and MLOps
  skills.
- **User side** → the speaker's view is that *anyone* with some software development background
  can do ~80–85% of this work.

The valuable profile is someone who works on the **user side but understands how foundation models
are built** — that knowledge lets you operate far better as a user. A software developer can build
an AI application today; someone who knows both sides can always command a better salary.

| Your goal | Focus |
| --- | --- |
| Research scientist | Builder side |
| App developer using LLMs | User side |
| **AI Engineer** | **Both, in parallel** |


---

## Key takeaways

1. **Foundation models are the centre of gravity** of the entire GenAI landscape.
2. **Every GenAI term is either "building a foundation model" or "using one."** Classify first,
   study second — this is the antidote to information overload.
3. **The user side is more accessible; the builder side is more differentiating.** Aim for both if
   you want to be an AI Engineer.
4. **GenAI passes every "is this technology successful?" test** — real problems, daily utility,
   economic impact, new jobs, accessibility.
5. **Do not chase every new release.** Fit each new thing into the mental model; most of it is a new
   instance of a slot you already understand.
