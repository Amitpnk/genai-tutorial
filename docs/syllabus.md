# Syllabus to be Covered

Consolidated syllabus extracted from the two DV Analytics brochures:

| Source PDF | Program(s) |
| --- | --- |
| `docs/slides/AI Forward Deployment Engineer Brochure for DV (1).pdf` | Master AI Forward Deployment Engineer (FDE) |
| `docs/slides/APIDS_APIDA_BROCHURE.pdf` | APIDS — Advanced Program in Industrial Data Science<br>APIDA — Advanced Program in Industrial Data Analytics |

---

## Part 1 — Master AI Forward Deployment Engineer (FDE)

**Positioning:** A zero-to-FDE program. Full technical foundation (Python, ML, Deep Learning,
Transformers, GenAI, Agentic AI, Cloud, DevOps), but the focus is the FDE job itself —
understanding the client, translating the problem, building fast, and shipping a live solution.

**The FDE balance the course is weighted around:**

- 20% AI Expert — enough AI depth to pick and apply the right approach
- 30% Engineer — build, integrate, deploy, and keep it running
- 50% Problem-Solver + Communicator + Shipper — understand the client, translate the problem, present and deliver

**Structure:** 5 parts, 22 modules.

### Prologue — What is a Forward Deployed Engineer?

- Hybrid engineer + consultant who builds and ships a working solution inside the client's real environment
- Intersection of three worlds: Engineering (code, integrate, deploy, debug live), Consulting (stakeholders, requirements, expectations), AI (LLMs, RAG, agents)
- Core difference: a SWE builds a product for many users; an FDE builds a solution for one client, tuned to that client's data, constraints, and goals

---

### PART A — The FDE Core (the real job, starts Day 1)

#### Module 1 — The FDE Role & Mindset (6 lessons)

1. 1.1 What is an FDE? — the intersection of engineering, consulting, and AI
2. 1.2 FDE vs SWE — FDEs build for clients, SWEs build products
3. 1.3 The FDE Mindset — Speed > Perfection; Empathy > Assumptions; Ship it
4. 1.4 The 20/30/50 FDE — why 50% of the job is problem-solving & delivery, not code
5. 1.5 FDE Skillset — AI + Data + Cloud + SE + Consulting = the pillars
6. 1.6 The 7-Stage FDE Playbook — Discover → Translate → Design → Prototype → Deploy → Operate → Deliver

#### Module 2 — Problem Discovery & Translation (8 lessons)

> The single highest-value FDE skill — taught early, before any AI.

1. 2.1 The Real Problem vs the Stated Problem — why clients describe symptoms, not causes
2. 2.2 Stakeholder Discovery — who to talk to, what to ask, how to listen
3. 2.3 Requirements Gathering Techniques — interviews, shadowing, workflow mapping
4. 2.4 The Problem Translation Framework — business pain → technical problem statement
5. 2.5 Choosing the Right Approach — Rules vs ML vs RAG vs Agents vs "no AI needed"
6. 2.6 Scoping & Success Criteria — define "done" and how you'll measure value
7. 2.7 Risk, Data & Compliance Early — spotting privacy, legal & data-quality flags upfront
8. 2.8 **Lab:** Translate a Messy Client Ask — turn a vague request into a one-line technical spec

---

### PART B — Technical Foundations

#### Module 3 — Python & Programming Foundations (6 lessons)

1. 3.1 Python Essentials — variables, data types, control flow, functions, OOP basics
2. 3.2 Working with Data in Python — lists, dicts, files, JSON, pandas & numpy basics
3. 3.3 Python for AI — requests, virtual environments, pip, async basics
4. 3.4 Git & GitHub — version control, branches, commits, pull requests, collaboration
5. 3.5 Linux & Command Line Basics — shell, files, permissions, environment variables
6. 3.6 Clean Code & Debugging — readable code, error handling, logging, testing basics

#### Module 4 — Software & API Development (7 lessons)

1. 4.1 Software Development Fundamentals — project structure, modularity, environments, dependencies
2. 4.2 What is an API? — REST fundamentals, HTTP methods, status codes, JSON
3. 4.3 Building APIs with FastAPI / Flask — endpoints, request/response, validation
4. 4.4 API Integrations — consuming third-party APIs, authentication, API keys, webhooks
5. 4.5 Databases for FDEs — SQL vs NoSQL, CRUD, connecting a database to your app
6. 4.6 Backend Fundamentals — auth, environment configs, error handling, rate limiting
7. 4.7 **Lab:** Build & Expose a REST API — ship a working API that serves data to a client

