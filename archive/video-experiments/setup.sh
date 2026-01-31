#!/bin/bash

# Youth Horizons Video Experiments Setup Script

echo "Setting up Remotion video project..."

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is required. Install from https://nodejs.org/"
    exit 1
fi

# Check Node version (need 20+)
NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 20 ]; then
    echo "Warning: Node.js 20+ recommended. You have $(node -v)"
fi

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Warning: ffmpeg not found. Install it for rendering:"
    echo "  macOS: brew install ffmpeg"
    echo "  Ubuntu: sudo apt install ffmpeg"
fi

# Initialize Remotion project in the remotion-project subfolder
if [ ! -f "remotion-project/package.json" ]; then
    echo ""
    echo "Initializing Remotion project in ./remotion-project..."
    echo ""
    echo "When prompted:"
    echo "  - Choose 'Blank' template (use arrow keys)"
    echo "  - Enable TailwindCSS: Yes"
    echo ""
    npx create-video@latest remotion-project
else
    echo "remotion-project/package.json exists, skipping project creation"
fi

# Install dependencies
if [ -f "remotion-project/package.json" ]; then
    echo ""
    echo "Installing dependencies..."
    cd remotion-project && npm install && cd ..
fi

# Install Remotion skills for Claude Code (optional)
echo ""
read -p "Install Remotion skills for Claude Code? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cd remotion-project && npx skills add remotion-dev/skills && cd ..
fi

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "  1. cd remotion-project"
echo "  2. npm run dev"
echo "  3. Open http://localhost:3000"
echo "  4. See ../VIDEO-IDEAS.md for concepts to build"
echo ""
