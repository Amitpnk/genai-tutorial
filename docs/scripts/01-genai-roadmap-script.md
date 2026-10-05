# Video 1 — The GenAI Roadmap | Recording Script

Companion to [`docs/notes/01-genai-roadmap-mental-model.md`](../notes/01-genai-roadmap-mental-model.md)
and the deck at [`docs/slides/01-genai-roadmap.html`](../slides/01-genai-roadmap.html).

- **Target runtime:** 27–28 minutes
- **Slides:** 25 (deck advances with `→`; press `I` for the index)
- **Pace:** ~145 words/minute. Where a timing feels tight, cut words, not the pause after a claim.
- **Delivery note:** the whole video is one argument — *every GenAI term goes on one of two sides*.
  Say the thesis at 0:40, prove it in part two, hand them the curricula in part three. Resist
  tangents; every term you are tempted to explain is a future video.

---

## Packaging

**Title (pick one):**

1. The GenAI Roadmap: How to Learn AI Without Drowning in Buzzwords
2. Every GenAI Term Fits in One of Two Boxes — Here's the Map
3. Stop Chasing AI News. Learn This One Diagram Instead.

**Thumbnail text:** `USER` | `BUILDER` with the foundation-model box between them, and a small
`YOU ARE HERE` arrow pointing at USER.

**Description:**

```
RAG, RLHF, quantization, PEFT, vector databases, LLMOps — the terms arrive flat, all at once,
with no indication of which ones are actually for you.

This video fixes the ordering problem. One diagram puts foundation models at the centre and
splits everything else into two sides: you are either USING a ready-made model or BUILDING one.
Once a term is on a side, you know whether it is your problem. By the end you have both
curricula and a habit you can run on every new word you meet.

This is video 1 of the GenAI series. Notes, slides and code are in the repo.

00:00 The terms arrive flat
00:50 Three questions this video answers
02:10 PART ONE — What generative AI is
02:25 Definition: it creates, it doesn't predict
03:20 Sixty years of AI, and what survived
04:40 What classical ML was actually for
06:00 Where GenAI sits: the nested circles
07:20 Four industries that already changed
09:10 PART TWO — The mental model
09:25 Foundation models: the four properties
10:50 Generalised vs specialised
12:20 LLM vs LMM — a note on the word
13:05 The split: user side and builder side
14:40 The classification game
16:30 PART THREE — Two curricula
16:45 Builder side: the prerequisites
17:40 Builder modules 1–4
19:10 Builder modules 5–7
20:10 User side: building basic LLM apps
21:15 Three ways to improve the response
22:30 Agents, LLMOps and the rest
23:50 Should you learn both sides?
25:10 Five takeaways
26:10 The three questions, answered
27:00 What's next in the series
```

**Tags:** generative ai roadmap, genai for beginners, foundation models, llm roadmap, ai engineer
roadmap, rag vs fine tuning, prompt engineering, langchain, ai engineer vs data scientist

**Pinned comment:** "The one-sentence version: foundation models in the middle, *using one* on the
left, *building one* on the right. Drop a term in the replies and I'll tell you which side it goes
on."

---

## Cold open — before slide 1

> [ON SCREEN: black, or a slow scroll of a GenAI news feed]

Here is a list of words: RAG. RLHF. Quantization. PEFT. Vector databases. LLMOps.

If you are learning generative AI right now, you have met all six of those in the last month, and I
would bet you cannot confidently tell me which of them you actually need.

That is not a knowledge problem. That is a sorting problem. And in the next twenty-five minutes I am
going to hand you the thing that sorts them.

---

## Slide 1 — Title · 0:00–0:50

> [ON SCREEN: slide 1, the title]

This is the GenAI roadmap.

And I want to be precise about what that word means here, because every roadmap video you have
watched is a list of topics in some order, and all of them look equally plausible, which is exactly
why none of them helped.

This is not a list. This is one diagram and one habit. The diagram puts a single term at the centre
of the entire field. The habit is what you do every time a new word shows up — which, in this field,
is roughly weekly.

The problem was never that generative AI is hard. The problem is that nobody told you what order to
learn it in.

---

## Slide 2 — You are not behind, you are unsorted · 0:50–2:10

> [ON SCREEN: slide 2, the three questions]

So let me name the actual feeling, because I think it gets misdiagnosed constantly.

