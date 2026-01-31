# Week 2 Slides: "Running Your First AI Models"

**Session Length:** 2 hours
**Total Slides:** 18

---

## Opening (2 slides)

### Slide 1 — Title
- "Running Your First AI Models"
- Subtitle: "From Clicking Buttons to Writing Code"
- Youth Horizons AI Program - Week 2

### Slide 2 — Today's Roadmap
- Visual timeline or icons:
  - Share & Review (15 min)
  - Introduction to Google Colab (20 min)
  - Your First Pipeline (25 min)
  - Explore Different Pipelines (30 min)
  - Challenge: Find the Limits (20 min)
  - Save & Reflect (10 min)

---

## Part 1: Share & Review (2 slides)

### Slide 3 — Quick Check-In
- "Share with the group:"
  - The most interesting AI tool you found
  - One limitation you discovered
- Discussion moment

### Slide 4 — Recall: The Pattern
- Last week: INPUT → [AI MODEL] → OUTPUT
- This week: You control this pattern with code
- "Why bother with code?"
  - Process many inputs at once
  - Customize how the model works
  - Combine models in creative ways
  - Build tools others can use
- **Image:** `images/slide-04-clicking-vs-code.png`

---

## Part 2: Introduction to Google Colab (3 slides)

### Slide 5 — What is Google Colab?
- "A free cloud computer in your browser"
- Why it's perfect for AI:
  - Free GPU (the processor AI needs)
  - No installation required
  - Saves automatically
  - Connects to GitHub
- **Image:** `images/slide-05-colab-overview.png`

### Slide 6 — How Notebooks Work
- Two types of cells:
  - **Markdown cells** — text and explanations
  - **Code cells** — Python that runs
- Key shortcuts:
  - Shift+Enter: Run and move to next
  - Ctrl+Enter: Run and stay
- "Cells run in order!"
- **Image:** `images/slide-06-notebook-cells.png`

### Slide 7 — Python Basics You'll Need
- Variables: `my_name = "Alex"`
- Lists: `favorites = ["pizza", "AI", "music"]`
- Loops: `for thing in favorites:`
- f-strings: `f"I like {thing}!"`
- → "Open your notebook to practice"
- **Image:** `images/slide-07-python-basics.png`

---

## Part 3: Your First Pipeline (4 slides)

### Slide 8 — The Magic Three Lines
- Show the code:
  ```python
  from transformers import pipeline
  sentiment = pipeline("sentiment-analysis")
  sentiment("I love learning about AI!")
  ```
- "This downloads a real AI model and runs it"
- **Image:** `images/slide-08-three-lines.png`

### Slide 9 — What Just Happened?
- Line 1: Import the toolbox from Hugging Face
- Line 2: Create a sentiment analysis tool (downloads model)
- Line 3: Run it on your text
- Output: `[{'label': 'POSITIVE', 'score': 0.9998}]`
- **Image:** `images/slide-09-pipeline-breakdown.png`

### Slide 10 — Understanding the Output
- **label**: POSITIVE or NEGATIVE
- **score**: Confidence (0 to 1)
  - 0.99 = 99% confident
  - 0.51 = barely confident
- → "Try your own sentences in the notebook"
- **Image:** `images/slide-10-output-explained.png`

### Slide 11 — The Power of Code: Many Inputs
- Process a whole list at once:
  ```python
  texts = ["I love this!", "This is terrible.", "Meh."]
  results = sentiment(texts)
  ```
- "Try sentences that might trick it:"
  - Sarcasm: "Oh great, another Monday"
  - Mixed feelings: "Food was good, service was slow"
  - Neutral: "The sky is blue"
- **Image:** `images/slide-11-batch-processing.png`

---

## Part 4: Explore Different Pipelines (4 slides)

### Slide 12 — The Pipeline Zoo
- Sentiment analysis is just ONE type
- Many more to explore:
  - Zero-Shot Classification
  - Question Answering
  - Summarization
  - Named Entity Recognition
  - Text Generation
- "Same pattern, different task"
- **Image:** `images/slide-12-pipeline-zoo.png`

### Slide 13 — Zero-Shot Classification
- "Classify text into categories YOU define"
- Example:
  ```python
  classifier("I need to finish my homework")
  categories = ["school", "sports", "food"]
  ```
- "Even categories it wasn't trained on!"
- Use cases: Sorting emails, categorizing feedback
- → "Try in notebook"

