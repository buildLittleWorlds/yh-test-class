# Week 2 Planning Guide

**Status:** Outline complete, ready for image generation

---

## Current Progress

- [x] Created `outline.md` with 18 slides
- [x] Created `package.json` for Slidev
- [x] Generate images using Nano Banana Pro
- [x] Create `slides.md` presentation
- [x] Update GitHub Action to build week-02
- [x] Test locally (build verified)
- [ ] Deploy (push to main)

---

## Nano Banana Pro Prompts

Copy each prompt below into Nano Banana Pro to generate the corresponding image. Save each image to `slidev/week-02/public/images/` with the filename shown.

---

### 1. `slide-04-clicking-vs-code.png`

```
Split diagram comparing two approaches:

LEFT SIDE - "Last Week: Clicking"
- Icon of a web browser with a play button
- Single input box
- One output at a time
- Label: "Manual, one by one"

RIGHT SIDE - "This Week: Code"
- Icon of a code editor/terminal
- List of multiple inputs
- Multiple outputs generated
- Label: "Automated, many at once"

Arrow from left to right showing progression.
Bottom text: "Code gives you POWER: batch processing, customization, automation"

Clean infographic style, two-column comparison. Educational diagram for middle/high school students learning AI.
```

---

### 2. `slide-05-colab-overview.png`

```
Diagram showing what Google Colab is:

Center: Large cloud icon labeled "Google's Computers"

Connected to cloud with lines:
- Your browser (laptop icon) with arrow labeled "You write code"
- GPU chip icon with label "Free AI processor"
- Google Drive icon with label "Auto-saves your work"
- GitHub icon with label "Connect your repos"

Bottom text: "A free cloud computer that runs in your browser"

Clean, friendly infographic style with simple icons. Educational diagram for students.
```

---

### 3. `slide-06-notebook-cells.png`


```
Diagram showing two types of notebook cells stacked vertically:

TOP CELL - "Markdown Cell"
- Light blue background
- Contains formatted text, headers, bullet points
- Label: "For explanations and notes"
- Icon: document/text icon

BOTTOM CELL - "Code Cell"
- Light gray background with code syntax
- Shows: print("Hello!")
- Below it: Output area showing "Hello!"
- Label: "For Python that actually runs"
- Icon: play button

Arrow between them showing: "Shift+Enter to run"

Clean notebook-style visual. Educational diagram for students learning to code.
```

---

### 4. `slide-07-python-basics.png`

```
Four-quadrant diagram showing Python basics:

QUADRANT 1 - "Variables"
my_name = "Alex"
Visual: Box labeled "my_name" containing "Alex"

QUADRANT 2 - "Lists"
favorites = ["pizza", "AI", "music"]
Visual: Three connected boxes containing the items

QUADRANT 3 - "Loops"
for thing in favorites:
    print(thing)
Visual: Arrow cycling through the list items

QUADRANT 4 - "f-strings"
f"I like {thing}!"
Visual: Template with slot showing variable insertion

Clean, educational diagram with code snippets and visual representations. For middle/high school students.
```

---

### 5. `slide-08-three-lines.png`

```
Diagram showing three lines of code with visual annotations:

Line 1: from transformers import pipeline
- Arrow pointing to: Hugging Face logo + "Get the AI toolbox"

Line 2: sentiment = pipeline("sentiment-analysis")
- Arrow pointing to: Download icon + model icon
- "Download a pre-trained AI model"

Line 3: sentiment("I love learning about AI!")
- Arrow pointing to: Input text → Model → Output
- Shows result: POSITIVE 99.9%

Visual flow from top to bottom, each line annotated with what it does.
Clean technical diagram style. Educational for students learning AI programming.
```

---

### 6. `slide-09-pipeline-breakdown.png`

```
Detailed diagram of what happens when you call an AI pipeline:

INPUT: "I love learning about AI!"

Step 1: TOKENIZE
- Text split into tokens: ["I", "love", "learning", "about", "AI", "!"]
- Convert to numbers: [1045, 2293, 4083, 2055, 4687, 999]

Step 2: MODEL
- Neural network icon processing the numbers
- Label: "Pre-trained on millions of examples"

Step 3: OUTPUT
- Raw scores → Softmax → Probabilities
- POSITIVE: 0.9998
- NEGATIVE: 0.0002

Arrow flow from top to bottom through each step.
Technical but accessible diagram for students learning how AI works internally.
```

---

### 7. `slide-10-output-explained.png`

```
Diagram decoding the pipeline output:

The output shown: [{'label': 'POSITIVE', 'score': 0.9998}]

Two callout boxes pointing to parts of the output:

BOX 1 - "label"
- POSITIVE or NEGATIVE
- "What the model thinks"
- Icon: thumbs up / thumbs down

BOX 2 - "score"
- 0 to 1 scale visualized as a meter/gauge
- 0.99 = "Very confident" (green zone)
- 0.51 = "Barely confident" (yellow zone)
- "How sure the model is"

Clean diagram with visual confidence meter. Educational for students.
```

---

### 8. `slide-11-batch-processing.png`