You open a thread, or a newsletter, or somebody's post, and the terms arrive flat. All at the same
size. With no indication of which ones are for you. And the conclusion you draw is *I am behind.*

You are not behind. You are unsorted. Those are very different problems, and they have very
different fixes.

Here are the three questions that are really being asked when somebody says they feel behind.

**Where do I start?** Every roadmap starts somewhere different and all of them sound reasonable.

**Do I need to know this one?** This is the big one. Something like half the terms in this field
belong to people who *train* models. You may never train a model. Nobody tells you that.

**And how do I keep up?** A new model ships every week. Chasing releases is not a learning strategy,
it is a treadmill.

I am going to answer all three. Not with a reading list — with one diagram and one habit. And the
habit is the part that is still working for you a year from now.

Three parts. What generative AI actually is. The mental model. And then the two curricula that fall
out of it.

---

## Slide 3 — Part one · 2:10–2:25

> [ON SCREEN: slide 3, the part-one flood]

Part one. What generative AI is. Quickly — because I want to get to the diagram — but properly,
because the definition is doing more work than people realise.

---

## Slide 4 — Definition · 2:25–3:20

> [ON SCREEN: slide 4, the definition]

Generative AI is AI that creates new content — text, images, music, even code — by learning patterns
from existing data, mimicking human creativity.

Now, the operative word in that sentence is *new*.

Not retrieved. Not looked up. Not selected from a list of things somebody wrote earlier. Written,
for the first time, for you.

And I know that sounds like a small distinction when you have been using ChatGPT for two years and
it feels normal. So let me take it away from you for a minute, and show you what AI could do before
this — because the size of the shift is genuinely hard to see from the inside.

---

## Slide 5 — Sixty years of attempts · 3:20–4:40

> [ON SCREEN: slide 5, the history list]

AI as a research field is about sixty, sixty-five years old. And most of it did not work.

I mean that affectionately. A lot of serious techniques came and went, and each one was, at the
time, certain it was the answer.

**Symbolic AI and expert systems** — the big idea of the 1980s. You sit down with an expert, you
encode their rules by hand, and then you keep encoding, forever, because the world keeps producing
cases your rules do not cover.

**Fuzzy logic** — reasoning in degrees of truth rather than strict true and false.

**Evolutionary algorithms** — generate candidate solutions, mutate them, keep the good ones.

And **NLP and computer vision**, which — and this is easy to forget now — were two separate fields.
Different toolboxes, different conferences, different people.

One approach outlasted all of them, and it is the one you already know: machine learning. Stop
writing the rules. Feed a statistical model a large amount of data, and let it extract the patterns
itself. Then use it to make predictions on data it has never seen.

And I want to say clearly: machine learning is not history. It is still relevant and it is still
hiring. It did not get replaced. Something got added on top of it.

---

## Slide 6 — What classical ML was for · 4:40–6:00

> [ON SCREEN: slide 6, the three-problem table]

Here is what we used machine learning for. Three shapes, and almost everything fit one of them.

**Regression** — predict a number. What will this company's stock close at tomorrow?

**Classification** — pick a category. Is this photo a cat or a dog?

**Ranking and recommendation** — given this product, which products are most similar? Which is how
every e-commerce "you might also like" strip works.

Now look down the right-hand column, because this is the whole point of the slide. A number. A
label. An ordering.

That is the complete output vocabulary of classical machine learning. Ask it a question, get back a
number, a label, or a list.

Nothing on this table requires creativity. And that was not an accident — that was the accepted
boundary. The standard line, and I said it myself, was: AI will take the repetitive work, but it
will never do the creative work. That is ours.

Two to three years ago that was a safe thing to say at a conference. Within two years it stopped
being true.

---

## Slide 7 — Where GenAI sits · 6:00–7:20

> [ON SCREEN: slide 7, the nested rectangles]

So where does generative AI actually sit? Because the way it gets talked about, you would think it
arrived from somewhere else.

It did not. It is inside everything you already know, four levels down.

**Artificial intelligence** is the outer ring. The umbrella. Symbolic AI, expert systems, fuzzy
logic — all the things from two slides ago live in here.

Inside that, **machine learning**. Learn patterns from data instead of hand-writing rules.

Inside that, **deep learning** — the subset of machine learning that uses neural networks.

And inside *that*, **generative AI**.