#### Module 5 — Machine Learning Basics (5 lessons)

1. 5.1 What is Machine Learning? — supervised vs unsupervised; where ML fits for an FDE
2. 5.2 Core Algorithms — regression, classification, clustering (practical intuition)
3. 5.3 The ML Workflow — data → features → train → evaluate → predict (scikit-learn)
4. 5.4 Model Evaluation — accuracy, precision/recall, overfitting, train/test split
5. 5.5 **Lab:** Build Your First ML Model — train & evaluate a classifier on real data

#### Module 6 — Deep Learning & Transformer Architecture (5 lessons)

1. 6.1 Neural Networks Explained — neurons, layers, weights, activation
2. 6.2 How Networks Learn — forward pass, loss, backpropagation, gradient descent (intuition)
3. 6.3 Key Architectures — CNNs (images) & RNNs (sequences): what & when
4. 6.4 Transformer Architecture — "Attention is all you need", the high-level mental model
5. 6.5 From Deep Learning to GenAI — why transformers led to LLMs

---

### PART C — Applied AI (the FDE toolkit)

#### Module 7 — AI & GenAI Foundations (4 lessons)

1. 7.1 Generative AI & the AI → ML → DL → GenAI evolution — models that generate content, not just classify
2. 7.2 Tokens & Tokenization — how LLMs see text; why tokens drive cost & limits
3. 7.3 Customizing AI: Pre-training vs Fine-tuning vs RAG; Open vs Closed models — when to use each
4. 7.4 AI Application Lifecycle — Idea → Prototype → Eval → Production → Monitor

#### Module 8 — Working with LLMs (4 lessons)

1. 8.1 How LLMs Work & Context Windows — next-token prediction; the LLM's "RAM"
2. 8.2 Hallucination — why LLMs make things up; mitigation strategies
3. 8.3 Model Selection for FDEs — Claude / GPT-4o / Gemini / LLaMA; the cost–speed–quality triangle
4. 8.4 API vs Self-Hosted, Cost & Latency — token pricing, batching, caching; compliance & scale

#### Module 9 — Prompt Engineering Essentials (4 lessons)

1. 9.1 Prompt Engineering Overview — 80% of AI quality comes from prompts
2. 9.2 Core Techniques — zero-shot, few-shot, chain-of-thought & prompt chaining
3. 9.3 System Prompts, Structured Output & Controls — persona + constraints; JSON mode; temperature
4. 9.4 Evaluation & Enterprise Patterns — A/B testing; classification, extraction, summarization, transformation

#### Module 10 — RAG & Vector Databases (5 lessons)

1. 10.1 RAG Foundations — retrieval-augmented generation, embeddings & vector databases
2. 10.2 Building a RAG Pipeline — chunking, similarity search; ingest → embed → store → retrieve → generate
3. 10.3 Retrieval Strategies & Metadata Filtering — Top-K, MMR, re-ranking; filter before vector search
4. 10.4 Advanced RAG — Self-query, HyDE, Corrective RAG, RAPTOR
5. 10.5 RAG Evaluation — faithfulness, answer relevance, context recall (RAGAS)

#### Module 11 — AI Agents & Agentic AI (5 lessons)

1. 11.1 What is an Agent? — LLM + Tools + Memory + Decision Loop; tool calling via JSON schema
2. 11.2 Agentic Patterns — ReAct (Reason → Act → Observe → Repeat), planning, reflection, memory
3. 11.3 Multi-Agent Systems & Frameworks — supervisor-worker, peer agents; LangChain & LangGraph
4. 11.4 Agent Observability — trace every step; log tool calls; measure token usage
5. 11.5 **Lab: Research Agent** — accepts a research question → searches the web (`web_search`) → reads relevant pages (`read_url`) → synthesizes a structured report → saves output (`write_file`)

#### Module 12 — MCP & AI Workflow Automation (4 lessons)

1. 12.1 What is MCP? — standard protocol for LLMs to call external tools safely; MCP vs REST API
2. 12.2 MCP Components — Host (Claude Desktop), Client (app), Server (tool wrapper)
3. 12.3 Building an MCP Server — expose any tool (DB, API, file system) via MCP
4. 12.4 AI Workflow Design & Automation — directed graphs + human checkpoints; trigger, event-driven & scheduled patterns

#### Module 13 — AI-Assisted Software Engineering (8 lessons)

