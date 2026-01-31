# Youth Horizons Level 2 Curriculum - Build Notes

**Created:** January 16, 2026
**Updated:** January 17, 2026
**Instructor:** Dr. Daniel Plate
**Program:** Youth Horizons AI Researcher Program - Level 2

---

## Overview

This curriculum teaches 7th-11th grade students to use AI/ML tools through a **"Guided Discovery with Choice"** approach. Instead of linear lectures, students explore, specialize in areas that interest them, and build personal projects.

### Key Design Principles

1. **Exploration before instruction** - Try things first, explain concepts after
2. **Student choice creates engagement** - Pick your own track and project
3. **AI-assisted coding** - Use ChatGPT/Claude to write code, focus on understanding and modifying
4. **Project-driven learning** - Build something that's YOURS
5. **Natural differentiation** - Same materials work for G7-11 through depth of exploration
6. **Portfolio outcome** - GitHub repo with notebooks + working project

### Course Structure

- **Duration:** 12 weeks, 2-hour sessions
- **Format:** Google Colab notebooks (designed for full 2-hour engagement)
- **Compensation:** $200/session
- **Class size:** 5-6 students
- **Platform:** Google Classroom for materials

---

## Curriculum Arc: Four Phases

```
Phase 1 (Weeks 1-3):  EXPLORATION    → Try everything, find your interests
Phase 2 (Weeks 4-6):  SPECIALIZATION → Pick a track, go deeper
Phase 3 (Weeks 7-9):  PROJECT        → Build something that's yours
Phase 4 (Weeks 10-12): SHOWCASE      → Polish and present
```

---

## Phase 1: Exploration (Weeks 1-3)

**Theme: "What's possible? What interests YOU?"**

### Week 1: What's Possible with AI?
**File:** `notebooks/week-01-whats-possible.ipynb`

| Time | Activity |
|------|----------|
| 0:00-0:15 | Introductions & What is AI? |
| 0:15-0:45 | Guided Exploration: Image AI |
| 0:45-1:00 | Discussion: How does this work? |
| 1:00-1:30 | Independent Exploration |
| 1:30-1:45 | Account Setup (GitHub, HuggingFace) |
| 1:45-2:00 | Share & Reflect |

**Key Activities:**
- Structured exploration of HF Spaces with note-taking
- Try to "break" AI tools - find their limits
- Create GitHub account and `ai-explorer` repo
- Identify top 3 favorite AI tools

---

### Week 2: Running Your First Models
**File:** `notebooks/week-02-running-models.ipynb`

| Time | Activity |
|------|----------|
| 0:00-0:15 | Share & Review |
| 0:15-0:35 | Introduction to Google Colab |
| 0:35-1:00 | Guided: First Pipeline (Sentiment) |
| 1:00-1:30 | Exploration: Different Pipelines |
| 1:30-1:50 | Challenge: Find the Limits |
| 1:50-2:00 | Save & Reflect |

**Pipelines Introduced:**
- `pipeline("sentiment-analysis")`
- `pipeline("zero-shot-classification")`
- `pipeline("question-answering")`
- `pipeline("summarization")`
- `pipeline("ner")`
- `pipeline("text-generation")`

---

### Week 3: AI as Your Coding Partner
**File:** `notebooks/week-03-ai-coding-partner.ipynb`

| Time | Activity |
|------|----------|
| 0:00-0:10 | Review |
| 0:10-0:30 | How to Prompt for Code (CLEAR Framework) |
| 0:30-0:55 | Guided: Building a Mini Tool |
| 0:55-1:25 | Challenge: Build Your Own Tool |
| 1:25-1:50 | Reading & Modifying AI Code |
| 1:50-2:00 | Share & Reflect |

**Key Skills:**
- CLEAR prompting framework (Context, Language, Explain, Ask, Requirements)
- Debug with AI help
- Read and modify AI-generated code

---

## Phase 2: Specialization (Weeks 4-6)

**Theme: "Go deeper in what interests you."**

### Week 4: Pick Your Path
**File:** `notebooks/week-04-pick-your-path.ipynb`

| Time | Activity |
|------|----------|
| 0:00-0:10 | Introduction to Tracks |
| 0:10-0:40 | Sample: Text & Language Track |
| 0:40-1:10 | Sample: Images & Vision Track |
| 1:10-1:40 | Sample: Creative AI Track |
| 1:40-1:55 | Choose Your Track + Brainstorm |
| 1:55-2:00 | Share & Setup |

Students try a mini-project from each track, then choose one.

---

### Weeks 5-6: Track Deep Dives

Students work through the notebook for their chosen track:

**Track A: Text & Language**
**File:** `notebooks/week-05-06-track-text.ipynb`

Topics:
- Emotion detection (beyond sentiment)
- Zero-shot classification
- Question answering systems
- Summarization + key information extraction
- Combining models

**Track B: Images & Vision**
**File:** `notebooks/week-05-06-track-images.ipynb`

Topics:
- Image classification deep dive
- Zero-shot image classification
- Image captioning
- Combining vision capabilities
- Building photo tools

**Track C: Creative AI**
**File:** `notebooks/week-05-06-track-creative.ipynb`

Topics:
- Controlling text generation (temperature, top-p)
- Genre-aware writing
- Mood-matched content
- Multi-modal creation (image to story)
- Building creative tools

---

## Phase 3: Project Building (Weeks 7-9)

**Theme: "Make something that's YOURS."**

**File:** `notebooks/week-07-09-project-phase.ipynb`

### Week 7: Define & Prototype
- Fill out project spec
- Load required models
- Build MVP (simplest working version)
- Document what works