Now, the thing I want you to take from this picture is not the ordering, it is the word *nesting*.
These are strict subsets. Which means every single thing that is true of machine learning is still
true of generative AI. The statistics did not stop applying. The data problems did not go away.
Training and evaluation did not become a different kind of activity.

If you already have ML fundamentals, you have not been made obsolete. You are standing in the outer
ring of this diagram.

And one more thing. That innermost ring did not open up because we got more data or more GPUs —
although we did. It opened up because of one specific deep-learning design: the **Transformer
architecture**. Every foundation model in use today is built on it. We will come back to it in part
three.

---

## Slide 8 — Four industries · 7:20–9:10

> [ON SCREEN: slide 8, the four panels]

Before the diagram, let me justify the time you are about to spend. Four industries that have
already changed — past tense, not "will be disrupted."

**Customer support.** Serving customers at scale used to mean a call centre full of agents, which is
expensive, and which is why support was always the first thing a company under-invested in. Now a
chatbot is the first layer, and only the queries it cannot resolve escalate to a human. Where ten
people were needed, two or three may now do. This pattern is spreading across the whole industry.

**Content creation.** Blogs, websites, video, social. And here is my honest test for this one: I can
no longer reliably tell whether an article I am reading on Medium was written by a person. I used to
be able to. The output quality is that good.

**Education.** This one is personal for a lot of you watching. Since these tools appeared, how
people study has changed — planning a curriculum, getting unstuck at one in the morning, generating
practice questions until a concept finally lands. It is effectively a personal tutor that is always
available. And schools are being forced to rethink how they teach, which is not a small thing.

**Software development.** This one was supposed to be safe. Creative work, intellectual work, on the
right side of the boundary. But models write genuinely good code, including production code, and you
can now change an application by writing a prompt. Where five programmers were needed, two or three
may do.

So: real problems, daily utility, measurable economic impact, new job titles that did not exist, and
accessible to anyone with a browser. That is every test for whether a technology is actually
successful — and it is exactly why it is worth building a durable mental model here, instead of
chasing headlines.

Which is part two.

---

## Slide 9 — Part two · 9:10–9:25

> [ON SCREEN: slide 9, the part-two flood]

Part two. The mental model.

This is the part of the video to actually pay attention to. If you take one thing away, take the
next five slides.

---

## Slide 10 — Foundation models · 9:25–10:50

> [ON SCREEN: slide 10, the four properties]

Step one. We put a single term at the centre of the entire field: **foundation models**.

Four properties. Three of them are about size and are easy. The fourth is the one that matters.

**One — very large scale.** A very large number of parameters. The architecture itself is huge.

**Two — trained on roughly everything.** The honest description is "a very large fraction of the
public internet," and at that point the difference between that and "everything" stops being
useful.

**Three — enormously expensive.** Many GPUs, and crores of rupees, to train one of these once. And
I want you to sit with that number for a second, because it has a consequence people skip: it means
very few organisations in the world build foundation models. Which means almost everybody else —
including, almost certainly, you — *uses* them. Remember that; it comes back in two slides.

**Four — and this is the one — they are generalised, not specialised.**

That is the clean break with everything in part one. Let me show you what it actually means.

---

## Slide 11 — Generalised vs specialised · 10:50–12:20

> [ON SCREEN: slide 11, the two-sided diagram]

Left side of this picture: classical machine learning. One model, one task.

You build a stock model, it predicts stock prices. You build a vision model, it tells you cat or
dog. You build a ranking model, it gives you similar products.

And these do not transfer. At all. Ask your stock-price model for a cricket score and it has nothing
to say. Not a wrong answer — no mechanism by which it could have an answer. It was built for one
job, it does that one job, and that was fine. That was the deal.

Right side: one foundation model. One LLM.

Text generation. Summarisation. Sentiment analysis. Question answering. Same model. No retraining
between them.

And here is the part that should bother you slightly, in a good way: nobody trained it to do those
four things. There was no sentiment-analysis stage. It was trained to predict the next word. That is
the whole objective. And doing that well enough, over enough text, taught it all four of those
capabilities as a side effect.

Why does that work? Two reasons, and they are both on slide ten. The architecture is enormous, and
the data is enormous.

The analogy I keep coming back to: take a very smart person and make them read a very large number
of books. You did not teach them law, or medicine, or economics specifically. But they will start
solving problems in domains you never assigned, because enough general knowledge becomes a kind of
capability on its own.

That is a foundation model.

---

## Slide 12 — LLM vs LMM · 12:20–13:05

