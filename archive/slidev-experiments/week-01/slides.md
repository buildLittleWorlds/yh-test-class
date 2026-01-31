---
theme: default
title: "What's Possible with AI?"
info: |
  Youth Horizons AI Program - Week 1
  Explore, Discover, Get Inspired
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# What's Possible with AI?

## Explore, Discover, Get Inspired

Youth Horizons AI Program - Week 1

---
layout: default
---

# Today's Roadmap

<div class="grid grid-cols-2 gap-4 mt-8">
<div>

| Time | Activity |
|------|----------|
| 0:00-0:15 | What is AI? |
| 0:15-0:45 | Explore Image AI together |
| 0:45-1:00 | Discussion: How does it work? |

</div>
<div>

| Time | Activity |
|------|----------|
| 1:00-1:30 | Independent exploration |
| 1:30-1:45 | Account setup |
| 1:45-2:00 | Share & reflect |

</div>
</div>

---
layout: center
class: text-center
---

# Part 1: What is AI?

---
layout: image-right
image: /images/slide-03-input-model-output.png
backgroundSize: contain
---

# The Big Secret

<v-click>

## AI isn't magic.

</v-click>

<v-click>

Every AI tool follows the same pattern:

```
INPUT  →  [AI MODEL]  →  OUTPUT
```

</v-click>

<v-click>

The "model" learned patterns from millions of examples. That's it.

</v-click>

---
layout: default
---

# Examples of the Pattern

<img src="/images/slide-04-examples.png" class="h-80 mx-auto" />

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">
<div>

- **Text** → ChatGPT → **More text**
- **Text** → DALL-E → **Image**

</div>
<div>

- **Audio** → Whisper → **Text**
- **Image** → Classifier → **Labels**

</div>
</div>

---
layout: center
class: text-center
---

# Discussion Question

<div class="text-3xl mt-8 text-blue-600">

What's something you think AI probably **CAN'T** do well?

</div>

<div class="mt-8 text-gray-500">

We'll revisit this at the end of class.

</div>

---
layout: center
class: text-center
---

# Part 2: Image AI Exploration

---
layout: default
---

# Let's Explore: Image Generation

<div class="text-center mt-8">

## We'll try this together

<a href="https://huggingface.co/spaces/stabilityai/stable-diffusion-3.5-large" target="_blank" class="text-2xl text-blue-600 hover:underline">
  Stable Diffusion 3.5
</a>

<div class="text-gray-500 mt-4">
huggingface.co/spaces/stabilityai/stable-diffusion-3.5-large
</div>

</div>

---
layout: two-cols
---

# Experiment 1: Adding Detail

Try these prompts:

<v-clicks>

1. `a cat`

2. `a fluffy orange cat sitting on a windowsill`

3. `a fluffy orange cat sitting on a windowsill, golden hour lighting, photograph`

</v-clicks>

::right::

<img src="/images/slide-07-detail-funnel.png" class="h-80 mt-8" />

<div class="text-center mt-4 text-blue-600 font-bold">
How does adding detail change the result?
</div>

---
layout: two-cols
---

# Experiment 2: Style Matters

Same subject, different styles:

<v-clicks>

- `a robot, photograph`
- `a robot, oil painting, renaissance style`
- `a robot, anime style`
- `a robot, pencil sketch`

</v-clicks>

<div class="mt-4 text-blue-600 font-bold">
Which style worked best? Which failed?
</div>

::right::

<img src="/images/slide-08-style-branches.png" class="h-80 mt-8" />

---
layout: two-cols
---

# Experiment 3: Breaking It

Try to confuse the AI:

<v-clicks>

- **Contradictions:** `a square circle`
- **Abstract:** `the feeling of Monday morning`
- **Text:** `a sign that says HELLO WORLD`
- **Hands:** `a person waving with five fingers`

</v-clicks>

<div class="mt-4 text-blue-600 font-bold">
What fails? Why?
</div>

::right::

<img src="/images/slide-09-failure-modes.png" class="h-80 mt-8" />

---
layout: default
---

# Now the Other Direction: Image Understanding

<div class="text-center mt-8">

<a href="https://huggingface.co/spaces/gokaygokay/Florence-2" target="_blank" class="text-2xl text-blue-600 hover:underline">
  Florence-2
</a>

<div class="mt-4 text-lg">
Tasks to try: Caption, Detailed Caption, Object Detection
</div>

<div class="mt-8 text-xl text-green-600">
Upload your own photo!
</div>