### Week 8: Build & Iterate
- Get feedback from classmate
- Improve based on feedback
- Add nice formatting
- Handle edge cases

### Week 9: Polish & Prepare
- Final polish
- Create demo examples
- Write README
- Upload to GitHub
- Practice presentation

---

## Phase 4: Showcase (Weeks 10-12)

**Theme: "Share what you built."**

**File:** `notebooks/week-10-12-showcase.ipynb`

### Week 10: Final Prep
- Pre-flight checklist
- Create demo script
- Practice run

### Week 11: Presentations Round 1
- Students present (~5 min each)
- Give and receive feedback
- Note improvements to make

### Week 12: Final Presentations
- Improved presentations
- Course reflection
- Portfolio summary
- What's next

---

## File Structure

```
youth-horizons/
├── bing-plan.txt                    # Email confirmation from Bing
├── Level 1 & Level 2 Curriculum.pdf # Original curriculum outline
├── youth-horizons-class-proposal.pdf # Email thread with engagement details
├── CURRICULUM-BUILD-NOTES.md        # This file
├── archive/                         # Old linear notebooks (preserved)
│   ├── week-01-explore-ai.ipynb
│   ├── week-02-first-model.ipynb
│   └── ... (10 notebooks)
└── notebooks/                       # NEW guided discovery curriculum
    ├── week-01-whats-possible.ipynb      # Phase 1
    ├── week-02-running-models.ipynb
    ├── week-03-ai-coding-partner.ipynb
    ├── week-04-pick-your-path.ipynb      # Phase 2
    ├── week-05-06-track-text.ipynb
    ├── week-05-06-track-images.ipynb
    ├── week-05-06-track-creative.ipynb
    ├── week-07-09-project-phase.ipynb    # Phase 3
    └── week-10-12-showcase.ipynb         # Phase 4
```

---

## Key Differences from Original Approach

| Original | New Approach |
|----------|--------------|
| Linear weekly notebooks | Four-phase structure with flexibility |
| Follow-along instruction | Guided discovery with student choice |
| Everyone does same content | Three specialization tracks |
| Fine-tuning as required endpoint | Fine-tuning as optional stretch goal |
| Weekly deliverables | Portfolio project as main outcome |

---

## Testing Notes

### Phase 1
- [ ] Week 1 tested
- [ ] Week 2 tested
- [ ] Week 3 tested

### Phase 2
- [ ] Week 4 tested
- [ ] Track Text tested
- [ ] Track Images tested
- [ ] Track Creative tested

### Phase 3
- [ ] Project phase notebook tested

### Phase 4
- [ ] Showcase notebook tested

---

## Outstanding Items

1. **Test all notebooks** - Run through completely to verify
2. **Verify HuggingFace links** - Some Spaces may have changed
3. **Professional bio and headshot** - Bing requested for promotional materials
4. **Confirm Level 1 coverage** - What do students know coming in?

---

## Pre-Course Communication: Cost & Free Tier Considerations

**Added:** January 26, 2026

### Important: Communicate to Students/Parents Before Course Starts

The curriculum is designed to work entirely on **free tools**:
- **Google Colab** (free tier)
- **Hugging Face** (free, open-source models)
- **GitHub** (free account)

**No paid subscriptions are required.**

However, there are tradeoffs with free tiers that students/parents should understand:

### Google Colab Free Tier Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Sessions timeout after ~90 min idle | Models need to be reloaded | Save work frequently; "Restart Runtime" between sections |
| No guaranteed GPU access | Image models run slower on CPU | Expect 5-10 sec per image instead of 1-2 sec |
| ~12GB RAM limit | Can't load too many models at once | Restart runtime between notebooks |
| Occasional unavailability during peak times | May not be able to connect | Have backup plan; try again later |

### Models Used (All Free)

**Text models (small, work on CPU):**
- Sentiment analysis (~250MB)
- Zero-shot classification (~400MB)
- Question answering (~250MB)
- Summarization (~300MB)
- Named entity recognition (~250MB)
- Text generation - distilgpt2 (~80MB)
- Emotion detection (~250MB)

**Image models (medium, slower on CPU):**
- Image classification - ViT (~350MB)
- Zero-shot image classification - CLIP (~600MB)
- Image captioning - BLIP (~1GB) ← largest model, slowest on CPU

### What Students Should NOT Expect

The free tier does NOT support:
- Image generation (Stable Diffusion) — needs GPU, too much memory
- Large language models (GPT-2 full, Llama, etc.) — too slow/large
- Video models — not feasible
- Real-time applications — too slow

If students get excited and want to try these, they'll need paid resources (Colab Pro, cloud GPUs, etc.).

### Notebook Adjustments Needed

- [ ] Add "Restart Runtime" reminders between major sections
- [ ] Add note in Week 1 that models take time to load (this is normal)
- [ ] Add project guidance steering toward models we've already used
- [ ] Consider adding simplified project templates for students who need more structure

### Communication Template for Parents

> "The course uses free tools that don't require any subscriptions. Students will use Google Colab (a free cloud coding environment) and Hugging Face (a platform with free AI models). The tradeoff is that some AI tasks run slower than they would with paid resources, and coding sessions can timeout if left idle for too long. These are minor inconveniences, not blockers—students just need to save their work regularly."

---

## Key Resources

**Hugging Face:**
- Spaces: https://huggingface.co/spaces
- Models: https://huggingface.co/models
- Datasets: https://huggingface.co/datasets
- Transformers docs: https://huggingface.co/docs/transformers

**AI Assistants for Coding:**
- ChatGPT: https://chat.openai.com
- Claude: https://claude.ai
- HuggingChat: https://huggingface.co/chat

---

*Last updated: January 17, 2026*