> [ON SCREEN: slide 12, the two panels]

Quick note on vocabulary, because the diagram coming up says "foundation models" and you might
reasonably wonder why I am not just saying LLM.

An **LLM** — large language model — is text in, text out. That is the backbone of generative AI as
most people meet it, and it is what you will spend most of your time building on.

An **LMM** — large multimodal model — works with images, audio and video as well. Same idea, same
scale, wider set of inputs and outputs.

"Foundation model" is the term that covers both, which is why the diagram uses it. But if that extra
abstraction is costing you anything, mentally substitute "LLM" every time you see it. Nothing in
this roadmap breaks.

---

## Slide 13 — The split · 13:05–14:40

> [ON SCREEN: slide 13, the user/builder split]

Step two. And this is the slide. If you screenshot one frame of this video, make it this one.

Foundation models in the centre. And now we draw exactly two arrows out of it.

To the left: the **user's perspective**. Somebody else trained the model. You take it as given, and
you build on top of it.

To the right: the **builder's perspective**. You train the model and you ship it to the world so
other people can use it.

That is it. That is the whole diagram.

And here is the claim, which is a strong one, and which I am going to make anyway: **every term,
every tool, every technique in generative AI sits on one of these two sides.** Not most of them. All
of them.

Which means the question "do I need to learn this?" becomes a question you can actually answer. You
find out which side a term is on, and the side tells you whether it is your problem.

There is exactly one honest exception, and it is at the bottom of the screen: **fine-tuning**.
Fine-tuning genuinely lives on both sides. It is something you do while building a model, and it is
something you do while using one. Same word, two depths. We will unpack that in part three.

One exception out of the entire field. I will take that.

---

## Slide 14 — The classification game · 14:40–16:30

> [ON SCREEN: slide 14, the classification table]

Step three is the habit, and I call it the classification game. The rules take one sentence: a new
term shows up, you look it up, and you put it on a side.

That is it. Let me play a round so you can hear what it sounds like.

**Prompt engineering.** Refining the input you send to a model that already exists. The model is
given. User side.

**RLHF** — reinforcement learning from human feedback. It shapes and safeguards a model's behaviour
during its creation. You cannot do this unless you are making the model. Builder side.

**RAG** — retrieval-augmented generation. Question answering over *your* documents, using somebody
else's model. User side.

**Pre-training.** Training on world-scale data, on world-scale hardware. Builder side, and not
subtle.

**Quantization.** Optimising the model so it runs in constrained environments. You are modifying the
model itself. Builder side.

**AI agents.** Software on top of a model that also *does* things — books the ticket, sends the
email. The model is given; what is new is your code. User side.

**Vector databases.** You need one the moment you implement RAG, and RAG was user side. So: user
side.

And **fine-tuning**, which is the both, as promised.

Now — the table is not the lesson. I need to be really clear about that, because it is the thing
that looks most like the lesson. **The sorting is the lesson.**

I ran this game for six, eight months on every new term I came across. Looked it up, put it on a
side, moved on. And what I ended up with, without planning it, was two ordered curricula — because
when you keep sorting into two piles, eventually the piles have a structure.

Those two piles are part three. That is literally where they came from.

---

## Slide 15 — Part three · 16:30–16:45

> [ON SCREEN: slide 15, the part-three flood]

Part three. The two curricula. What each side actually asks you to learn — and, at the end, which
one you should open first.

---

## Slide 16 — Builder prerequisites · 16:45–17:40

> [ON SCREEN: slide 16, the prerequisites]

Curriculum A. The builder's perspective: build a foundation model and deploy it so the world can
use it.

This side is more technical, and it is closest to what ML and deep-learning practitioners already
do. It is also the one side of this diagram that has real prerequisites — you cannot start it in the
middle.

Machine learning fundamentals. Deep learning fundamentals. And a deep-learning framework —
TensorFlow or PyTorch, and I would say PyTorch, because that is where the ecosystem is.

If those three are missing, the seven modules I am about to list will not land. And I want to frame
that as useful information rather than discouragement — it is telling you which side of the diagram
to open first.

---

## Slide 17 — Builder modules 1–4 · 17:40–19:10

> [ON SCREEN: slide 17, modules one to four]

Seven modules, in order. Here are the first four.

**One, the Transformer architecture.** Every current foundation model is built on it, so this is not
optional on this side. Encoder side, decoder side, embeddings, self-attention, layer normalisation,
and the language-modelling concept itself.