1. 13.1 AI-First SDLC — Prompt → Generate → Review → Refine → Ship
2. 13.2 Claude Code — agentic CLI that reads/writes files, runs commands, fixes bugs
3. 13.3 Cursor — AI-native IDE, inline generation, codebase-aware completions
4. 13.4 GitHub Copilot — autocomplete + chat, line-by-line acceleration
5. 13.5 Rapid Prototyping — 0 → working demo in 2 hours using AI tools
6. 13.6 AI Code Review — use AI to review your own PRs before submitting
7. 13.7 AI Debugging — "here's the error + stack trace, what's wrong?"
8. 13.8 **Lab:** Build a Full Feature in 2 Hours Using AI Tools

---

### PART D — Build, Deploy & Ship (the engineer)

#### Module 14 — Data Engineering & System Design for AI (11 lessons)

1. 14.1 DE Fundamentals — data is the fuel for AI; FDEs must be able to wrangle it
2. 14.2 ETL vs ELT — load first, transform in the warehouse
3. 14.3 Data Lake vs Lakehouse — Delta Lake on object storage
4. 14.4 Medallion Architecture — Bronze (raw) → Silver (cleaned) → Gold (business-ready)
5. 14.5 Batch vs Streaming — batch for history; streaming for real-time AI
6. 14.6 Data Pipelines — ingestion → transformation → loading → validation
7. 14.7 Data Quality — null checks, schema validation, freshness monitoring
8. 14.8 Platform Landscape — Databricks, Snowflake, dbt, Airflow, Kafka: when to use each
9. 14.9 AI System Design Fundamentals — requirements → components → data flow → interfaces
10. 14.10 Designing the AI Data Layer — feature stores, vector stores, caches
11. 14.11 Scalability & Reliability Patterns — load balancing, queues, retries, idempotency, graceful degradation

> The brochure heading says "12 lessons" but lists 11 (14.1–14.11).

#### Module 15 — DevOps & Containerization (8 lessons)

1. 15.1 DevOps for FDEs — the build → ship → run loop
2. 15.2 Git in Depth — branching strategies, merge vs rebase, conflict resolution, workflows
3. 15.3 Docker Fundamentals — images, containers, Dockerfile, volumes, networking
4. 15.4 Docker Compose — run multi-container AI apps (app + DB + vector store)
5. 15.5 Kubernetes Fundamentals — pods, deployments, services, scaling & self-healing
6. 15.6 Kubernetes for AI Workloads — deploying & scaling AI services on K8s
7. 15.7 CI/CD Pipelines — GitHub Actions: test → build → deploy on every merge
8. 15.8 **Lab:** Containerize & Orchestrate an AI App — Docker Compose → deploy on Kubernetes

#### Module 16 — Cloud Architecture & AI Deployment (15 lessons)

1. 16.1 Cloud-Native Principles — design for failure; scale horizontally; automate everything
2. 16.2 AWS Well-Architected — the 5 pillars every FDE should know before touching client cloud
3. 16.3 AI Platform Deployment — where AI apps live: EC2, Lambda, ECS, Bedrock, SageMaker
4. 16.4 Microservices & APIs — decompose AI apps into independently deployable services
5. 16.5 Docker for AI — consistent, portable, deployable containers
6. 16.6 Kubernetes for AI at Scale — orchestrate, scale & self-heal production AI services
7. 16.7 Serverless for AI — Lambda for lightweight inference; cost-effective event-driven AI
8. 16.8 Model Serving & Inference Infrastructure — endpoints, autoscaling, GPU vs CPU, batching for throughput
9. 16.9 Deployment Strategies — blue-green, canary & rolling releases for AI services
10. 16.10 Infrastructure as Code — Terraform / CloudFormation: reproducible, version-controlled environments
11. 16.11 CI/CD for FDEs — automated test → build → deploy for AI services
12. 16.12 Observability & Monitoring in Production — logs, metrics, tracing, latency, cost & drift dashboards
13. 16.13 Security Fundamentals — IAM least-privilege; VPC isolation; secrets in AWS Secrets Manager
14. 16.14 AI-Specific Security — prompt injection, jailbreaks, data poisoning, model & output security
15. 16.15 **Lab:** Deploy an AI Service End-to-End — container → cloud → CI/CD → monitored production endpoint

#### Module 17 — LLMOps & Production Operations (10 lessons)

