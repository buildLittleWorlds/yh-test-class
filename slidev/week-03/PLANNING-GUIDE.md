# Week 3 Planning Guide

**Status:** Outline complete, ready for image generation

---

## Current Progress

- [x] Created `outline.md` with 20 slides
- [x] Created `package.json` for Slidev
- [ ] Generate images using Nano Banana Pro
- [ ] Create `slides.md` presentation
- [ ] Update GitHub Action to build week-03
- [ ] Test locally
- [ ] Deploy

---

## Nano Banana Pro Prompts

Copy each prompt below into Nano Banana Pro to generate the corresponding image. Save each image to `slidev/week-03/public/images/` with the filename shown.

---

### 1. `slide-04-big-idea.png`

```
Diagram showing the four steps of working with AI to code:

Four connected boxes in a horizontal flow with arrows between them:

BOX 1: "KNOW"
- Icon: lightbulb or brain
- Text below: "What you want to build"

BOX 2: "ASK"
- Icon: chat bubble with code symbols
- Text below: "AI to write the code"

BOX 3: "UNDERSTAND"
- Icon: magnifying glass over code
- Text below: "What the AI wrote"

BOX 4: "MODIFY"
- Icon: pencil/edit tool
- Text below: "To do what YOU want"

Large arrow underneath spanning all four, labeled: "This is how programmers work in 2026"

Clean, modern infographic style. Educational diagram for middle/high school students learning to code with AI.
```

---


### 2. `slide-05-ai-assistants.png`

```
Diagram showing three AI coding assistants side by side:

THREE CARDS arranged horizontally:

CARD 1 - "ChatGPT"
- OpenAI logo or chat icon
- URL: chat.openai.com
- Label: "Most popular"

CARD 2 - "Claude"
- Anthropic logo or assistant icon
- URL: claude.ai
- Label: "Great at code"

CARD 3 - "HuggingChat"
- Hugging Face logo (yellow face emoji style)
- URL: huggingface.co/chat
- Label: "Free & open source"

Bottom text: "Open one of these in another tab now!"

Clean card-style design with distinct colors for each. Educational style for students.
```

---

### 3. `slide-06-clear-framework.png`

```
Visual breakdown of the CLEAR framework for code prompts:

Vertical list with large letters on the left and explanations on the right:

C - CONTEXT
"I'm working in Google Colab..."
Icon: computer/environment

L - LANGUAGE/LIBRARIES
"Using Python and transformers..."
Icon: code brackets or library books

E - EXPLAIN THE GOAL
"I want to analyze sentiment of reviews..."
Icon: target/bullseye

A - ASK SPECIFICALLY
"Write a function called analyze_reviews that..."
Icon: checklist

R - REQUIREMENTS
"Include comments, handle errors..."
Icon: settings gear

The letters C-L-E-A-R stacked vertically spell out the word clearly.
Each letter is a different color for visual distinction.

Clean educational diagram, mnemonic style. For students learning prompt engineering.
```

---

### 4. `slide-07-bad-vs-good.png`

```
Split comparison diagram - Bad vs Good code prompts:

LEFT SIDE - "BAD PROMPT" (red tint)
- Speech bubble containing: "Write code that does sentiment analysis"
- X mark icon
- Problems listed below:
  - No context
  - No specifics
  - No requirements
- Result: Confused robot icon

RIGHT SIDE - "GOOD PROMPT" (green tint)
- Speech bubble containing abbreviated CLEAR prompt:
  "I'm working in Google Colab with Python.
   Using transformers, write a function
   called analyze_reviews that takes a list
   and returns sentiment for each..."
- Checkmark icon
- Benefits listed below:
  - Clear context
  - Specific request
  - Defined output
- Result: Happy robot with code

Arrow or VS symbol between the two sides.
Clean comparison infographic style. Educational for students.
```

---

### 5. `slide-09-text-analyzer.png`

```
Flow diagram showing what the Text Analyzer tool does:

INPUT (top):
Large text box containing a sample paragraph icon
Label: "Any paragraph of text"

Arrow down to CENTER PROCESSING:
Box labeled "TEXT ANALYZER" with three branching arrows going to:

OUTPUT (three boxes at bottom):

BOX 1 - "SENTIMENT"
- Thumbs up/down icons
- "Positive or Negative?"
- Confidence score meter

BOX 2 - "SUMMARY"
- Compress/shrink icon
- "1-2 sentences"
- Document becoming smaller

BOX 3 - "ENTITIES"
- Highlight/tag icons
- "People, Places, Orgs"
- Example: "Elon Musk, SpaceX, California"

All three outputs flow to a final "FORMATTED DISPLAY" box at the bottom.

Clean technical flow diagram. Shows the multi-pipeline tool concept.
```

---

### 6. `slide-13-challenge-options.png`

```
Four challenge option cards arranged in a 2x2 grid:

CARD A - "REVIEW ANALYZER" (blue)
- Icon: star rating / review stars
- Bullet points:
  - Analyze product reviews
  - Calculate overall sentiment
  - Find best & worst reviews
- Difficulty: ★★☆

CARD B - "HOMEWORK HELPER" (green)
- Icon: graduation cap / book
- Bullet points:
  - Summarize any topic
  - Extract key facts
  - Generate quiz questions
- Difficulty: ★★☆

CARD C - "STORY STARTER" (purple)
- Icon: pencil / creative writing
- Bullet points:
  - Generate story openings
  - Analyze mood of each
  - Continue your favorite
- Difficulty: ★★★

CARD D - "YOUR IDEA" (orange)
- Icon: lightbulb / question mark
- Bullet points:
  - What do YOU want?
  - Discuss with instructor
  - Get creative!
- Difficulty: ???

Clean card-style design like game/quest cards. Engaging for students.
```

