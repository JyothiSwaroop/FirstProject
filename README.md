## AI Inference Project

This project demonstrates text generation and other AI inference tasks using Hugging Face `transformers`. It includes both command-line scripts and an interactive web interface similar to ChatGPT.

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

### Web UI (Recommended)
Launch the interactive chat interface for testing different inferences:

```bash
python app.py
```

For development with debug mode enabled:
```bash
FLASK_DEBUG=true python app.py
```

Then open your browser to `http://localhost:5000`

Features:
- ChatGPT-like interface for interactive testing
- Support for multiple inference types (Text Generation, Sentiment Analysis)
- Configurable seed for reproducible results
- Adjustable max tokens for text generation
- Real-time inference testing with different prompts

### Command Line Scripts
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
- `app.py`: Flask web server with chat interface for interactive inference testing
- `templates/index.html`: ChatGPT-like web UI for testing different inference models
- `Inference-TextGeneration.py`: Command-line script for text generation with `gpt2`
- `inference.py`: Command-line script for sentiment analysis
- `requirements.txt`: Pinned dependencies for reproducible installs
- `PROMPTS.md`: Log of session prompts (what you asked) and script input prompts (what the model generates from)

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
