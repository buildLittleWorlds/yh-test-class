# Week 3 Slides: "AI as Your Coding Partner"

**Session Length:** 2 hours
**Total Slides:** 20

---

## Opening (2 slides)

### Slide 1 — Title
- "AI as Your Coding Partner"
- Subtitle: "Using ChatGPT and Claude to Build Things"
- Youth Horizons AI Program - Week 3

### Slide 2 — Today's Roadmap
- Visual timeline:
  - Review: What pipelines did you try? (10 min)
  - How to Prompt for Code (20 min)
  - Guided: Building a Mini Tool (25 min)
  - Challenge: Build Your Own Tool (30 min)
  - Reading & Modifying AI Code (25 min)
  - Share & Reflect (10 min)

---

## Part 1: Review & Setup (2 slides)

### Slide 3 — Quick Review
- "What pipelines did you explore last week?"
  - Sentiment? Summarization? NER? Text generation?
- "Any cool failures you found?"
- Discussion moment

### Slide 4 — Today's Big Idea
- "You DON'T need to memorize Python syntax"
- The four steps:
  1. Know what you want to build
  2. Ask AI to write the code
  3. Understand what the AI wrote
  4. Modify it to do what YOU want
- "This is how professional programmers work in 2026"
- **Image:** `images/slide-04-big-idea.png`

---

## Part 2: How to Prompt for Code (4 slides)

### Slide 5 — The AI Assistants
- Three tools you can use (open one now):
  - ChatGPT - chat.openai.com
  - Claude - claude.ai
  - HuggingChat - huggingface.co/chat (free!)
- "Open one in another tab"
- **Image:** `images/slide-05-ai-assistants.png`
- **Links:** ChatGPT, Claude, HuggingChat

