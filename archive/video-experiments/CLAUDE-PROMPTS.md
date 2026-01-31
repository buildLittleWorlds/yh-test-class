# Claude Code Prompts for Video Creation

Sample prompts to use with Claude Code once Remotion is set up and skills are installed.

---

## Getting Started

After running `setup.sh` and starting the dev server (`npm run dev`), use these prompts in Claude Code.

---

## Video 1: The AI Pattern

### Initial Creation

```
Create a new Remotion composition called "InputModelOutput" that explains
the INPUT → MODEL → OUTPUT pattern for AI.

The video should be:
- 1920x1080 resolution
- 30fps
- About 60-90 seconds (1800-2700 frames)

Structure:
1. Title slide (2 seconds): "The Secret Pattern Behind Every AI"
2. Show three boxes: INPUT → MODEL → OUTPUT (3 seconds to animate in)
3. First example (5 seconds):
   - "What's the weather?" appears in INPUT box
   - Arrow pulses to MODEL box labeled "ChatGPT"
   - "It's sunny and 72°F" appears in OUTPUT
4. Second example (5 seconds): text prompt → DALL-E → image icon
5. Third example (5 seconds): audio waveform → Whisper → transcribed text
6. Final frame (3 seconds): "Every AI. Same pattern. Different task."

Use a dark background (#1F2937) with white text and purple (#7C3AED) accents.
```

### Iteration Prompts

```
Make the arrows animate with a pulsing glow effect when data flows through them.
```

```
Add a subtle fade-in for each example instead of instant appearance.
```

```
The text in the INPUT box should have a typing animation effect.
```

---

## Video 2: How Pipelines Work

### Initial Creation

```
Create a composition called "PipelineFlow" that shows what happens when you
run this Python code:

from transformers import pipeline
classifier = pipeline("sentiment-analysis")
classifier("I love learning about AI!")

Make it 90 seconds. Show each line appearing with syntax highlighting, then
animate what's happening underneath:

Line 1: Show the Hugging Face logo and "toolbox" visual
Line 2: Show a model downloading (progress bar), then the classifier ready
Line 3: Break down the flow: text → tokenizer → neural network → output

End with "POSITIVE: 99.8%" animating in with a green progress bar.

Use the same dark theme as other videos. Code should use a monospace font
with Python syntax colors.
```

---

## Video 3: Pattern Matching vs Understanding

```
Create a composition called "UnderstandingGap" showing the difference between
human understanding and AI pattern matching.

Split screen layout:
- Left side: Human brain icon
- Right side: Neural network icon

Both see the same image (represent as a polaroid/photo frame).

Animate thought bubbles on the human side:
- "Someone's celebrating!"
- "That cake looks homemade"
- "The kid looks jealous"

Animate labels on the AI side:
- "cake: 98%"
- "people: 4"
- "indoor: true"

End with text: "AI matches patterns. Humans understand meaning."

60 seconds total.
```

---

## Reusable Components

### Create Core Components First

```
Create a reusable TitleSlide component that takes:
- title (string)
- subtitle (optional string)
- duration in frames (default 90)

It should fade in the title, then the subtitle, centered on screen.
Use Inter font, white text on dark background.
```

```
Create a reusable CodeBlock component that:
- Takes an array of code lines
- Reveals them one at a time with syntax highlighting
- Supports Python syntax colors
- Has configurable timing per line
```

```
Create an AnimatedArrow component that:
- Draws itself from left to right
- Has an optional pulse/glow effect
- Can be horizontal or have slight curves
- Takes color and thickness as props
```

---

## Rendering Commands

Once compositions are ready:

```bash
# Preview in browser
npm run dev

# Render to MP4
npx remotion render InputModelOutput out/input-model-output.mp4

# Render at specific quality
npx remotion render InputModelOutput out/video.mp4 --crf 18

# Render just a portion (frames 0-300)
npx remotion render InputModelOutput out/test.mp4 --frames=0-300
```

---

## Tips for Good Prompts

1. **Be specific about timing** — "3 seconds" or "90 frames" is clearer than "a moment"
2. **Describe the visual structure** — "split screen", "centered", "bottom-third"
3. **Reference existing components** — "Use the TitleSlide component we created"
4. **Iterate in small steps** — Get the basic structure, then refine animations
5. **Ask for previews** — "Show me a still frame at the 5-second mark"
