## Project Prompts Log

This file tracks all prompts used to create and iterate on project files. Update this log whenever you refine instructions or add new tasks.

---

## Scripts Created

### 1. Inference-TextGeneration.py
**Date:** 2025-12-14

**Prompts:**
- "how to build Inference-TextGeneration.py file?"
- "Yes please" (add requirements and README)
- "Please run and validate"
- "Sure please go ahead add" (instrument script with progress logs)
- "Want to add all prompts I've used to create this Python script to the project and keep updaing when needed."

**Input Prompts (model generation):**
- "The future of software engineering is"
- "To fix a segmentation fault, you must"

---

### 2. Inference-FinBERT.py
**Date:** 2025-12-27

**Purpose:** Financial sentiment analysis using specialized FinBERT model

**Input Prompts (financial sentiment):**
- "The company announced a restructuring plan to cut operational costs by 20%."
- "I hate waiting in line at the grocery store."

**Model:** ProsusAI/finbert

---

### 3. LangChain-Setup.py
**Date:** 2025-12-27

**Purpose:** Introduction to LangChain with HuggingFace pipeline integration

**Features:**
- Wraps GPT-2 pipeline in LangChain
- Uses PromptTemplate for structured prompts
- LCEL (LangChain Expression Language) chain syntax

**Example Topic:** "Docker" (originally "Recursion")

---

### 4. LangChainWithOutputParser.py
**Date:** 2025-12-28

**Purpose:** LangChain with Output Parser (Data Adapter pattern)

**Features:**
- Demonstrates Output Parser usage
- Clean string output via StrOutputParser
- Fixed `return_full_text=False` for cleaner generation
- Chain: prompt → llm → output_parser

**Example Topic:** "Recursion"

---

### 5. inference.py
**Purpose:** Basic inference script (legacy/base implementation)

---

### 6. RunnableWithMessageHistory.py
**Date:** 2025-12-29

**Purpose:** LangChain conversational memory with message history

**Features:**
- RunnableWithMessageHistory wrapper for stateful conversations
- ChatMessageHistory for session-based memory storage
- ChatPromptTemplate with MessagesPlaceholder
- Session management with configurable session IDs
- Multi-turn conversation tracking

**Dependencies Added:**
- `langchain-community` (for ChatMessageHistory)

**Example Conversation:**
- Turn 1: "Hi, my name is Dave."
- Turn 2: "What is my name?" (tests memory recall)

**Session ID:** "user_123" (demonstrates session isolation)

---

## Git & Project Management

### 2025-12-27
**Git Setup:**
- "Github: Current Python FirstProject regarding Models, don't want to commit model or environment data. How to commit only script changes?"
- "What is the correct way of using gitignore in FirstProject directory?"
- "Can we capture gitignore steps in Wiki page?"

**Created:** GITIGNORE-TEMPLATE.md (Git setup documentation for ML projects)

### 2025-12-29
**Automation & Workflow:**
- "How can I automate prompt file update along with project code updates?"
- "Idea is to have prompt file updated and commit along with code commits."
- "Can you explain about these changes?" (explained commit-with-prompt.sh workflow)

**Script Updates:**
- Created RunnableWithMessageHistory.py (conversational memory with LangChain)
- Installed `langchain-community` package
- Updated PROMPTS.md automation documentation

---

## Notes
- Keep entries concise: what you asked, what changed
- If a prompt leads to code edits, link the file and a short summary of changes
- Added prompt logging CLI (README.md#Prompt Logging CLI)
- Document model names, versions, and input examples for reproducibility