### Slide 14 — Question Answering
- "Answer questions from a passage of text"
- You provide: context + question
- Model returns: answer + confidence
- Use cases: Customer support, document search
- → "Try in notebook"

### Slide 15 — Your Exploration Mission
- Try at least 3 different pipeline types
- For each one:
  1. Run the example code
  2. Try your own inputs
  3. Find something surprising
  4. Find something that breaks it
- Record observations in your notebook
- **Image:** `images/slide-15-exploration-checklist.png`

---

## Part 5: Challenge - Find the Limits (2 slides)

### Slide 16 — Challenge: Break the Models
- Challenge 1: Find 3 sentences that trick sentiment analysis
- Challenge 2: Run one paragraph through multiple pipelines
  - What does each reveal?
- Challenge 3: Chain pipelines together
  - Generate text → Analyze its sentiment
- "AI models have patterns — find them!"
- **Image:** `images/slide-16-break-it.png`

### Slide 17 — Discussion: What Did You Find?
- "What kinds of inputs caused problems?"
- Common failure modes:
  - Sarcasm and irony
  - Mixed sentiments
  - Context-dependent meaning
  - Unusual formatting
- "These limitations matter for real applications"

---

## Part 6: Wrap-up (1 slide)

### Slide 18 — Save & Look Ahead
- Save your notebook to GitHub:
  - File > Download > .ipynb
  - Upload to your `ai-explorer` repo
- Next week: **AI as Your Coding Partner**
  - Use ChatGPT/Claude to write code FOR you
  - Understand and modify what they create
- Code pattern to remember:
  ```python
  from transformers import pipeline
  model = pipeline("task-name")
  result = model("your input")
  ```
- **Image:** `images/slide-18-next-week.png`

---

## Slide Count Summary

| Section | Slides |
|---------|--------|
| Opening | 1-2 |
| Part 1: Share & Review | 3-4 |
| Part 2: Google Colab | 5-7 |
| Part 3: First Pipeline | 8-11 |
| Part 4: Explore Pipelines | 12-15 |
| Part 5: Challenge | 16-17 |
| Part 6: Wrap-up | 18 |
| **Total** | **18 slides** |

---

## Images to Generate

| Slide | File | Purpose |
|-------|------|---------|
| 4 | `slide-04-clicking-vs-code.png` | Visual comparison: GUI vs code control |
| 5 | `slide-05-colab-overview.png` | What Colab is and why it's useful |
| 6 | `slide-06-notebook-cells.png` | Markdown vs Code cells explained |
| 7 | `slide-07-python-basics.png` | Variables, lists, loops visual reference |
| 8 | `slide-08-three-lines.png` | The 3-line code with visual annotations |
| 9 | `slide-09-pipeline-breakdown.png` | What each line does step by step |
| 10 | `slide-10-output-explained.png` | Label + Score output decoded |
| 11 | `slide-11-batch-processing.png` | One input vs many inputs comparison |
| 12 | `slide-12-pipeline-zoo.png` | Overview of all pipeline types |
| 15 | `slide-15-exploration-checklist.png` | Visual checklist for exploration |
| 16 | `slide-16-break-it.png` | Challenge modes illustrated |
| 18 | `slide-18-next-week.png` | Preview of AI coding partner concept |

---

## Diagram Generation Prompts

### Slide 4 — Clicking vs Code
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

Clean infographic style, two-column comparison.
```

### Slide 5 — Google Colab Overview
```
Diagram showing what Google Colab is:

Center: Large cloud icon labeled "Google's Computers"

Connected to cloud:
- Your browser (laptop icon) with arrow labeled "You write code"
- GPU chip icon with label "Free AI processor"
- Google Drive icon with label "Auto-saves your work"
- GitHub icon with label "Connect your repos"

Bottom text: "A free cloud computer that runs in your browser"

Clean, friendly infographic style with icons.
```

### Slide 6 — Notebook Cells Explained
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

Clean notebook-style visual.
```

### Slide 7 — Python Basics Visual Reference
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

Clean, educational diagram with code snippets and visual representations.
```

### Slide 8 — The Magic Three Lines
```
Diagram showing the three lines of code with visual annotations:

Line 1: from transformers import pipeline
- Arrow pointing to: Hugging Face logo + "Get the AI toolbox"