```
Split comparison diagram:

LEFT - "One at a time"
- Single text input box
- Arrow to model box
- Single output
- Clock icon showing: "Slow"

RIGHT - "Batch processing"
- List of 5 texts stacked vertically
- Single arrow to model box
- List of 5 outputs
- Lightning bolt icon showing: "Fast"

Code snippet at bottom:
texts = ["text1", "text2", "text3"]
results = sentiment(texts)  # All at once!

Label: "Code lets you process hundreds of inputs in seconds"

Clean infographic comparing the two approaches. Educational style.
```

---

### 9. `slide-12-pipeline-zoo.png`

```
Visual taxonomy of Hugging Face pipeline types:

Center hub: pipeline("task-name")

Radiating spokes to different task types arranged in a circle:

1. sentiment-analysis - Thumbs up/down icon - "Positive or negative?"
2. zero-shot-classification - Folder sorting icon - "Which category?"
3. question-answering - Question mark icon - "Find the answer"
4. summarization - Compress/shrink icon - "Make it shorter"
5. ner (Named Entity Recognition) - Highlight/marker icon - "Find names & places"
6. text-generation - Pencil/writing icon - "Continue writing"

Bottom label: "Same code pattern, different AI task"

Clean hub-and-spoke diagram with icons. Educational overview for students.
```

---

### 10. `slide-15-exploration-checklist.png`

```
Visual checklist styled like a mission card or quest:

Title: "YOUR EXPLORATION MISSION"

Checklist items with empty checkbox icons:

□ Try at least 3 pipeline types
□ Run the example code
□ Try your own inputs
□ Find something SURPRISING
□ Find something that BREAKS IT
□ Record observations in notebook

Visual elements: Magnifying glass icon, notebook icon, lightbulb icon

Bottom text: "Open your notebook for the full list of pipelines to try"

Clean mission-card style, engaging and fun for students. Gamified feel.
```

---

### 11. `slide-16-break-it.png`

```
Three-column challenge diagram styled like game challenge cards:

CHALLENGE 1 - "Trick Sentiment"
- Icon: confused robot face
- "Find 3 sentences that fool it"
- Examples listed: sarcasm, mixed feelings

CHALLENGE 2 - "Multi-Pipeline"
- Icon: multiple connected gears
- "Same text, different pipelines"
- "What does each one reveal?"

CHALLENGE 3 - "Chain Them"
- Icon: chain links
- "Generate text → Analyze it"
- "Output of one = Input of next"

Bottom banner: "AI models have patterns — find them!"

Engaging challenge-card style, like a game. Fun for students.
```

---

### 12. `slide-18-next-week.png`

```
Diagram previewing Week 3 concept, showing progression:

TOP SECTION: "This week: YOU write code"
- Person icon typing on keyboard
- Arrow pointing to code
- Code arrow pointing to AI model
- Results come back

BOTTOM SECTION: "Next week: AI writes code FOR you"
- Person icon talking/chatting
- Speech bubble going to ChatGPT/Claude icon
- AI generates code (code icon)
- Person reviews and uses it

Large arrow showing progression from top to bottom.

Code pattern box at bottom:
from transformers import pipeline
model = pipeline("task-name")
result = model("input")

Label: "Master this pattern — you'll use it constantly"

Clean progression diagram showing the learning journey.
```

---

## After Generating Images

### Step 1: Save Images
Save each generated image to:
```
slidev/week-02/public/images/
```

### Step 2: Create slides.md
Use the outline.md to build the Slidev presentation. Reference images as:
```markdown
![Description](/images/slide-XX-name.png)
```

Or for layouts:
```markdown
---
layout: image-right
image: /images/slide-XX-name.png
backgroundSize: contain
---
```

### Step 3: Update GitHub Action
Edit `.github/workflows/deploy-slides.yml` to add:

```yaml
- name: Build Week 02 slides
  working-directory: slidev/week-02
  run: |
    npm ci
    npx slidev build --base /yh-test-class/week-02/

# In the "Prepare deployment folder" step, add:
mv slidev/week-02/dist dist/week-02
```

### Step 4: Update READMEs
Update the slides table in:
- `slidev/README.md`
- Root `README.md`

Change Week 2 from "*Coming soon*" to the live link.

### Step 5: Test and Deploy
```bash
cd slidev/week-02
npm install
npm run dev  # Test locally at http://localhost:3030
```

Then commit and push to trigger deployment.

---

## Quick Reference

| Prompt # | Filename | Slide |
|----------|----------|-------|
| 1 | slide-04-clicking-vs-code.png | 4 |
| 2 | slide-05-colab-overview.png | 5 |
| 3 | slide-06-notebook-cells.png | 6 |
| 4 | slide-07-python-basics.png | 7 |
| 5 | slide-08-three-lines.png | 8 |
| 6 | slide-09-pipeline-breakdown.png | 9 |
| 7 | slide-10-output-explained.png | 10 |
| 8 | slide-11-batch-processing.png | 11 |
| 9 | slide-12-pipeline-zoo.png | 12 |
| 10 | slide-15-exploration-checklist.png | 15 |
| 11 | slide-16-break-it.png | 16 |
| 12 | slide-18-next-week.png | 18 |
