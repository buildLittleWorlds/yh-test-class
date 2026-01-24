# Week 1 Slides: "What's Possible with AI?"

**Session Length:** 2 hours
**Total Slides:** 19

---

## Opening (2 slides)

### Slide 1 — Title
- "What's Possible with AI?"
- Subtitle: "Explore, Discover, Get Inspired"
- Youth Horizons AI Program - Week 1

### Slide 2 — Today's Roadmap
- Visual timeline or icons:
  - What is AI? (15 min)
  - Explore Image AI together (30 min)
  - Discussion: How does it work? (15 min)
  - Independent exploration (30 min)
  - Account setup (15 min)
  - Share & reflect (15 min)

---

## Part 1: What is AI? (3 slides)

### Slide 3 — The Big Secret
- "AI isn't magic."
- Diagram: INPUT → [AI MODEL] → OUTPUT
- **Image:** `images/slide-03-input-model-output.png`

### Slide 4 — Examples of the Pattern
- Text → ChatGPT → More text
- Text → DALL-E → Image
- Audio → Whisper → Text
- Image → Classifier → Labels
- *Every AI tool follows this pattern*
- **Image:** To generate — see prompts below

### Slide 5 — Discussion Question
- Large text: "What's something you think AI probably CAN'T do well?"
- "We'll revisit this at the end of class."

---

## Part 2: Image AI Exploration (5 slides)