Line 2: sentiment = pipeline("sentiment-analysis")
- Arrow pointing to: Download icon + model icon
- "Download a pre-trained AI model"

Line 3: sentiment("I love learning about AI!")
- Arrow pointing to: Input text → Model → Output
- Shows result: POSITIVE 99.9%

Visual flow from top to bottom, each line annotated.
Clean technical diagram style.
```

### Slide 9 — Pipeline Breakdown (What Happens Inside)
```
Detailed diagram of what happens when you call a pipeline:

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
Technical but accessible diagram.
```

### Slide 10 — Output Explained
```
Diagram decoding the pipeline output:

The output: [{'label': 'POSITIVE', 'score': 0.9998}]

Two callout boxes:

BOX 1 - "label"
- POSITIVE or NEGATIVE
- "What the model thinks"
- Icon: thumbs up / thumbs down

BOX 2 - "score"
- 0 to 1 scale visualized as a meter/gauge
- 0.99 = "Very confident" (green zone)
- 0.51 = "Barely confident" (yellow zone)
- "How sure the model is"

Clean diagram with visual confidence meter.
```

### Slide 11 — Batch Processing Power
```
Split comparison diagram:

LEFT - "One at a time"
- Single text input
- Arrow to model
- Single output
- Clock icon: "Slow"

RIGHT - "Batch processing"
- List of 5 texts stacked
- Single arrow to model
- List of 5 outputs
- Lightning icon: "Fast"

Code snippet at bottom:
texts = ["text1", "text2", "text3"]
results = sentiment(texts)  # All at once!

Label: "Code lets you process hundreds of inputs in seconds"
```

### Slide 12 — The Pipeline Zoo
```
Visual taxonomy of Hugging Face pipeline types:

Center hub: "pipeline('task-name')"

Radiating spokes to different task types:

1. sentiment-analysis - Thumbs up/down icon - "Positive or negative?"
2. zero-shot-classification - Folder sorting icon - "Which category?"
3. question-answering - Question mark icon - "Find the answer"
4. summarization - Compress icon - "Make it shorter"
5. ner (Named Entity Recognition) - Highlight icon - "Find names & places"
6. text-generation - Pencil icon - "Continue writing"

Bottom label: "Same code pattern, different AI task"

Clean hub-and-spoke diagram with icons.
```

### Slide 15 — Exploration Checklist
```
Visual checklist/mission card style:

Title: "YOUR EXPLORATION MISSION"

Checklist items with checkbox icons:

□ Try at least 3 pipeline types
□ Run the example code
□ Try your own inputs
□ Find something SURPRISING
□ Find something that BREAKS IT
□ Record observations

Visual elements: Magnifying glass, notebook, lightbulb icons

Bottom: "Open your notebook for the full list of pipelines to try"

Clean mission-card style, engaging for students.
```

### Slide 16 — Break the Models
```
Three-column challenge diagram:

CHALLENGE 1 - "Trick Sentiment"
- Icon: confused face
- "Find 3 sentences that fool it"
- Examples: sarcasm, mixed feelings

CHALLENGE 2 - "Multi-Pipeline"
- Icon: multiple gears
- "Same text, different pipelines"
- "What does each reveal?"

CHALLENGE 3 - "Chain Them"
- Icon: chain links
- "Generate text → Analyze it"
- "Output of one = Input of next"

Bottom banner: "AI models have patterns — find them!"

Engaging challenge-card style.
```

### Slide 18 — Next Week Preview
```
Diagram previewing Week 3 concept:

TOP: "This week: YOU write code"
- Person typing code
- Code goes to AI model
- Results come back

BOTTOM: "Next week: AI writes code FOR you"
- Person talking to ChatGPT/Claude icon
- AI generates code
- Person reviews and uses it

Arrow showing progression from manual coding to AI-assisted coding.

Code pattern box:
from transformers import pipeline
model = pipeline("task-name")
result = model("input")

Label: "Master this pattern — you'll use it constantly"
```

---

## Teaching Notes

- Slides are for **concepts and demos** — keep them visual
- Notebook is for **hands-on coding** — students work there
- Expect the first pipeline load to take 1-2 minutes (downloading model)
- Have students share screen when they get interesting results
- Common issues:
  - Forgetting to run cells in order
  - Colab disconnecting (just reconnect and re-run)
  - Typos in code (encourage copy-paste for now)