1. 17.1 LLMOps vs MLOps — what's different when operating LLM systems in production
2. 17.2 Model Versioning & Registry — promote, roll back, and audit models (not just code)
3. 17.3 Prompt & Config Management — version prompts, feature-flag AI behavior, ship changes safely
4. 17.4 Guardrails & Safety in Production — input/output filtering, PII redaction, content moderation at the edge
5. 17.5 Production Evaluation — online eval, A/B testing live traffic, human-in-the-loop feedback loops
6. 17.6 Cost Management & FinOps for AI — token/GPU cost monitoring, budgets, rate limiting, quotas
7. 17.7 Scaling & Resilience — request queuing, caching layers, fallback models when the primary is down
8. 17.8 Environment & Release Strategy — dev/staging/prod separation, secrets rotation, disaster recovery
9. 17.9 Monitoring, Drift & Incident Response — quality drift, alerting, on-call runbooks for AI systems
10. 17.10 **Lab:** Operate a Live AI System — add versioning, guardrails, cost tracking & monitoring to a deployed service

#### Module 18 — AI Ethics, Responsible AI & Compliance (8 lessons)

> Mandatory for enterprise clients like banks and hospitals. An FDE who can speak to ethics, safety, and
> regulation earns trust; one who can't loses the deal.

1. 18.1 Responsible AI Foundations — ethics & safety as a business requirement, not an afterthought
2. 18.2 Bias & Fairness — where bias comes from; detecting & mitigating it in AI systems
3. 18.3 Transparency & Explainability — making AI decisions understandable & auditable
4. 18.4 AI Regulations & the EU AI Act — risk tiers, obligations & what enterprises must comply with
5. 18.5 Data Privacy & Compliance — GDPR, HIPAA, data residency & handling sensitive data
6. 18.6 PII & Sensitive Data Handling — detection, redaction, anonymization, access control
7. 18.7 Governance & Audit Trails — policies, approvals, logging & accountability for AI in production
8. 18.8 **Lab:** Add a Compliance & Safety Layer — bias check, PII redaction & audit logging on an AI service

---

### PART E — Deliver Like an FDE (the differentiator)

#### Module 19 — Client Engagement & Communication (10 lessons)

1. 19.1 Conducting Client Workshops — facilitate, align stakeholders, extract requirements
2. 19.2 Communicating to Technical & Non-Technical Stakeholders — same solution, two languages
3. 19.3 Technical Storytelling — problem → journey → outcome; make people care
4. 19.4 Solution Presentation & Demos — show, don't tell; run a demo that sells
5. 19.5 Managing Expectations — scope, timelines, and saying no gracefully
6. 19.6 Handling Difficult Stakeholders — skeptics, scope-creep, and conflicting priorities
7. 19.7 Writing Technical Briefs & Proposals — clear, persuasive, approvable documents
8. 19.8 Implementation Roadmaps — phasing, milestones, and quick wins
9. 19.9 Running the Feedback Loop — iterate in front of the client without losing control
10. 19.10 **Lab:** Pitch & Present a Solution — present a POC to a mock client panel

#### Module 20 — Enterprise Delivery, Pricing & Consulting (14 lessons)

Taking a solution all the way to a delivered, trusted, handed-over system — including how you scope,
estimate, and price the engagement — plus building your own FDE career.

1. 20.1 The FDE Delivery Model — how FDEs embed, deliver, and create value
2. 20.2 Converting Business Problems into AI Solutions — end-to-end, in practice
3. 20.3 Designing Solutions Around Business Objectives — tie every build to measurable value
4. 20.4 Scoping an Engagement — breaking a project into phases, effort & deliverables
5. 20.5 Cost Estimation & Pricing a Project — estimating effort, AI running costs & pricing the engagement
6. 20.6 Building Rapid POCs — prove value fast, de-risk the project
7. 20.7 Enterprise Project Planning — milestones, risks, realistic timelines
8. 20.8 Delivery Best Practices — quality, documentation, and handover
9. 20.9 Training & Enabling the Client — make the client independent after you leave
10. 20.10 Measuring & Reporting ROI — show the business impact you delivered
11. 20.11 Real-World Client Engagement Scenarios — case-based practice
12. 20.12 Portfolio Building — case studies & GitHub projects that prove you can deliver
13. 20.13 LinkedIn & Personal Branding — get found and hired as an FDE
14. 20.14 The End-to-End Enterprise AI Delivery Framework — the full FDE method, start to finish

#### Module 21 — Hands-On Projects (Real Use Cases) (10 lessons)

Two full, guided projects before the solo capstone; each a real enterprise use case taken end-to-end
(discover, build, deploy, deliver).

**Project 1 — Enterprise Knowledge Assistant (RAG).** A hospital / bank support desk is drowning in
repetitive questions. Build an AI assistant that answers accurately from the client's own documents,
with sources and safe fallbacks.

