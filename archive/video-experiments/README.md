# Youth Horizons Video Experiments

This folder contains a Remotion project for creating instructional videos to supplement the Youth Horizons curriculum notebooks.

## What is Remotion?

[Remotion](https://www.remotion.dev/) is an open-source framework for creating videos programmatically using React. Instead of dragging timelines in video editors, you write code — each frame is a React component.

## Why Remotion for This Curriculum?

The curriculum teaches students to build with code. Creating instructional videos *with code* is a natural fit:

- **Animated diagrams** — The INPUT → MODEL → OUTPUT pattern, pipeline flows
- **Code walkthroughs** — Syntax highlighting, step-by-step reveals
- **Consistent branding** — Reusable components across all videos
- **Version controlled** — Videos are code, stored in git
- **AI-assisted** — Claude Code can help generate and iterate on videos

## Setup

### Prerequisites

- Node.js 20+
- npm
- ffmpeg (for rendering): `brew install ffmpeg`
- Claude Code CLI (optional, for AI-assisted creation)

### Initialize the Project

```bash
cd video-experiments
./setup.sh
```

When prompted:
- Choose **Blank** template (use arrow keys to navigate)
- Enable TailwindCSS: **Yes**

### Development

```bash
cd remotion-project
npm run dev

# Open http://localhost:3000 in your browser
```

### Rendering

```bash
cd remotion-project

# Render a specific composition
npx remotion render <CompositionName> out/video.mp4

# Example
npx remotion render InputModelOutput out/input-model-output.mp4
```

## Project Structure (After Initialization)

```
video-experiments/
├── README.md                  # This file
├── VIDEO-IDEAS.md             # Detailed video concepts
├── CLAUDE-PROMPTS.md          # Sample prompts for Claude Code
├── setup.sh                   # Setup script
└── remotion-project/          # The actual Remotion project
    ├── src/
    │   ├── Composition.tsx    # Your video compositions
    │   └── Root.tsx           # Composition registry
    ├── public/                # Static assets (images, fonts)
    ├── out/                   # Rendered videos
    └── package.json
```

## Video Specifications

Default settings for Youth Horizons videos:

| Setting | Value |
|---------|-------|
| Resolution | 1920x1080 (1080p) |
| Frame Rate | 30 fps |
| Duration | 60-180 seconds per concept |
| Format | MP4 (H.264) |

## Workflow

1. **Identify a concept** from the notebooks that would benefit from animation
2. **Sketch the flow** — what visual sequence explains this concept?
3. **Create components** — build reusable pieces (code blocks, arrows, boxes)
4. **Compose the video** — arrange components with timing
5. **Preview and iterate** — use Remotion Studio for real-time feedback
6. **Render** — export final MP4

## Using Claude Code

With Remotion skills installed, you can prompt Claude Code naturally:

```
Create a 90-second video that explains the INPUT → MODEL → OUTPUT pattern.
Start with the text "Every AI follows the same pattern" then animate
three examples: text→ChatGPT→text, image→classifier→labels, audio→Whisper→text.
```

Claude Code will generate the React components and timing.

## Related Files

- `VIDEO-IDEAS.md` — Detailed concepts for potential videos
- `../notebooks/` — Source curriculum notebooks
- `../slides/week-01/` — Existing slide content and diagrams
- `../diagrams/` — Excalidraw source files

## Resources

- [Remotion Documentation](https://www.remotion.dev/docs)
- [Remotion + Claude Code Guide](https://www.remotion.dev/docs/ai/claude-code)
- [claude-remotion-kickstart](https://github.com/jhartquist/claude-remotion-kickstart) — Starter kit with pre-built components