---

### 7. `slide-15-debug-iterate.png`

```
Workflow diagram for debugging AI-generated code:

TWO PATHS shown:

PATH 1 - "IF IT BREAKS" (left side, red to green flow)
Step 1: Error message icon with red X
Step 2: Arrow to "Copy the error"
Step 3: Arrow to chat bubble "Paste to AI: 'I got this error:'"
Step 4: Arrow to "AI suggests fix"
Step 5: Arrow to green checkmark "Try again!"

PATH 2 - "IF YOU WANT CHANGES" (right side, yellow flow)
Step 1: Code icon with pencil
Step 2: Arrow to "Describe what's different"
Step 3: Arrow to chat bubble "Be specific: 'Change X to do Y'"
Step 4: Arrow to "AI modifies code"
Step 5: Arrow to sparkle icon "Improved!"

Bottom banner: "Iteration is normal — even pros do this constantly!"

Clean workflow diagram style. Shows debugging as a positive process.
```

---

### 8. `slide-16-code-detective.png`

```
Visual showing how to read and understand code:

CENTER: Large magnifying glass over a code snippet

Around the magnifying glass, four detective questions in callout boxes:

BOX 1 (top left): "What does it DO?"
- Icon: question mark
- Arrow pointing to function name in code

BOX 2 (top right): "What goes IN?"
- Icon: input arrow
- Arrow pointing to parameters in code

BOX 3 (bottom left): "What comes OUT?"
- Icon: output arrow
- Arrow pointing to return statement in code

BOX 4 (bottom right): "What's a better NAME?"
- Icon: name tag
- Arrow pointing to function name

Title at top: "CODE DETECTIVE"
Subtitle: "Read code like you're solving a mystery"

The code snippet shows a simple function structure (blurred/simplified).
Detective/mystery theme with clean educational style.
```

---

### 9. `slide-20-next-week.png`

```
Diagram showing three specialization tracks for Weeks 4-6:

Title at top: "PICK YOUR PATH"
Subtitle: "Weeks 4-6: Specialization"

THREE TRACK CARDS arranged horizontally:

TRACK A - "TEXT & LANGUAGE" (blue)
- Icon: chat bubbles / text document
- Build: Chatbots, writing tools, Q&A bots
- Skills: NLP pipelines, conversation design
- Example projects listed

TRACK B - "IMAGES & VISION" (green)
- Icon: camera / image frame
- Build: Photo tools, art generators, detectors
- Skills: Vision models, image processing
- Example projects listed

TRACK C - "CREATIVE AI" (purple)
- Icon: palette / magic wand
- Build: Story generators, game AI, creative tools
- Skills: Combining models, creative applications
- Example projects listed

Bottom text: "Think about which excites YOU most!"

All three paths converge at bottom to "PROJECT PHASE (Weeks 7-9)"

Clean path/journey style diagram. Exciting and inviting for students choosing their direction.
```

---

## After Generating Images

### Step 1: Save Images
Save each generated image to:
```
slidev/week-03/public/images/
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
- name: Build Week 03 slides
  working-directory: slidev/week-03
  run: |
    npm ci
    npx slidev build --base /yh-test-class/week-03/

# In the "Prepare deployment folder" step, add:
mv slidev/week-03/dist dist/week-03
```

### Step 4: Update READMEs
Update the slides table in:
- `slidev/README.md`
- Root `README.md`

Change Week 3 from "*Coming soon*" to the live link.

### Step 5: Test and Deploy
```bash
cd slidev/week-03
npm install
npm run dev  # Test locally at http://localhost:3030
```

Then commit and push to trigger deployment.

---

## Quick Reference

| Prompt # | Filename | Slide |
|----------|----------|-------|
| 1 | slide-04-big-idea.png | 4 |
| 2 | slide-05-ai-assistants.png | 5 |
| 3 | slide-06-clear-framework.png | 6 |
| 4 | slide-07-bad-vs-good.png | 7 |
| 5 | slide-09-text-analyzer.png | 9 |
| 6 | slide-13-challenge-options.png | 13 |
| 7 | slide-15-debug-iterate.png | 15 |
| 8 | slide-16-code-detective.png | 16 |
| 9 | slide-20-next-week.png | 20 |

---

## External Links to Include in Slides

These links create interactive opportunities during class:

| Slide | Link | Description |
|-------|------|-------------|
| 5 | https://chat.openai.com | ChatGPT - have students open |
| 5 | https://claude.ai | Claude - alternative option |
| 5 | https://huggingface.co/chat/ | HuggingChat - free option |
| 9 | https://huggingface.co/tasks/text-classification | Sentiment analysis demo |
| 9 | https://huggingface.co/tasks/summarization | Summarization demo |
| 9 | https://huggingface.co/tasks/token-classification | NER demo |

**Usage in class:**
- Slide 5: Students open their preferred AI assistant
- Slide 9: Show demos of the pipelines they'll be using, then build same functionality in code
- Links bridge the "clicking" from Week 1 → "code" from Week 2 → "AI-assisted code" in Week 3