1. 21.1 Discover & Translate — scope the FAQ problem; write the technical spec
2. 21.2 Build the RAG Pipeline — ingest PDFs → chunk → embed → vector store → retrieve
3. 21.3 Add Guardrails & Grounding — source citations, "I don't know" fallback, PII filtering
4. 21.4 Deploy & Expose — containerize, put behind an API, ship a simple chat UI
5. 21.5 Evaluate & Deliver — RAGAS accuracy check, cost tracking, handover

**Project 2 — Document Processing & Automation Agent.** An operations team manually reads incoming
documents (invoices, claims, contracts), extracts data, and files it. Build an agent that reads
documents, extracts structured data, validates it, and pushes it into a system automatically.

6. 21.6 Discover & Translate — map the manual workflow; define what to automate
7. 21.7 Build the Extraction Agent — read documents → extract structured JSON → validate
8. 21.8 Tool Calling & Integration — push validated data to a database / API via tools
9. 21.9 Human-in-the-Loop & Automation — approval checkpoints; trigger/scheduled runs
10. 21.10 Deploy, Monitor & Deliver — ship it, add observability & cost controls, hand over

#### Module 22 — Capstone: End-to-End FDE Engagement (8 lessons)

Take one real problem from a confused client to a live, delivered solution — solo.

1. 22.1 Pick Your Client & Problem — hospital, bank, HR, legal, education, or your own
2. 22.2 Discover & Translate — find the real problem; write the technical spec
3. 22.3 Design the Solution — architecture, approach, and tool choices
4. 22.4 Build the POC — a working demo that proves it
5. 22.5 Deploy It Live — container → cloud → monitored endpoint
6. 22.6 Operate & Harden — guardrails, cost tracking, monitoring
7. 22.7 Present & Deliver — pitch the solution and hand it over
8. 22.8 Portfolio Write-Up — turn your capstone into a hire-me case study

---

## Part 2 — APIDS / APIDA (Data Science & AI)

### Program Overview

| | APIDS — Industrial Data Science | APIDA — Industrial Data Analytics |
| --- | --- | --- |
| Focus | Full 360° data science: DBMS programming, data analysis, advanced visualization, storytelling dashboards, advanced ML and Generative AI | Data analytics: DBMS programming, data analysis, advanced visualization, storytelling dashboards, advanced analytics for predictive models |
| DBMS & Automation | SQL, SAS, Python, PySpark, Scala, Bigdata | SQL, SAS, Python |
| Analysis & Visualization | Excel Base & Advanced, Power BI, Tableau, Alteryx | Excel Base & Advanced, Power BI, Tableau, Alteryx |
| Data Mining | Advanced Analytics using Excel, SAS and Python; Advanced ML, DL and Generative AI using Python | Advanced Analytics using Excel, SAS and Python |
| Cloud Computing | AWS, Azure, GCP (with Hadoop/Spark, Docker, Kubernetes context) | — |
| LLMs & Prompt Engineering | ChatGPT, Google Gemini, Claude etc. for optimizing workflow models | ChatGPT, Google Gemini, Claude etc. for optimizing workflow models |
| Soft Skills | Spoken English, speech control, corporate code of conduct | Spoken English, speech control, corporate code of conduct |

- **Duration:** 6–8 months, live (online or offline) with all sessions recorded on the LMS
- **Eligibility:** Any graduate, post-graduate, master's or PhD, any discipline; working and non-working professionals
- **Includes:** real-time industry projects, project mentorship & resume building, soft-skills development, tests & mock interviews, job referrals

> The brochure's APIDS-vs-APIDA application matrix uses tick marks that do not survive text extraction. The
> table above is reconstructed from each program's written "Skills and Applications" section, so the
> APIDS-only rows (Bigdata/Scala/PySpark, Cloud, ML & AI, GenAI) should be confirmed against the printed matrix.

### Curriculum

#### Module 1 — Introduction to Data Science and Excel