**Two, types of transformers.** Encoder-only, decoder-only, encoder–decoder. And then the actual
architectures — BERT, GPT, and the other well-known models. Because once you know the three shapes,
every model announcement becomes readable.

**Three, pre-training.** This is the big one. Training objectives, and different models use
different ones. Tokenization strategies. Training strategies — local machine versus cloud, single
machine versus distributed. Then the problems that only appear at this scale, and their solutions.
And finally evaluating whether pre-training actually went well, which is harder than it sounds.

**Four, optimization.** Foundation models are too large for normal hardware, so this module is
unavoidable. Optimisation during training, model compression — quantization and knowledge
distillation — and then inference-time optimisation, to bring prediction latency down to something a
user will tolerate.

---

## Slide 18 — Builder modules 5–7 · 19:10–20:10

> [ON SCREEN: slide 18, modules five to seven]

And the last three.

**Five, fine-tuning.** You have a generalised model; now adapt it so it performs better on a
specific task or task-type. Task-specific tuning, instruction tuning, continual pre-training — which
is further pre-training inside a particular domain — plus RLHF and PEFT.

**Six, evaluation.** Thorough evaluation across a lot of metrics before anything ships. And here is
a thing worth knowing: this module is where the LLM leaderboards come from. Every "model X beat model
Y" headline you have seen is this step, published.

**Seven, deployment.** Last, and not optional. An undeployed model is of no use to anyone.

That is the builder curriculum. And in practice, that is the pipeline a data scientist at an
organisation that actually builds foundation models runs through — which, as we said on slide ten, is
a much smaller set of organisations than the internet implies.

---

## Slide 19 — User side, step 1 · 20:10–21:15

> [ON SCREEN: slide 19, closed vs open source]

Curriculum B. The user's perspective. And I will tell you my bias up front: this side is less
technical, and it is a lot more fun, because you get to build things that work.

Step one is building basic LLM apps, and it starts with one decision — which model, reached how.

**Closed-source models.** Somebody else hosts them. You reach them over an **API** and pay per
token. Nothing to run, nothing to size, nothing to keep alive at 3am.

**Open-source models.** You run them yourself, locally or on your own server, with tools like
**Hugging Face** or **Ollama**. More control, more privacy, and more responsibility.

Then you need a framework to hold the application together, and that is where **LangChain** comes
in — which is where the rest of this playlist lives, so if that is what you came for, that starts in
the next video.

---

## Slide 20 — Three ways to improve the response · 21:15–22:30

> [ON SCREEN: slide 20, the three techniques]

Step two. You have built something, and the responses are not good enough. There are three
techniques, and they are three of the biggest topics in this field.

**Prompt engineering.** The art and science of writing the input you send a foundation model. And I
know "just write a better prompt" sounds like it should not be a discipline, but there is already a
large body of real work here, and it is worth studying properly.

**RAG.** A model was trained on its own data and knows absolutely nothing about *yours*. Your
company's documents, your product's manual, your codebase. RAG is how you show an LLM your private
data and do question answering over it. This is an entire field on its own.

**Fine-tuning.** The same word as on the builder side, at a shallower depth. Here you are adapting a
ready-made model; over there you are reaching into the deeper layers of one you are creating.

One piece of practical advice: reach for those in that order. Prompting is cheapest, RAG is the
middle, fine-tuning is costliest. A surprising number of problems that get brought to me as
"we need to fine-tune" are prompt problems.

---

## Slide 21 — Agents, LLMOps, the rest · 22:30–23:50

> [ON SCREEN: slide 21, steps three to five]

**Step three. AI agents** — the fastest-moving thing on this list.

An LLM app is usually a chatbot: you ask, it answers. An agent is a chatbot that can also *act*.

Concretely: you ask for the best places to visit in India, it says Goa. Fine, so far that is a
chatbot. Then you say "book me a hotel there" — and it does. It actually does it.

Mechanically, what changed is not the model. You gave the model **tools** it is allowed to call.
That is the entire difference. Chatbot plus tools equals AI agent. Hold onto that, because it is the
single most confused point in this field — people attribute to the model something that is
happening in your code.

**Step four. LLMOps.** The umbrella term for taking an LLM application to production: deployment,
evaluation, monitoring, continuous improvement, and the technical handling around all of it. A
growing set of libraries exists to help.

