#!/bin/bash
# Setup git hooks for automatic prompt logging

HOOK_FILE=".git/hooks/pre-commit"

echo "Setting up git pre-commit hook..."

cat > "$HOOK_FILE" << 'EOF'
#!/bin/bash
# Pre-commit hook: Remind to update PROMPTS.md when committing Python files

# Get staged Python files
PYTHON_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$' || true)

if [ -n "$PYTHON_FILES" ]; then
    # Check if PROMPTS.md is staged
    PROMPTS_STAGED=$(git diff --cached --name-only | grep 'PROMPTS.md' || true)
    
    if [ -z "$PROMPTS_STAGED" ]; then
        echo ""
        echo "⚠️  WARNING: Python files are being committed but PROMPTS.md is not updated!"
        echo ""
        echo "Python files in this commit:"
        echo "$PYTHON_FILES" | sed 's/^/  • /'
        echo ""
        echo "Consider updating PROMPTS.md:"
        echo "  python scripts/add-prompt.py --note \"Your description\""
        echo "  git add PROMPTS.md"
        echo ""
        echo "Or use the smart commit script:"
        echo "  bash scripts/commit-with-prompt.sh"
        echo ""
        
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Commit cancelled."
            exit 1
        fi
    fi
fi

exit 0
EOF

chmod +x "$HOOK_FILE"
chmod +x scripts/commit-with-prompt.sh

echo "✓ Git hooks installed successfully!"
echo ""
echo "The pre-commit hook will now:"
echo "  • Detect when you commit Python files"
echo "  • Remind you to update PROMPTS.md"
echo "  • Prevent accidental commits without documentation"
echo ""
echo "Quick usage:"
echo "  bash scripts/commit-with-prompt.sh  # Interactive commit with prompt logging"
echo ""