1. **1.1 Overview of Data Science** — definition and importance; the data science lifecycle; key roles (Data Analyst, Data Scientist, Data Engineer)
2. **1.2 Introduction to Excel for Data Analysis** — interface and basic operations; data entry and formatting; basic formulas (SUM, AVERAGE, COUNT, MAX, MIN)
3. **1.3 Advanced Excel Functions** — logical (IF, AND, OR, NOT); lookup (VLOOKUP, HLOOKUP, INDEX-MATCH); text (LEFT, RIGHT, MID, CONCATENATE); date and time
4. **1.4 Data Cleaning and Preparation in Excel** — removing duplicates; handling missing values; text to columns; data validation
5. **1.5 Excel Pivot Tables and Charts** — creating and customizing pivot tables; pivot charts and slicers; calculated fields and items
6. **1.6 Excel Data Analysis Tools** — descriptive statistics with the Data Analysis ToolPak; correlation and regression; what-if analysis (Goal Seek, Scenario Manager)
7. **1.7 Introduction to Power Query** — importing data from various sources; basic transformations; creating and managing queries
8. **1.8 Excel Macros and VBA Basics** — recording and running macros; introduction to VBA programming; simple user-defined functions

#### Module 2 — SQL for Data Analysis

1. **2.1 Introduction to Databases and SQL** — relational concepts; SQL's role in analysis; setting up a database environment (MySQL, PostgreSQL)
2. **2.2 Basic SQL Queries** — SELECT; filtering with WHERE; sorting with ORDER BY; LIMIT/TOP
3. **2.3 Working with Multiple Tables** — joins (INNER, LEFT, RIGHT, FULL OUTER); UNION and UNION ALL; subqueries
4. **2.4 Aggregations and Group Operations** — aggregate functions (COUNT, SUM, AVG, MAX, MIN); GROUP BY; HAVING
5. **2.5 Advanced SQL Techniques** — window functions; Common Table Expressions (CTEs); CASE statements; handling NULL values
6. **2.6 Data Manipulation with SQL** — INSERT, UPDATE, DELETE; creating and altering tables; views and temporary tables
7. **2.7 Optimizing SQL Queries** — query execution plans; indexing basics; optimization techniques
8. **2.8 SQL for Data Analysis Projects** — cohort analysis; customer segmentation; funnel analysis; time series analysis with SQL

#### Module 3 — Data Visualization with Tableau

1. **3.1 Introduction to Tableau** — product overview; interface and workspace; connecting to data sources
2. **3.2 Creating Basic Visualizations** — bar charts and histograms; line and area charts; scatter and bubble plots; pie charts and treemaps
3. **3.3 Working with Dimensions and Measures** — dimensions vs measures; discrete vs continuous fields; changing aggregation methods; calculated fields
4. **3.4 Advanced Chart Types** — box and violin plots; Gantt charts; bullet graphs; waterfall charts
5. **3.5 Maps and Geospatial Analysis** — basic maps; custom territories and geocoding; map layers; spatial calculations
6. **3.6 Dashboards and Stories** — designing effective dashboards; interactivity with actions and filters; Tableau stories for presentations
7. **3.7 Advanced Tableau Techniques** — table calculations; Level of Detail (LOD) expressions; parameters and what-if analysis; trend lines and forecasting
8. **3.8 Tableau Best Practices and Optimization** — performance optimization; visual design best practices; sharing and publishing; Tableau Server basics

#### Module 4 — Business Intelligence with Power BI

1. **4.1 Introduction to Power BI** — Desktop, Service, Mobile; interface and components; connecting to various data sources
2. **4.2 Data Transformation with Power Query** — Power Query Editor; basic data cleaning; combining and merging queries; custom columns and measures
3. **4.3 Data Modeling in Power BI** — relationships between tables; star vs snowflake schema; hierarchies and date tables; modeling best practices
4. **4.4 DAX (Data Analysis Expressions)** — introduction to DAX; calculated columns and measures; time intelligence functions; advanced functions (CALCULATE, FILTER, ALL)
5. **4.5 Visualizations in Power BI** — standard charts; matrix and table visualizations; custom visuals from AppSource; map visualizations
6. **4.6 Power BI Reports and Dashboards** — effective report design; interactivity with slicers and filters; creating and sharing dashboards; mobile-optimized reports
7. **4.7 Power BI Service and Collaboration** — publishing to the Service; app workspaces; row-level security; sharing and collaborating on reports
8. **4.8 Advanced Power BI Features** — dataflows; AI insights and quick measures; real-time streaming datasets; embedding reports

#### Module 5 — Python Programming for Data Science

