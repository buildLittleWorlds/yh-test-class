# Video Ideas for Youth Horizons

Concepts from the curriculum that are well-suited for animated Remotion videos.

---

## Priority 1: Core Concepts (Week 1-2)

These are foundational ideas that every student needs to understand. Animation helps make abstract concepts concrete.

### Video 1: The AI Pattern

**Source:** Week 1, Part 1 / Slides 3-4
**Duration:** 60-90 seconds
**Concept:** Every AI tool follows INPUT → MODEL → OUTPUT

**Storyboard:**

1. **0:00-0:05** — Title: "The Secret Pattern Behind Every AI"
2. **0:05-0:15** — Fade in three boxes: INPUT | MODEL | OUTPUT with arrows connecting
3. **0:15-0:25** — First example animates in:
   - "What's the weather?" types into INPUT
   - Arrow pulses through MODEL (labeled "ChatGPT")
   - "It's sunny and 72°F" appears in OUTPUT
4. **0:25-0:35** — Second example (image generation):
   - "A castle in the clouds" → DALL-E → [image fades in]
5. **0:35-0:45** — Third example (speech-to-text):
   - [waveform icon] → Whisper → "Hello, how are you?"
6. **0:45-0:55** — Fourth example (classification):
   - [cat photo] → Classifier → "Cat: 94%"
7. **0:55-0:60** — All four stack vertically, pattern highlighted
8. **0:60-0:65** — Text: "Every AI. Same pattern. Different task."

**Components needed:**
- AnimatedBox (with typing effect for text)
- Arrow (with pulse animation)
- ImagePlaceholder (for generated images)
- WaveformIcon (for audio)

---

### Video 2: How Pipelines Work

**Source:** Week 2, Parts 3-4 / Slide 19
**Duration:** 90-120 seconds
**Concept:** What happens when you run `pipeline("sentiment-analysis")`

**Storyboard:**

1. **0:00-0:10** — Title: "3 Lines of Code, A Lot Happening Underneath"
2. **0:10-0:25** — Line 1 appears with syntax highlighting:
   ```python
   from transformers import pipeline
   ```
   Arrow points to annotation: "Get the toolbox from Hugging Face"
   Visual: Hugging Face logo, packages flowing in
3. **0:25-0:45** — Line 2 appears:
   ```python
   classifier = pipeline("sentiment-analysis")
   ```
   Annotation: "Pick a specific tool"
   Visual: Dropdown showing different pipeline types
   Sub-visual: Model downloading animation (progress bar)
4. **0:45-1:10** — Line 3 appears:
   ```python
   classifier("I love learning about AI!")
   ```
   Visual breakdown of what happens:
   - Text enters → Tokenizer splits into tokens
   - Tokens → Numbers (embeddings)
   - Numbers flow through neural network (simplified)
   - Output: POSITIVE 99.8%
5. **1:10-1:20** — Zoom out to show all three lines together
6. **1:20-1:30** — End card: "That's it. You just ran an AI model."

**Components needed:**
- CodeBlock (with line-by-line reveal)
- TokenizerAnimation (text → tokens → numbers)
- NeuralNetworkSimple (abstract flowing nodes)
- ConfidenceBar (animated percentage)

---

### Video 3: Pattern Matching vs Understanding

**Source:** Week 1, Part 3 / Slides 11-13
**Duration:** 60-90 seconds
**Concept:** AI matches patterns but doesn't "understand" like humans

**Storyboard:**

1. **0:00-0:10** — Title: "The Understanding Gap"
2. **0:10-0:25** — Split screen: Human brain vs Neural network
   - Human side: "Sees a photo of a birthday party"
   - AI side: Same photo
3. **0:25-0:40** — Human thought bubbles appear:
   - "Someone's celebrating!"
   - "That cake looks homemade"
   - "The kid on the left looks jealous"
   - "This was probably taken by a parent"
4. **0:40-0:55** — AI analysis appears:
   - "cake: 98%"
   - "people: 4 detected"
   - "indoor scene"
   - "balloons: present"
5. **0:55-1:05** — Highlight the gap:
   - Human: Meaning, emotion, context, story
   - AI: Labels, counts, categories
6. **1:05-1:15** — Key insight text: "AI = incredibly talented mimics"
7. **1:15-1:25** — "They reproduce patterns. They don't know what patterns mean."

**Components needed:**
- SplitScreen (human vs AI comparison)
- ThoughtBubble (animated appearance)
- LabelTag (classification output style)
- GapHighlight (visual showing the divide)

