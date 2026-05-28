# local-ai-research-agent
### Comprehensive AI Engineer Project — 100% Free Stack
> **Goal:** Transition from Full Stack / Backend Engineer to a job-ready AI Engineer by building a real, end-to-end multi-agent research system — locally, for free.

**Stack:** Python 3.12 · Ollama (Mistral 7B) · ChromaDB · LangChain · LangGraph · Streamlit · DuckDuckGo Search  
**Timeline:** ~21 days at 6 hours/day  
**GitHub Repo:** `local-ai-research-agent`

---

## Progress Tracker
Mark steps as you complete them: ⬜ = todo · 🔄 = in progress · ✅ = done

---

## Phase 1 — Environment Setup & RAG Pipeline
> **Days 1–3 · Goal:** Get everything installed and build a working document Q&A app. Upload a PDF, ask questions, get answers grounded in the document.

| # | Status | Step | Key Concepts |
|---|--------|------|--------------|
| 1.1 | ⬜ | Set up project folder, venv, Git repo, folder structure | `python3 -m venv`, `git init`, project structure |
| 1.2 | ⬜ | Install and run Ollama, pull Mistral 7B | `ollama install`, `ollama pull mistral:7b`, local inference |
| 1.3 | ⬜ | Understand ChromaDB — create collection, add text, query it | `PersistentClient`, `collection.add`, `collection.query` |
| 1.4 | ⬜ | Understand embeddings — embed sentences, see similarity scores | `nomic-embed-text`, cosine similarity, vector meaning |
| 1.5 | ⬜ | Build PDF ingestion pipeline — load, chunk, embed, store | `PyMuPDF`, text splitting, chunk size, overlap |
| 1.6 | ⬜ | Build retrieval + answer pipeline — question → search → answer | Similarity search, prompt template, context injection, RAG |
| 1.7 | ⬜ | Wrap everything in a Streamlit UI | `st.file_uploader`, `st.chat_input`, `st.session_state` |

**What you can say in an interview after Phase 1:**
> *"I built a RAG pipeline from scratch — PDF ingestion, chunking, embedding via Ollama, vector storage in ChromaDB, and retrieval-augmented generation — wrapped in a Streamlit UI. No paid APIs."*

---

## Phase 2 — AI Agents & Tool Calling
> **Days 4–7 · Goal:** Give the LLM tools it can choose to use. The model reasons about what to do next, picks a tool, acts, observes the result, and continues. This is where Agentic AI begins.

| # | Status | Step | Key Concepts |
|---|--------|------|--------------|
| 2.1 | ⬜ | Understand the ReAct pattern — Thought → Action → Observation | ReAct loop, chain of thought, agent reasoning |
| 2.2 | ⬜ | Understand tool calling — how the LLM picks a tool | Function signatures, docstrings as instructions, structured output |
| 2.3 | ⬜ | Build three tools: search_docs, web_search, calculate | `@tool` decorator, LangChain tools, DuckDuckGo (free) |
| 2.4 | ⬜ | Create the agent executor and run a test query | `AgentExecutor`, `OllamaLLM`, `initialize_agent`, verbose output |
| 2.5 | ⬜ | Add agent memory — short-term and long-term | `ConversationBufferMemory`, long-term ChromaDB memory |
| 2.6 | ⬜ | Add error handling and retries | `max_iterations`, fallback logic, graceful errors |
| 2.7 | ⬜ | Display agent reasoning steps in Streamlit UI | Callbacks, thought display, `st.expander`, streaming |

**What you can say in an interview after Phase 2:**
> *"I built an AI agent with tool calling — the LLM dynamically decides whether to search my vector store, search the web, or run a calculation using the ReAct pattern. I also implemented short and long-term memory."*

---

## Phase 3 — Agentic AI — Advanced Patterns
> **Days 8–11 · Goal:** The patterns that separate junior AI engineers from seniors. Planning, self-correction, human-in-the-loop, guardrails, and observability. This is what "Agentic AI" actually means in practice.

| # | Status | Step | Key Concepts |
|---|--------|------|--------------|
| 3.1 | ⬜ | Build a planning agent — Plan-and-Execute pattern | Task decomposition, planner, executor, multi-step planning |
| 3.2 | ⬜ | Build a self-correcting agent — reflection loop | Self-reflection, output evaluation, retry on failure |
| 3.3 | ⬜ | Implement human-in-the-loop | HITL, agent pause, human confirmation, approval workflow |
| 3.4 | ⬜ | Add guardrails and safety checks | Input validation, output checking, hallucination detection, topic boundaries |
| 3.5 | ⬜ | Add agent observability — logging and monitoring | Decision logging, token tracking, latency, LangSmith free tier |