1. **5.1 Introduction to Python** — environment setup (Anaconda, Jupyter Notebook); syntax and basic data types; control structures; functions and modules
2. **5.2 Data Structures in Python** — lists, tuples, dictionaries; sets and arrays; list comprehensions; working with strings
3. **5.3 NumPy for Numerical Computing** — arrays and operations; indexing and slicing; broadcasting; linear algebra operations
4. **5.4 Pandas for Data Manipulation** — Series and DataFrame objects; reading and writing data (CSV, Excel, SQL); cleaning and preprocessing; merging, grouping, aggregating
5. **5.5 Data Visualization with Matplotlib and Seaborn** — basic plots with Matplotlib; customizing appearance; statistical visualization with Seaborn; interactive plotting with Plotly
6. **5.6 Exploratory Data Analysis (EDA)** — descriptive statistics; correlation analysis; handling missing data; outlier detection and treatment
7. **5.7 Web Scraping and API Interaction** — HTML basics and inspecting web pages; scraping with BeautifulSoup; working with APIs (requests library); parsing JSON
8. **5.8 Introduction to Object-Oriented Programming** — classes and objects; inheritance and polymorphism; custom data structures; OOP best practices for data science

#### Module 6 — Machine Learning with Python

1. **6.1 Introduction to Machine Learning** — supervised, unsupervised, reinforcement; the ML workflow; train-test split and cross-validation; bias-variance tradeoff
2. **6.2 Scikit-learn Library** — overview; data preprocessing techniques; feature selection and engineering; Pipeline and FeatureUnion
3. **6.3 Supervised Learning: Regression** — linear regression; polynomial regression; regularization (Ridge, Lasso); decision trees and random forests for regression
4. **6.4 Supervised Learning: Classification** — logistic regression; Support Vector Machines (SVM); decision trees and random forests; Naive Bayes classifiers
5. **6.5 Unsupervised Learning** — K-means clustering; hierarchical clustering; Principal Component Analysis (PCA); t-SNE for dimensionality reduction
6. **6.6 Ensemble Methods** — bagging and random forests; boosting (AdaBoost, Gradient Boosting); stacking ensembles; voting classifiers
7. **6.7 Model Evaluation and Hyperparameter Tuning** — regression and classification metrics; confusion matrix and ROC curves; grid search and random search; AutoML tools

#### Module 7 — Deep Learning and Neural Networks

1. **7.1 Introduction to Neural Networks** — artificial neurons and activation functions; feedforward neural networks; the backpropagation algorithm; gradient descent optimization
2. **7.2 Deep Learning Frameworks: TensorFlow and Keras** — TensorFlow basics and computational graphs; Keras API overview; building and training simple networks; saving and loading models
3. **7.3 Convolutional Neural Networks (CNNs)** — convolution and pooling operations; architectures (LeNet, AlexNet, VGG); transfer learning with pre-trained models; image classification and object detection
4. **7.4 Recurrent Neural Networks (RNNs)** — sequential data and RNN architecture; LSTM networks; GRUs; applications in text generation and sentiment analysis
5. **7.5 Autoencoders and Generative Models** — autoencoder architecture and applications; Variational Autoencoders (VAEs); introduction to GANs; style transfer and image generation
6. **7.6 Natural Language Processing with Deep Learning** — word embeddings (Word2Vec, GloVe); sequence-to-sequence models; attention mechanisms; Transformer architecture and BERT

#### Module 8 — GenAI, Advanced LLM Models and LangChain Applications

1. **8.1 LLM Models from Hugging Face** — installing and setting up the environment; pretrained language models and their usage; NLP tasks (classification, NER, Q&A, text generation); Hugging Face Pipelines for streamlining NLP workflows; fine-tuning pretrained models for specific tasks; deploying models to different environments; *case study: bank customer complaints classification*
2. **8.2 LangChain Fundamentals** — introduction to LangChain; installation and setup; main components; getting started with LangChain and OpenAI; LangChain with Hugging Face models; chains and working with prompts
3. **8.3 LangChain Model I/O** — basic document loader and chain on loaded documents; CSVLoader and WebBaseLoader; Wikipedia, PyPDFLoader and BSHTMLLoader; output parsers (CSV parser, Pydantic)
4. **8.4 LangChain — RAG (Retrieval-Augmented Generation)** — building a retrieval chain; understanding Refine, MapReduce and MapRerank; embeddings (understanding, download, visualization); prompt composition and templates; using multiple LLMs (chains); data loaders and text splitters; introducing ChromaDB; working with various chains (Conversational Retrieval QA, Retrieval QA, Summarization, API)
5. **8.5 LangChain Memory and Chatbots** — the concept of memory and ConversationBufferMemory; the four types of memory in LangChain; building applications with memory; chatbot using LangChain and ConversationalRetrievalChain; chatbot with RAG; tool — a chatbot that talks to multiple documents
6. **8.6 LangChain Agents and Tools** — the concept of tools and LangChain agents; ReAct (Reasoning and Acting) prompting; SerpApi tool and a PPT-maker app; CSV agent and a "Talk to your Data" app; custom tools