---

## Priority 2: Skill-Building Concepts (Week 2-3)

### Video 4: Why Detail Matters in Prompts

**Source:** Week 1, Slides 7-8
**Duration:** 45-60 seconds
**Concept:** More specific prompts = more predictable results

**Storyboard:**

1. **0:00-0:05** — Title: "Why Details Matter"
2. **0:05-0:15** — Wide funnel with "a cat" — many different cat silhouettes inside
3. **0:15-0:25** — Medium funnel: "fluffy orange cat on windowsill" — fewer options
4. **0:25-0:35** — Narrow funnel: full detailed prompt — single specific result
5. **0:35-0:45** — Bottom text: "More detail = Fewer possibilities = More control"

**Components needed:**
- AnimatedFunnel (narrows with more detail)
- Silhouettes (cat variations)
- PromptText (appears as funnel narrows)

---

### Video 5: Common AI Failure Modes

**Source:** Week 1, Experiments 3
**Duration:** 60-75 seconds
**Concept:** Why AI struggles with hands, text, and contradictions

**Storyboard:**

1. **0:00-0:05** — Title: "Where AI Gets Confused"
2. **0:05-0:20** — Hands section:
   - Show training data concept: hands in many positions
   - Result: "hand-like shapes" not "exactly 5 fingers"
3. **0:20-0:35** — Text in images section:
   - Show font variety in training
   - Result: letter shapes, not spelling rules
4. **0:35-0:50** — Contradictions section:
   - "Square circle" prompt
   - "No training examples of impossible things"
5. **0:50-0:60** — Summary: "AI learned patterns, not rules"

**Components needed:**
- TrainingDataMontage (quick image flashes)
- FailureExample (garbled hands/text)
- ImpossibleShape (animated confusion)

---

## Priority 3: Account Setup Guides

### Video 6: GitHub Account Setup

**Source:** Week 1, Part 5
**Duration:** 120-180 seconds
**Concept:** Step-by-step GitHub account creation and first repo

This would be a **screencast-style** video with annotations, better suited for screen recording than pure Remotion animation. Consider using Remotion for intro/outro with screen recording in between.

---

### Video 7: Google Colab Orientation

**Source:** Week 2, Part 2
**Duration:** 90-120 seconds
**Concept:** What is Colab, how cells work, keyboard shortcuts

Similar to Video 6 — hybrid screencast + animated overlays.

---

## Priority 4: Track-Specific Teasers (Week 4)

Short videos (30-45 seconds each) previewing each specialization track.

### Video 8: Text Track Teaser
- Quick demos of sentiment analysis, zero-shot classification, summarization
- "Turn text into insights"

### Video 9: Images Track Teaser
- Image classification, object detection, captioning
- "Teach computers to see"

### Video 10: Creative Track Teaser
- Text generation, style control, multi-modal
- "Create with AI as your partner"

---

## Production Notes

### Branding Elements

- **Font:** Inter or similar clean sans-serif
- **Colors:**
  - Primary: #7C3AED (purple, matches Hugging Face)
  - Secondary: #10B981 (green for success/positive)
  - Accent: #F59E0B (orange for highlights)
  - Background: #1F2937 (dark gray) or #FFFFFF (light)
- **Logo:** Youth Horizons program logo (if exists)
- **End card:** "Youth Horizons AI Researcher Program"

### Audio Considerations

Remotion can sync to audio tracks. Options:
1. **No audio** — Used as silent visual aids during live instruction
2. **Music only** — Background track, no narration
3. **Narrated** — Voiceover explaining each step (requires script + recording)

For initial experiments, recommend starting with **no audio** (silent visual aids).

### Reusable Components to Build First

1. **TitleSlide** — Consistent opening for all videos
2. **EndCard** — Program branding + "Next: [topic]"
3. **CodeBlock** — Syntax-highlighted, line-by-line reveal
4. **Arrow** — Animated connector with optional pulse
5. **AnimatedBox** — Container that can hold text/images, animates in
6. **SplitScreen** — Side-by-side comparison layout

Building these first enables rapid production of multiple videos.

---

## Suggested Starting Point

**Start with Video 1: The AI Pattern**

Reasons:
- Most foundational concept
- Simple visual structure (boxes + arrows)
- Reusable components (AnimatedBox, Arrow)
- Short duration (60-90 sec)
- Tests the full workflow without complexity

Once Video 1 works, the components carry forward to Videos 2-5.