### Slide 6 — Let's Explore: Image Generation
- Big link: [Stable Diffusion 3.5](https://huggingface.co/spaces/stabilityai/stable-diffusion-3.5-large)
- "We'll try this together"

### Slide 7 — Experiment 1: Adding Detail
- Three prompts to try:
  1. `a cat`
  2. `a fluffy orange cat sitting on a windowsill`
  3. `a fluffy orange cat sitting on a windowsill, golden hour lighting, photograph`
- Question: "How does adding detail change the result?"
- **Image:** To generate — see prompts below

### Slide 8 — Experiment 2: Style Matters
- Same subject, different styles:
  - `a robot, photograph`
  - `a robot, oil painting, renaissance style`
  - `a robot, anime style`
  - `a robot, pencil sketch`
- **Image:** To generate — see prompts below

### Slide 9 — Experiment 3: Breaking It
- "Try to confuse the AI:"
  - Contradictions: `a square circle`
  - Abstract: `the feeling of Monday morning`
  - Text: `a sign that says HELLO WORLD`
  - Hands: `a person waving with five fingers`
- "What fails? Why?"
- **Image:** To generate — see prompts below

### Slide 10 — Now the Other Direction: Image Understanding
- Big link: [Florence-2](https://huggingface.co/spaces/gokaygokay/Florence-2)
- Backup link: [Image Captioning Spaces](https://huggingface.co/spaces?sort=likes&search=image+caption)
- Tasks to try: Caption, Detailed Caption, Object Detection
- "Upload your own photo!"

---

## Part 3: Discussion (3 slides)

### Slide 11 — Let's Figure This Out
- Question 1: "Why does more detail = better results?"
- Question 2: "Why does AI struggle with hands and text?"
- Question 3: "Can AI understand *why* a photo is funny?"

### Slide 12 — The Key Insight
- Diagram: Human Understanding vs AI Pattern Matching
- "The Understanding Gap"
- **Image:** `images/slide-12-understanding-gap.png` (Excalidraw version)
- **Alt:** `images/slide-12-understanding-gap-gemini.png` (Gemini version)

### Slide 13 — Remember This
- "AI = incredibly talented mimics"
- "They reproduce patterns they've seen"
- "They don't know what those patterns *mean*"
- **Image:** To generate — see prompts below

---

## Part 4: Independent Exploration (2 slides)

### Slide 14 — Your Mission
- "Visit at least 6 AI tools"
- "Spend 3-4 minutes with each"
- "Find their limits — what breaks them?"
- "Rate and take notes"
- → "Open your notebook for the list and note-taking tables"

### Slide 15 — The Categories
- Mind map or visual showing:
  - Text & Language (Chatbot Arena, HuggingChat, Summarizer)
  - Audio & Speech (Whisper, Edge TTS)
  - Images (Segment Anything, Depth Estimation, Face Analysis)
  - Wild Cards (You discover!)
- **Image:** To generate — see prompts below

---

## Part 5: Account Setup (2 slides)

### Slide 16 — GitHub: Your Portfolio Home
- Logo + link: [github.com](https://github.com)
- "Choose your username carefully — it's permanent!"
- Good: `maya-builds`, `alex-ai`
- Avoid: birth years, gamertags
- → "Follow detailed steps in your notebook"

### Slide 17 — Hugging Face: Home of AI Models
- Logo + link: [huggingface.co](https://huggingface.co)
- "You'll use this constantly"
- → "Follow steps in notebook"

---

## Part 6: Wrap-up (2 slides)

### Slide 18 — Share & Reflect
- "Each person shares:"
  - ONE tool that impressed you
  - ONE thing AI couldn't do
- "Then complete reflection questions in your notebook"

### Slide 19 — Next Week Preview
- "You'll run AI models yourself — with code"
- Show the 3-line code snippet:
  ```python
  from transformers import pipeline
  classifier = pipeline("sentiment-analysis")
  classifier("I love learning about AI!")
  ```
- "That's it. See you next week!"
- **Image:** To generate — see prompts below

---

## Slide Count Summary

| Section | Slides |
|---------|--------|
| Opening | 1-2 |
| Part 1: What is AI? | 3-5 |
| Part 2: Image AI | 6-10 |
| Part 3: Discussion | 11-13 |
| Part 4: Exploration | 14-15 |
| Part 5: Account Setup | 16-17 |
| Part 6: Wrap-up | 18-19 |
| **Total** | **19 slides** |

---

## Images

### Existing Images
| Slide | File | Description |
|-------|------|-------------|
| 3 | `images/slide-03-input-model-output.png` | INPUT → MODEL → OUTPUT diagram |
| 12 | `images/slide-12-understanding-gap.png` | Pattern matching vs understanding (Excalidraw) |
| 12 | `images/slide-12-understanding-gap-gemini.png` | Pattern matching vs understanding (Gemini) |

### Images to Generate
| Slide | File to create | Purpose |
|-------|----------------|---------|
| 4 | `slide-04-examples.png` | Concrete examples of the AI pattern |
| 7 | `slide-07-detail-funnel.png` | Why more detail = better results |
| 8 | `slide-08-style-branches.png` | How style words affect output |
| 9 | `slide-09-failure-modes.png` | Why AI struggles with hands, text, contradictions |
| 13 | `slide-13-training-inference.png` | How AI actually learns (training vs using) |
| 15 | `slide-15-categories.png` | AI tool landscape taxonomy |
| 19 | `slide-19-pipeline-code.png` | What the 3-line code actually does |

---

## Diagram Generation Prompts

### Slide 4 — Examples of the Pattern
```
Diagram showing four parallel examples of the AI pattern, each as a simple flowchart:

Row 1: "What's the weather?" → [ChatGPT] → "It's sunny and 72°F"
Row 2: "A castle in the clouds" → [DALL-E] → [small image icon]
Row 3: [audio waveform icon] → [Whisper] → "Hello, how are you?"
Row 4: [photo icon] → [Classifier] → "Cat: 94%, Orange tabby"

Align them vertically to emphasize the shared INPUT → MODEL → OUTPUT structure.
Clean diagram style, labels clearly readable.
```

### Slide 7 — Why Detail Matters
```
Diagram showing how prompt specificity narrows possibilities:

Left side: Wide funnel labeled "a cat" containing many different cat images (silhouettes or simple icons showing variety - different colors, poses, settings)

Middle: Medium funnel labeled "a fluffy orange cat on a windowsill" with fewer, more similar options

Right side: Narrow funnel labeled "fluffy orange cat, windowsill, golden hour, photograph" pointing to one specific outcome

Arrow across the bottom: "More detail = Fewer possibilities = More predictable result"

Clean infographic style.
```

### Slide 8 — How Style Words Work
```
Diagram showing how the same subject + different styles = different outputs:

Center: "a robot" (the constant subject)

Four branches leading to four boxes:
- "photograph" → realistic robot image style
- "oil painting, renaissance" → classical painting style
- "anime" → anime/manga style
- "pencil sketch" → hand-drawn sketch style

Label at bottom: "Style words tell the model which patterns to use"

Clean diagram, simple visual representations of each style.
```

### Slide 9 — Where AI Struggles (and Why)
```
Diagram explaining why AI fails at certain things:

Three columns:

Column 1 - "Hands"
- Icon: hand with wrong number of fingers
- Below: "Hands appear in many positions/angles in training data"
- "Model learned 'hand-like shapes' not 'exactly 5 fingers'"

Column 2 - "Text in Images"
- Icon: garbled text on a sign
- Below: "Letters vary hugely in fonts, sizes, angles"
- "Model learned letter-like shapes, not spelling rules"

Column 3 - "Contradictions"
- Icon: "square circle" with question mark
- Below: "No training examples of impossible things"
- "Model can't combine patterns that don't exist"

Clean infographic style, educational.
```

### Slide 13 — How AI Actually Learns
```
Two-part diagram showing AI training vs. usage:

TOP - "Training" (happens once, before you use it):
Millions of images with labels → [Neural Network] → Learns patterns (edges, textures, shapes, objects)

BOTTOM - "Using" (what happens when you give it a prompt):
Your prompt → [Trained Model looks for matching patterns] → Combines patterns into output

Key insight box: "The model doesn't 'understand' cats - it learned which pixel patterns usually appear together in images labeled 'cat'"

Clean technical diagram, arrows showing flow.
```

### Slide 15 — AI Tool Landscape
```
Organized diagram of AI tool categories:

Four quadrants or branches:

TEXT & LANGUAGE
- Chatbots (conversation)
- Summarization (long → short)
- Classification (categorize text)
- Translation (language → language)

AUDIO & SPEECH
- Speech-to-Text (transcription)
- Text-to-Speech (synthesis)
- Voice cloning
- Music generation

IMAGES
- Generation (text → image)
- Captioning (image → text)
- Segmentation (identify objects)
- Editing (modify images)

MULTIMODAL
- Vision + Language (VQA)
- Audio + Text
- Video understanding

Clean taxonomy diagram, shows the breadth of what AI can do.
```

### Slide 19 — What the Code Actually Does
```
Diagram breaking down the 3 lines of code:

Line 1: "from transformers import pipeline"
Arrow pointing to: "Get the toolbox from Hugging Face"

Line 2: "classifier = pipeline('sentiment-analysis')"
Arrow pointing to: "Pick a specific tool (sentiment = positive/negative feeling)"
Show: Downloads model, tokenizer, config

Line 3: "classifier('I love learning about AI!')"
Arrow pointing to: "Run it on your text"
Show: Text → [Tokenize] → [Model] → [Decode] → "POSITIVE: 99%"

Bottom label: "Three lines, but a lot happens underneath"

Technical but accessible diagram.
```

---

## Teaching Notes

- Slides are for **concepts and links** — keep them visual
- Notebook is for **doing and note-taking** — students work there
- Typical rhythm: Show slide (30 sec - 2 min) → Activity (5-15 min) → Next slide
- Have both windows ready for quick switching during Zoom