**Step five. Miscellaneous** — and I mean that as a real category, not a dumping ground. Multimodal
foundation models: audio in, video out, and every other combination. And diffusion-based models like
Stable Diffusion, which is a different family from everything else in this video.

---

## Slide 22 — Should you learn both? · 23:50–25:10

> [ON SCREEN: slide 22, the role table]

So — the question I get every single time I draw this diagram. Do I need to learn both sides?

Yes. But the weighting depends entirely on the role you are aiming at.

If you want to be a **research scientist** — builder side. Plus ML engineering and MLOps skills.
This is data-science work, and the prerequisites from slide sixteen are real.

If you want to be an **app developer using LLMs** — user side. And here is my actual claim: anyone
with a software development background can do eighty to eighty-five percent of this work. Not
eventually. Now.

If you want to be an **AI engineer** — both, in parallel. And that is the profile that is genuinely
scarce right now.

Let me put a finer point on why. The valuable person is not the one who can train a model, and it is
not the one who can call an API. It is someone who **works on the user side but understands how
foundation models are built.**

Because a software developer can build an AI application today — that is true and it is not
impressive anymore. Someone who knows both sides can explain *why* the application behaves the way
it does. Why it hallucinated there. Why fine-tuning will not fix that. Why that latency is
structural. And that person can always command a better salary.

---

## Slide 23 — Takeaways · 25:10–26:10

> [ON SCREEN: slide 23, the five takeaways]

Five things to carry out of this, and the last one is the point.

**Foundation models are the centre of gravity** of the entire landscape. Start every explanation
there.

**Every GenAI term is either "building a foundation model" or "using one."** Classify first, study
second. That is the antidote to information overload.

**The user side is more accessible; the builder side is more differentiating.** Aim for both if you
want to be an AI engineer.

**Generative AI passes every test for a successful technology** — real problems, daily utility,
economic impact, new jobs, broad access. It is worth your time.

And: **do not chase every new release.** Fit each new thing into the model instead. Almost all of it
is a new instance of a slot you already understand.

---

## Slide 24 — The three questions, answered · 26:10–27:00

> [ON SCREEN: slide 24, the three answers]

Let me close the loop on the three questions from the beginning.

**Where do I start?** The user side — unless you already have ML and deep-learning fundamentals. It
needs no prerequisites you do not have, and you can ship something that works this week.

**Do I need to know this one?** Classify it first. If it lands on the builder side, it is not your
problem yet. And knowing that a word is somebody else's job is itself progress — that is the feeling
of being behind, going away.

**How do I keep up?** You stop trying to. You keep up with the slots, not the releases. A new model
is a new instance of something you already understand.

And notice something about all three of those answers: none of them required you to know a single
model name.

---

## Slide 25 — Close · 27:00–27:45

> [ON SCREEN: slide 25, the closing slide]

So, the one-sentence version. Foundation models at the centre. Using one on the left. Building one
on the right. Every term you meet from here goes on a side.

Classify first. Study second.

Next in this playlist we start on the user side, with LangChain — building the basic LLM app from
slide nineteen, for real, with code.

The notes for this video, these slides, and all the code are in the repo linked below.

And if you want to test whether this actually stuck: drop a GenAI term in the comments — any term,
the more obscure the better — and tell me which side you think it goes on. I will tell you if you
got it right.

See you in the next one.

> [END SCREEN: next video + playlist]

---

## Recording notes

- **Slides 7, 11 and 13 are the diagram slides.** Slow down on all three, and let each one sit on
  screen for a beat before you start talking. On slide 13, physically point left and right.
- **Slide 13 is the screenshot moment.** Say "screenshot this" out loud — it is also the best
  thumbnail frame.
- **Slide 14 is the only slide where you read a list aloud.** Keep it fast and rhythmic: term,
  side, one-line reason. If it starts to drag, cut quantization and vector databases.
- **Say "I don't know" where it is honest.** The fine-tuning-on-both-sides point is the one place
  the model gets messy, and admitting that is more convincing than papering over it.
- **B-roll worth having:** a GenAI news feed scrolling (cold open), a terminal running one API call
  (slide 19), and a leaderboard page (slide 18, on "model X beat model Y").
- **Numbers to keep accurate:** "sixty to sixty-five years" of AI, "crores of rupees" to train,
  "eighty to eighty-five percent" of user-side work. Those are the claims someone will fact-check in
  the comments.