<div class="mt-4 text-sm text-gray-500">
Backup: <a href="https://huggingface.co/spaces?sort=likes&search=image+caption" target="_blank" class="text-blue-500 hover:underline">Image Captioning Spaces</a>
</div>

</div>

---
layout: center
class: text-center
---

# Part 3: Discussion

## How Does This Actually Work?

---
layout: default
---

# Let's Figure This Out

<div class="space-y-8 mt-8">

<v-click>

### Question 1
**Why does more detail = better results?**

Think about: "draw a cat" vs "draw a fluffy orange tabby cat curled up on a blue velvet couch"

</v-click>

<v-click>

### Question 2
**Why does AI struggle with hands and text?**

Hint: How consistent are hands in photos? Does "A" always look the same?

</v-click>

<v-click>

### Question 3
**Can AI understand *why* a photo is funny?**

Or the emotional meaning? Or what happened before/after?

</v-click>

</div>

---
layout: image
image: /images/slide-12-understanding-gap.png
backgroundSize: contain
class: bg-white
---

---
layout: two-cols
---

# Remember This

<v-clicks>

## AI = Incredibly Talented Mimics

They **reproduce patterns** they've seen.

They don't know what those patterns **mean**.

</v-clicks>

::right::

<img src="/images/slide-13-training-inference.png" class="h-80 mt-8" />

---
layout: center
class: text-center
---

# Part 4: Independent Exploration

---
layout: default
---

# Your Mission

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

## The Challenge

<v-clicks>

- Visit **at least 6** AI tools
- Spend **3-4 minutes** with each
- Find their limits
- Rate and take notes

</v-clicks>

</div>
<div>

## What to look for

<v-clicks>

- What surprised you?
- What broke it?
- Would you use this?

</v-clicks>

<div class="mt-4 text-blue-600">
Open your notebook for the list!
</div>

</div>
</div>

---
layout: image-right
image: /images/slide-15-categories.png
backgroundSize: contain
---

# The Categories

<div class="text-sm space-y-4">

**Text & Language**
- Chatbot Arena, HuggingChat, Summarizer

**Audio & Speech**
- Whisper, Edge TTS

**Images**
- Segment Anything, Depth Estimation

**Wild Cards**
- You discover!

</div>

---
layout: center
class: text-center
---

# Part 5: Account Setup

---
layout: two-cols
---

# GitHub: Your Portfolio Home

<div class="mt-4">

<a href="https://github.com" target="_blank" class="text-2xl text-blue-600 hover:underline">
  github.com
</a>

</div>

<v-clicks>

### Choose your username carefully!

**Good:**
- `maya-builds`
- `alex-ai`

**Avoid:**
- Birth years
- Gamertags
- Inside jokes

</v-clicks>

::right::

<div class="mt-16 text-center">

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" class="h-32 mx-auto" />

<div class="mt-4 text-gray-500">
Follow detailed steps in your notebook
</div>

</div>

---
layout: two-cols
---

# Hugging Face: Home of AI Models

<div class="mt-4">

<a href="https://huggingface.co" target="_blank" class="text-2xl text-blue-600 hover:underline">
  huggingface.co
</a>

</div>

<v-click>

### You'll use this constantly!

- AI models
- Spaces (demos)
- Datasets
- Community

</v-click>

::right::

<div class="mt-16 text-center">

<img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" class="h-32 mx-auto" />

<div class="mt-4 text-gray-500">
Follow steps in notebook
</div>

</div>

---
layout: center
class: text-center
---

# Part 6: Share & Reflect

---
layout: default
---

# Share & Reflect

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

## Each person shares:

<v-clicks>

- **ONE** tool that impressed you

- **ONE** thing AI couldn't do

</v-clicks>

</div>
<div>

## Then in your notebook:

<v-clicks>

- Which category interests you most?
- What CAN'T AI do? (revisit your answer)
- Your dream AI tool idea
- One question you still have

</v-clicks>

</div>
</div>

---
layout: two-cols
---

# Next Week Preview

<div class="mt-8">

## You'll run AI models yourself — with code!

</div>

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

classifier("I love learning about AI!")
```

<v-click>

<div class="mt-4 text-green-600 text-xl font-bold">
Three lines. That's it.
</div>

</v-click>

::right::

<img src="/images/slide-19-pipeline-code.png" class="h-80 mt-8" />

---
layout: center
class: text-center
---

# See You Next Week!

<div class="text-2xl mt-8 text-gray-600">

Youth Horizons AI Program

</div>
