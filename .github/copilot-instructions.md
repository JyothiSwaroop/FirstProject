# AI Agent Instructions for FirstProject

## Project Overview
This is a **learning sandbox for ML model inference and LangChain integration**. Focus: exploring HuggingFace transformers and LangChain patterns with local models. Not production code—emphasize reproducibility and educational clarity.

## Environment & Dependencies

**Python environment:** `ai_env/` (Python 3.14 venv, pre-configured)

**Activate before any work:**
```bash
source ai_env/bin/activate
```

**Core dependencies (pinned in requirements.txt):**
- `transformers==4.57.3` - HuggingFace pipeline API
- `torch==2.9.1` - PyTorch backend
- `langchain_huggingface`, `langchain_core` - LangChain integration

**Install new packages:** Always update `requirements.txt` with pinned versions after adding dependencies.

## Codebase Patterns

### 1. Script Structure (Inference Files)
All inference scripts follow this pattern (see [Inference-TextGeneration.py](Inference-TextGeneration.py)):
```python
# 1. Setup (with progress logging)
print("[init] Loading model...")
pipeline_or_model = pipeline(...)

# 2. Input Prompts (document these in PROMPTS.md)
prompts = ["Example prompt 1", "Example prompt 2"]

# 3. Inference
print("[generate] Running inference...")
outputs = model(prompts)

# 4. Output formatting
print("[output] Printing results")
# Format and display
```

**Progress logging convention:** Use `[stage]` prefixes in print statements (`[init]`, `[generate]`, `[output]`) for execution tracking.

### 2. LangChain Integration (LCEL Chains)
LangChain scripts use **LCEL (pipe syntax)** for composition (see [LangChainWithOutputParser.py](LangChainWithOutputParser.py)):

```python
# Backend: Wrap HF pipeline
pipe = pipeline('text-generation', model='gpt2', return_full_text=False)  # ← Critical: prevents input duplication
llm = HuggingFacePipeline(pipeline=pipe)

# Frontend: Prompt template
prompt = PromptTemplate.from_template("...")

# Data adapter: Output parser
output_parser = StrOutputParser()

# Chain composition (LCEL)
chain = prompt | llm | output_parser
result = chain.invoke({"topic": "..."})
```

**Important:** Always set `return_full_text=False` in pipelines to avoid echoing input in output.

### 3. Model Specialization Pattern
Use task-specific models from HuggingFace Hub (see [Inference-FinBERT.py](Inference-FinBERT.py)):
- Financial sentiment: `ProsusAI/finbert`
- General text generation: `gpt2`

Structure: `classifier = pipeline("task", model="org/model-name")`

## Critical Workflows

### Adding New Scripts
1. **Create script** following the 4-part structure above
2. **Document in PROMPTS.md** using the CLI:
   ```bash
   python scripts/add-prompt.py --note "Added X script for Y functionality"
   ```
3. **Add input prompts** to `PROMPTS.md` under "Script Input Prompts" section
4. **Update requirements.txt** if new dependencies added
5. **Test execution** and verify progress logs appear

### Prompt Logging (CRITICAL)
**PROMPTS.md tracks ALL iterations and changes.** Use [scripts/add-prompt.py](scripts/add-prompt.py):

```bash
python scripts/add-prompt.py --note "What you're doing" [--link "file.py"] [--section "Section Name"]
```

**Smart commit workflow** (recommended):
```bash
git add <files>
bash scripts/commit-with-prompt.sh  # Auto-prompts for PROMPTS.md update
```

### Git Hooks
Pre-commit hook warns if Python files are committed without updating PROMPTS.md. Set up with:
```bash
bash scripts/setup-git-hooks.sh
```

## File Organization

- **Inference-*.py**: Standalone model inference examples
- **LangChain*.py**: LangChain integration patterns
- **scripts/**: Automation (prompt logging, git hooks)
- **PROMPTS.md**: Central log of session prompts, script inputs, and changes (see [PROMPTS.md](PROMPTS.md) structure)
- **GITIGNORE-TEMPLATE.md**: Reference for ML project git setup (excludes `ai_env/`, model caches)

## Testing & Validation
Run scripts directly:
```bash
python Inference-TextGeneration.py
```

**First run:** Models download to HuggingFace cache (~500MB for GPT-2).

**Offline mode** (after first run):
```bash
export HF_HUB_OFFLINE=1
python <script>.py
```

## Common Pitfalls
1. **Forgetting `return_full_text=False`** in pipelines → outputs include input text
2. **Not activating venv** → import errors or wrong Python version
3. **Skipping PROMPTS.md updates** → losing context on changes
4. **Committing model files** → check `.gitignore` excludes `*.bin`, `*.pt`, cache dirs

## When Adding Features
- Preserve educational comments explaining HuggingFace/LangChain concepts
- Add explicit TODOs for exploration areas (see [Inference-FinBERT.py](Inference-FinBERT.py#L3-L4))
- Document model sources and versions in PROMPTS.md for reproducibility
- Use descriptive variable names and progress logging