**What you can say in an interview after Phase 3:**
> *"I implemented advanced agentic patterns — a planning agent that decomposes tasks before acting, a self-correction loop where the agent evaluates and retries its own output, human-in-the-loop confirmations, and guardrails for input and output validation."*

---

## Phase 4 — Multi-Agent Systems
> **Days 12–16 · Goal:** Multiple specialised agents collaborating under an orchestrator. The most impressive thing you can demonstrate in an interview. Everything comes together here.

| # | Status | Step | Key Concepts |
|---|--------|------|--------------|
| 4.1 | ⬜ | Understand multi-agent architecture — orchestrator, specialist, critic | Agent roles, coordination patterns, when to split agents |
| 4.2 | ⬜ | Understand LangGraph — nodes, edges, state machine | `StateGraph`, nodes, edges, shared state, conditional edges |
| 4.3 | ⬜ | Build the Researcher agent — returns structured JSON findings | Structured output, JSON schema, search tools |
| 4.4 | ⬜ | Build the Writer agent — turns findings into a report | Grounded generation, context window, report structure |
| 4.5 | ⬜ | Build the Critic agent — scores and sends feedback | Quality scoring, structured feedback, revision instructions |
| 4.6 | ⬜ | Build the Orchestrator with LangGraph | `StateGraph`, loop control, quality threshold, max iterations |
| 4.7 | ⬜ | Real-time multi-agent UI in Streamlit | `st.status`, streaming, agent status display, source citations |

**What you can say in an interview after Phase 4:**
> *"I built a multi-agent research system — a Researcher, Writer, Critic, and Orchestrator — coordinated using LangGraph as a state machine. The system researches a topic, writes a report, critiques it, and revises until a quality threshold is met. All streamed live in a Streamlit UI."*

---

## Phase 5 — Polish, GitHub & Interview Prep
> **Days 17–21 · Goal:** Make everything interview-ready. Clean code, strong README, architecture diagram, demo video, and you can answer every AI engineering interview question cold.

| # | Status | Step | Key Concepts |
|---|--------|------|--------------|
| 5.1 | ⬜ | Refactor and clean the codebase | Type hints, docstrings, `.env`, folder structure, no hardcoding |
| 5.2 | ⬜ | Write the README | Project overview, setup guide, architecture, learnings |
| 5.3 | ⬜ | Create the architecture diagram | Mermaid or draw.io, agent flow, data flow, LangGraph state machine |
| 5.4 | ⬜ | Record the demo video | OBS, 2–3 min script, end-to-end demo, YouTube unlisted |
| 5.5 | ⬜ | Interview question prep — all phases | RAG questions, agent questions, agentic AI, system design |
| 5.6 | ⬜ | Full mock interview | You answer, I give honest feedback on every answer |

**What you can say in an interview after Phase 5:**
> *"Here's my GitHub — local-ai-research-agent. The README has the architecture diagram and a link to a live demo. Want me to walk you through how the orchestrator manages the agent loop?"*

---

## Full Stack Summary

| Layer | Technology | Why |
|-------|-----------|-----|
| LLM | Ollama + Mistral 7B | 100% local, free, no API key |
| Embeddings | nomic-embed-text via Ollama | Free, runs locally |
| Vector DB | ChromaDB | Local file-based, no server needed |
| Agent framework | LangChain | Industry standard, free, open source |
| Multi-agent orchestration | LangGraph | State machine for complex agent flows |
| Web search tool | DuckDuckGo Search | Free, no API key required |
| UI | Streamlit | Pure Python, free, fast to build |
| Language | Python 3.12 | Industry standard for AI engineering |

---

## Interview Questions This Project Unlocks

### RAG
- What is RAG and why do we need it?
- How do you choose chunk size and overlap?
- What is the difference between semantic search and keyword search?
- How would you improve retrieval accuracy?

### AI Agents
- What is an AI agent and how is it different from a single LLM call?
- Explain the ReAct pattern in plain English
- How does the LLM know which tool to call?
- What is the difference between short-term and long-term agent memory?

### Agentic AI
- What does "agentic" mean and how is it different from "AI agent"?
- How do you prevent an agent from running in an infinite loop?
- What is human-in-the-loop and when would you use it?
- How do you add guardrails to an agentic system?

### Multi-Agent
- Why would you split work across multiple agents instead of one?
- What is an orchestrator agent?
- How does LangGraph manage state between agents?
- How do you handle a situation where one agent produces bad output?

### System Design
- How would you scale this system to handle 1000 users?
- How would you monitor an agent in production?
- What would you change if you had access to the OpenAI API?
- How do you evaluate the quality of your agent's output?

---

*Built during job search — fully local, 100% free stack — by a Full Stack Engineer transitioning to AI Engineering.*