### Slide 6 — The CLEAR Framework
- When asking AI to write code, use CLEAR:
  - **C** - Context (environment, what you're building)
  - **L** - Language/Libraries (Python, transformers, etc.)
  - **E** - Explain the goal (what should it do?)
  - **A** - Ask specifically (function names, inputs, outputs)
  - **R** - Requirements (comments, formatting, extras)
- **Image:** `images/slide-06-clear-framework.png`

### Slide 7 — Bad vs Good Prompt
- **Bad prompt:**
  - "Write code that does sentiment analysis"
  - What's wrong: No context, no details, no requirements
- **Good prompt:**
  - "I'm working in Google Colab with Python. Using the Hugging Face transformers library, write a function called analyze_reviews that..."
  - Shows the full CLEAR structure
- "Which will give better results?"
- **Image:** `images/slide-07-bad-vs-good.png`

### Slide 8 — Practice: Write Your Prompt
- Task: You want code that:
  1. Summarizes a paragraph
  2. Finds all people/places/organizations
  3. Displays everything nicely
- "Fill in the CLEAR framework in your notebook"
- "Share with a classmate — how could you make it clearer?"

---

## Part 3: Guided - Building a Mini Tool (4 slides)

### Slide 9 — Our Goal: Text Analyzer
- We'll build a tool that:
  - Takes any paragraph
  - Analyzes sentiment (positive/negative)
  - Summarizes it
  - Finds named entities (people, places, orgs)
  - Displays results nicely
- **Image:** `images/slide-09-text-analyzer.png`

### Slide 10 — Step 1: Ask AI for the Code
- Show the prompt we'll use
- "Go to your AI assistant and paste this prompt"
- → ChatGPT / Claude / HuggingChat link
- "Copy what it gives you into your notebook"

### Slide 11 — Step 2-3: Run & Understand
- Run it — did it work?
- Common issues:
  - Missing `!pip install`
  - Model name typos
  - Indentation errors
- "Let's go through what the AI wrote together"
- Discussion: imports, pipelines, function structure

### Slide 12 — Step 4: Ask AI to Modify It
- Now ask the AI:
  - "Modify the function to also count words"
  - "Classify the text into: news, opinion, story, educational"
  - "Use emoji for results"
- "The AI can iterate! Ask for changes."

---

## Part 4: Challenge - Build Your Own Tool (3 slides)

### Slide 13 — Pick Your Challenge
- **Option A: Review Analyzer**
  - Analyze product/movie reviews, give star rating
- **Option B: Homework Helper**
  - Summarize, extract key facts, generate quiz questions
- **Option C: Story Starter**
  - Generate story openings, analyze mood, continue favorite
- **Option D: Your Own Idea**
  - What do YOU want to build?
- **Image:** `images/slide-13-challenge-options.png`

### Slide 14 — Build Time!
- Write your prompt using CLEAR
- Ask AI to generate the code
- Copy to notebook and run
- Test and iterate!
- "You have 25 minutes — GO!"

### Slide 15 — Debug & Iterate
- If something doesn't work:
  1. Copy the error message
  2. Paste to AI with "I got this error:"
  3. Ask it to fix the code
- If it works but you want changes:
  - Describe what you want different
  - Be specific: "Change X to do Y instead"
- **Image:** `images/slide-15-debug-iterate.png`

---

## Part 5: Reading & Modifying AI Code (3 slides)

### Slide 16 — Code Detective
- Being able to READ code is just as important
- Show mystery_function code snippet
- Questions to ask yourself:
  - What does this function do?
  - What input does it expect?
  - What does it return?
  - What would be a better name?
- **Image:** `images/slide-16-code-detective.png`

### Slide 17 — Modify Without AI Help
- Challenge: Modify the mystery_function yourself
  - Add a new category
  - Count additional things
  - Add a warning condition
- "Try yourself first, then use AI if stuck"
- This builds real understanding!

### Slide 18 — Ask Good Questions About Code
- When you see code you don't understand:
  - "What does this line do?"
  - "Explain the f-string"
  - "What's the difference between X and Y?"
- AI is great at explaining code!
- Use it to learn, not just to generate

---

## Part 6: Wrap-up (2 slides)

### Slide 19 — Save & Reflect
- Save notebook to GitHub
- Reflection questions:
  - Most important thing about prompting?
  - Confidence rating (1-5)?
  - What would you build with more time?
  - What's still confusing?

### Slide 20 — Next Week: Pick Your Path!
- Weeks 4-6: Specialization tracks
  - **Text & Language** — Chatbots, writing tools, Q&A
  - **Images & Vision** — Photo tools, art generation, detection
  - **Creative AI** — Story generators, game AI, creative tools
- "Think about which excites you most!"
- The CLEAR framework + debugging workflow
- **Image:** `images/slide-20-next-week.png`

---

## Slide Count Summary

| Section | Slides |
|---------|--------|
| Opening | 1-2 |
| Part 1: Review | 3-4 |
| Part 2: Prompting for Code | 5-8 |
| Part 3: Building Mini Tool | 9-12 |
| Part 4: Challenge | 13-15 |
| Part 5: Reading Code | 16-18 |
| Part 6: Wrap-up | 19-20 |
| **Total** | **20 slides** |

---

## Images to Generate

| Slide | File | Purpose |
|-------|------|---------|
| 4 | `slide-04-big-idea.png` | The four steps: Know → Ask → Understand → Modify |
| 5 | `slide-05-ai-assistants.png` | ChatGPT, Claude, HuggingChat logos/icons |
| 6 | `slide-06-clear-framework.png` | CLEAR framework visual breakdown |
| 7 | `slide-07-bad-vs-good.png` | Bad vs good prompt comparison |
| 9 | `slide-09-text-analyzer.png` | What the text analyzer does (flow diagram) |
| 13 | `slide-13-challenge-options.png` | Four challenge options as cards |
| 15 | `slide-15-debug-iterate.png` | Debug and iterate workflow |
| 16 | `slide-16-code-detective.png` | Code reading/detective visual |
| 20 | `slide-20-next-week.png` | Three specialization tracks preview |

---

## External Links for Slides

**Priority links to include (interactive opportunities):**

| Slide | Link | Purpose |
|-------|------|---------|
| 5 | https://chat.openai.com | ChatGPT |
| 5 | https://claude.ai | Claude |
| 5 | https://huggingface.co/chat/ | HuggingChat (free option) |
| 9 | https://huggingface.co/tasks/text-classification | Sentiment demo |
| 9 | https://huggingface.co/tasks/summarization | Summarization demo |
| 9 | https://huggingface.co/tasks/token-classification | NER demo |

Students can try the demos during class, then build the same capabilities in code.

---

## Teaching Notes

- This week is more discussion-heavy — students need AI assistants open
- Have everyone confirm they can access at least one AI tool before Part 2
- The CLEAR framework is the key takeaway — reference it throughout
- Expect varied code from different AI assistants — that's okay!
- Debugging is a natural part of the process — normalize it
- Part 5 (reading code) is important for building real understanding
- End with excitement about choosing tracks next week