#### Module 9 — Agentic AI

1. **Introduction to Agentic AI** — AI agents vs traditional AI models; what makes AI "agentic" (autonomy, goals, tool use); the role of LLMs in agent-based systems; real-world applications and use cases; the agent ecosystem (frameworks, orchestration, integrations)
2. **Core Concepts and Architecture** — key components (perception, reasoning, planning, action); memory systems (short-term vs long-term); prompt engineering for agents; multi-agent collaboration patterns; evaluation metrics for agents
3. **Agentic AI Frameworks Overview** — comparing AutoGen, CrewAI, LangChain Agents, LlamaIndex Agents; when to use which (trade-offs and strengths); interoperability between frameworks; case studies of production-grade agent systems
4. **Building with AutoGen** — introduction and architecture; single-agent workflows; multi-agent conversations and task delegation; integrating tools and APIs; error handling and resilience; *project: two-agent research & writing system*
5. **Building with CrewAI** — basics and setup; roles, skills and task distribution; orchestrating multiple agents for a business process; dynamic role assignment and runtime decision-making; integrating external APIs; *project: customer-support agent crew*
6. **n8n for Agentic Automation** — n8n as a visual workflow orchestrator; connecting LLMs and agents into workflows; webhooks, triggers and event-driven agents; passing context between n8n nodes and agents; real-time data pipelines for agents; *project: Telegram chatbot agent with an n8n backend*
7. **MCP (Model Context Protocol)** — understanding the MCP specification; how MCP enables tools and data access for agents; setting up an MCP server and integrating it into workflows; MCP client-server communication in agent systems; using MCP with AutoGen, CrewAI and n8n; scaling multi-agent systems; *project: MCP-enabled knowledge retrieval agent*

### Hands-On Industry Projects

Projects are drawn from five domains:

| Domain | Representative problems |
| --- | --- |
| **Retail Marketing** | Targeted customer communication; price optimization; demand prediction and inventory management; customer experience enhancement; market trend prediction; customer retention; strategic decisions to increase sales |
| **Banking** | Customer identification and acquisition; portfolio analysis and risk management; customer retention; credit risk analysis; collection analysis; marketing analysis |
| **Telecom** | Revenue forecasting; churn prediction; fraud prevention; average revenue per unit (ARPU); risk management; profit-based customer segmentation; social network analysis; customer sentiment analysis |
| **E-Commerce** | Customer identification and acquisition; portfolio analysis and risk management; customer retention; credit risk analysis; collection analysis; marketing analysis |
| **Healthcare** | Risk analysis; insurance claim analysis; operations analysis; patient care analysis; performance monitoring; operational and interactive dashboards |

---

## Combined Coverage Map

Where the two programs overlap and where each is unique:

| Topic area | FDE program | APIDS / APIDA |
| --- | --- | --- |
| Excel, VBA, Power Query | — | Module 1 |
| SQL / databases | Module 4.5 (light) | Module 2 (deep) |
| BI & visualization (Tableau, Power BI) | — | Modules 3–4 |
| Python | Module 3 | Module 5 |
| Software & API development | Module 4 | — |
| Machine learning | Module 5 (basics) | Module 6 (deep) |
| Deep learning & transformers | Module 6 (intuition) | Module 7 (deep: CNN/RNN/GAN/BERT) |
| GenAI & LLM foundations | Modules 7–8 | Module 8.1 |
| Prompt engineering | Module 9 | Module 8 (within LangChain) |
| RAG & vector databases | Module 10 | Module 8.4 (LangChain RAG, ChromaDB) |
| Agents & agentic AI | Module 11 | Module 9 (AutoGen, CrewAI, n8n) |
| MCP | Module 12 | Module 9 (MCP section) |
| AI-assisted software engineering | Module 13 | — |
| Data engineering & system design | Module 14 | PySpark / Bigdata / Scala (APIDS) |
| DevOps, Docker, Kubernetes | Module 15 | Cloud module context (APIDS) |
| Cloud architecture & deployment | Module 16 | AWS / Azure / GCP (APIDS) |
| LLMOps & production operations | Module 17 | — |
| AI ethics & compliance | Module 18 | — |
| Client engagement & communication | Module 19 | Soft skills |
| Enterprise delivery, pricing, consulting | Module 20 | — |
| Guided projects & capstone | Modules 21–22 | Industry projects (5 domains) |
