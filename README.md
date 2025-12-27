## Text Generation Inference

This project demonstrates text generation using Hugging Face `transformers` with the `gpt2` model.

### Prerequisites
- macOS
- Python virtual environment located at `ai_env/` (provided)

### Setup
1. Activate the virtual environment:

```bash
cd /Users/jyothiswaroop/AI-ML/FirstProject
source ai_env/bin/activate
```

2. Install dependencies (pinned for reproducibility):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Run
Execute the text generation script:

```bash
python Inference-TextGeneration.py
```

On the first run, the `gpt2` model will be downloaded and cached.

### Optional
- Offline run after first download:

```bash
export HF_HUB_OFFLINE=1
python Inference-TextGeneration.py
```

- Deactivate the environment:

```bash
deactivate
```

### Files
- `Inference-TextGeneration.py`: Main script that seeds and generates text for two prompts using `gpt2`.
- `requirements.txt`: Pinned dependencies for reproducible installs.
 - `PROMPTS.md`: Log of session prompts (what you asked) and script input prompts (what the model generates from).

### Prompt Logging CLI
Use the helper to append prompts to `PROMPTS.md`:

```bash
source ai_env/bin/activate
python scripts/add-prompt.py --note "Your new prompt or change note"
```

Optional flags:
- `--link "+ affected file or URL"`
- `--section "Script Input Prompts"` to categorize entries


### Maintaining Prompts
- Log new requests or iterations in `PROMPTS.md` under a dated heading.
- Add any new generation prompts you introduce in the script to the "Script Input Prompts" section.
- For larger changes, include a short note and link the affected file.
