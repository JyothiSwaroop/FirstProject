#!/bin/bash
# Smart commit script: prompts for PROMPTS.md update before committing

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📝 Smart Commit with Prompt Logging${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if there are staged files
STAGED_FILES=$(git diff --cached --name-only)
if [ -z "$STAGED_FILES" ]; then
    echo -e "${RED}❌ No files staged for commit${NC}"
    echo "Use: git add <files>"
    exit 1
fi

# Show what's being committed
echo -e "${GREEN}Files staged for commit:${NC}"
echo "$STAGED_FILES" | sed 's/^/  • /'
echo ""

# Check if Python files are being committed
PYTHON_FILES=$(echo "$STAGED_FILES" | grep '\.py$' || true)

if [ -n "$PYTHON_FILES" ]; then
    echo -e "${YELLOW}📌 Python files detected!${NC}"
    echo ""
    
    # Prompt for documentation
    echo -e "${BLUE}What did you work on? (for PROMPTS.md)${NC}"
    read -p "Description: " PROMPT_NOTE
    
    if [ -n "$PROMPT_NOTE" ]; then
        # Add to PROMPTS.md
        python scripts/add-prompt.py --note "$PROMPT_NOTE"
        
        # Stage PROMPTS.md
        git add PROMPTS.md
        echo -e "${GREEN}✓ PROMPTS.md updated and staged${NC}"
        echo ""
    else
        echo -e "${YELLOW}⚠️  Skipping PROMPTS.md update${NC}"
    fi
fi

# Get commit message
echo -e "${BLUE}Commit message:${NC}"
read -p "> " COMMIT_MSG

if [ -z "$COMMIT_MSG" ]; then
    echo -e "${RED}❌ Commit message required${NC}"
    exit 1
fi

# Commit
git commit -m "$COMMIT_MSG"

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ Successfully committed!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "To push: git push"
