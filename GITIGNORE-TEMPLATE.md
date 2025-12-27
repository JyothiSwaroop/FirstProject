# Python ML Project - Git Setup Template

## Overview
This guide provides a standard `.gitignore` configuration for Python machine learning projects to avoid committing large model files, virtual environments, and cache data.

## Standard .gitignore for Python ML Projects

```gitignore
.DS_Store

# Virtual Environment
ai_env/
venv/
env/
ENV/
.venv/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Model files and cache
models/
*.bin
*.pt
*.pth
*.onnx
*.h5
*.pkl
*.safetensors

# Hugging Face cache
.cache/
huggingface/
transformers_cache/

# Jupyter Notebook
.ipynb_checkpoints

# Distribution / packaging
build/
dist/
*.egg-info/
```

## Setup Instructions

### 1. Initial Repository Setup

```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize git repository
git init

# Create .gitignore file
touch .gitignore

# Copy the standard template above into .gitignore
```

### 2. Verify What Will Be Committed

```bash
# Check current git status
git status

# List currently tracked files
git ls-files

# Check if large files are being ignored
git status --ignored
```

### 3. Add and Commit Only Scripts

```bash
# Add specific files/directories
git add *.py
git add scripts/
git add requirements.txt
git add README.md

# Or add all (gitignore will filter)
git add .

# Commit changes
git commit -m "Initial commit - scripts only"
```

### 4. Push to GitHub

```bash
# Add remote repository
git remote add origin https://github.com/username/repository.git

# Push changes
git push -u origin main
```

## What Gets Excluded

| Category | Files/Folders | Reason |
|----------|---------------|--------|
| **Environment** | `ai_env/`, `venv/`, etc. | Virtual environments are recreated locally |
| **Models** | `*.bin`, `*.pt`, `*.safetensors` | Large files (GBs), downloaded from HuggingFace |
| **Cache** | `__pycache__/`, `.cache/` | Generated files, not source code |
| **HuggingFace** | `transformers_cache/` | Downloaded model cache |

## What Gets Committed

✓ Python scripts (`.py` files)  
✓ `requirements.txt`  
✓ Documentation (`README.md`, `PROMPTS.md`)  
✓ Configuration files  
✓ Small data samples (if any)  

## Workflow for New Projects

1. **Create project directory**
2. **Copy this `.gitignore` template**
3. **Initialize git**: `git init`
4. **Create virtual environment**: `python -m venv ai_env`
5. **Activate environment**: `source ai_env/bin/activate`
6. **Install dependencies**: `pip install -r requirements.txt`
7. **Add scripts to git**: `git add .`
8. **Commit**: `git commit -m "Initial commit"`
9. **Push to GitHub**

## Common Scenarios

### Accidentally Committed Large Files

```bash
# Remove from git but keep locally
git rm --cached models/*.bin

# Commit the removal
git commit -m "Remove model files from git"
```

### Check Repository Size

```bash
# Check size of .git directory
du -sh .git

# List largest files in git history
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {print substr($0,6)}' | \
  sort --numeric-sort --key=2 | \
  tail -n 10
```

### Update Existing Repository

If you already have a repo without proper `.gitignore`:

```bash
# Add the .gitignore
# Then remove cached files
git rm -r --cached .

# Re-add everything (gitignore will filter)
git add .

# Commit
git commit -m "Apply .gitignore and remove unwanted files"
```

## Benefits

- **Faster cloning**: Repositories stay small (<10MB vs GBs)
- **Easier collaboration**: Team members download models locally
- **Clean history**: No large binary files in git history
- **GitHub friendly**: Avoid file size limits (100MB per file)

## Notes

- Model files should be downloaded from HuggingFace Hub
- Virtual environments recreated with: `pip install -r requirements.txt`
- Document model names/versions in README.md
- Consider using Git LFS for essential large files (if needed)
