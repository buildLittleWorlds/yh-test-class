---
theme: default
title: "Running Your First AI Models"
info: |
  Youth Horizons AI Program - Week 2
  From Clicking Buttons to Writing Code
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Running Your First AI Models

## From Clicking Buttons to Writing Code

Youth Horizons AI Program - Week 2

---
layout: default
---

# Today's Roadmap

<div class="grid grid-cols-2 gap-4 mt-8">
<div>

| Time | Activity |
|------|----------|
| 0:00-0:15 | Share & Review |
| 0:15-0:35 | Introduction to Google Colab |
| 0:35-1:00 | Your First Pipeline |

</div>
<div>

| Time | Activity |
|------|----------|
| 1:00-1:30 | Explore Different Pipelines |
| 1:30-1:50 | Challenge: Find the Limits |
| 1:50-2:00 | Save & Reflect |

</div>
</div>

---
layout: center
class: text-center
---

# Part 1: Share & Review

---
layout: default
---

# Quick Check-In

<div class="mt-8 space-y-8">

<v-click>

## Share with the group:

</v-click>

<v-clicks>

- **The most interesting AI tool** you found last week

- **One limitation** you discovered

</v-clicks>

</div>

<div class="mt-12 text-center text-gray-500">

Take 2-3 minutes each

</div>

---
layout: image-right
image: /images/slide-04-clicking-vs-code.png
backgroundSize: contain
---

# Recall: The Pattern

<v-click>

Last week: **INPUT → [AI MODEL] → OUTPUT**

</v-click>

<v-click>

This week: **You control this pattern with code**

</v-click>

<v-click>

## Why bother with code?

</v-click>

<v-clicks>

- Process many inputs at once
- Customize how the model works
- Combine models in creative ways
- Build tools others can use

</v-clicks>

---
layout: center
class: text-center
---

# Part 2: Introduction to Google Colab

---
layout: image-right
image: /images/slide-05-colab-overview.png
backgroundSize: contain
---

# What is Google Colab?

<div class="mt-4">

<a href="https://colab.research.google.com" target="_blank" class="text-2xl text-blue-600 hover:underline">
  colab.research.google.com
</a>

</div>

<v-click>

## A free cloud computer in your browser

</v-click>

<v-click>

### Why it's perfect for AI:

</v-click>

<v-clicks>

- **Free GPU** — the processor AI needs
- **No installation** required
- **Saves automatically**
- **Connects to GitHub**

</v-clicks>

---
layout: image-right
image: /images/slide-06-notebook-cells.png
backgroundSize: contain
---

# How Notebooks Work

<v-click>

## Two types of cells:

</v-click>

<v-clicks>

- **Markdown cells** — text and explanations
- **Code cells** — Python that runs

</v-clicks>

<v-click>

## Key shortcuts:

</v-click>

<v-clicks>

- **Shift+Enter**: Run and move to next
- **Ctrl+Enter**: Run and stay

</v-clicks>

<v-click>

<div class="mt-4 text-red-500 font-bold">
⚠️ Cells run in order!
</div>

</v-click>

---
layout: image-right
image: /images/slide-07-python-basics.png
backgroundSize: contain
---

# Python Basics You'll Need

<v-clicks>

**Variables:**
```python
my_name = "Alex"
```

**Lists:**
```python
favorites = ["pizza", "AI", "music"]
```

**Loops:**
```python
for thing in favorites:
    print(thing)
```

**f-strings:**
```python
f"I like {thing}!"
```

</v-clicks>

<div class="mt-4 text-blue-600">
→ Open your notebook to practice
</div>

---
layout: center
class: text-center
---

# Part 3: Your First Pipeline

---
layout: image-right
image: /images/slide-08-three-lines.png
backgroundSize: contain
---

# The Magic Three Lines

```python
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

sentiment("I love learning about AI!")
```

<v-click>

<div class="mt-4 text-green-600 text-xl font-bold">
This downloads a real AI model and runs it!
</div>

</v-click>

<div class="mt-4 text-sm">

<a href="https://huggingface.co/tasks/text-classification" target="_blank" class="text-blue-600 hover:underline">
  Try it on Hugging Face →
</a>

</div>

---
layout: image-right
image: /images/slide-09-pipeline-breakdown.png
backgroundSize: contain
---

# What Just Happened?

<v-clicks>

**Line 1:** Import the toolbox from Hugging Face

**Line 2:** Create a sentiment analysis tool *(downloads model)*

**Line 3:** Run it on your text

</v-clicks>

<v-click>

## Output:

```python
[{'label': 'POSITIVE', 'score': 0.9998}]
```

</v-click>

---
layout: image-right
image: /images/slide-10-output-explained.png
backgroundSize: contain
---

# Understanding the Output

<v-clicks>

## `label`
**POSITIVE** or **NEGATIVE**

What the model thinks

## `score`
Confidence from **0 to 1**

- 0.99 = 99% confident
- 0.51 = barely confident

</v-clicks>

<div class="mt-4 text-blue-600">
→ Try your own sentences in the notebook
</div>

---
layout: image-right
image: /images/slide-11-batch-processing.png
backgroundSize: contain
---

# The Power of Code: Many Inputs

<v-click>

Process a whole list at once:

```python
texts = [
    "I love this!",
    "This is terrible.",
    "Meh."
]
results = sentiment(texts)
```

</v-click>

<v-click>

## Try sentences that might trick it:

</v-click>

<v-clicks>

- **Sarcasm:** "Oh great, another Monday"
- **Mixed feelings:** "Food was good, service was slow"
- **Neutral:** "The sky is blue"

</v-clicks>

---
layout: center
class: text-center
---

# Part 4: Explore Different Pipelines

---
layout: image-right
image: /images/slide-12-pipeline-zoo.png
backgroundSize: contain
---

# The Pipeline Zoo

<v-click>

Sentiment analysis is just **ONE** type!

</v-click>

<v-click>

## Many more to explore:

</v-click>

<v-clicks>

- <a href="https://huggingface.co/tasks/zero-shot-classification" target="_blank" class="text-blue-600 hover:underline">Zero-Shot Classification</a>
- <a href="https://huggingface.co/tasks/question-answering" target="_blank" class="text-blue-600 hover:underline">Question Answering</a>
- <a href="https://huggingface.co/tasks/summarization" target="_blank" class="text-blue-600 hover:underline">Summarization</a>
- <a href="https://huggingface.co/tasks/token-classification" target="_blank" class="text-blue-600 hover:underline">Named Entity Recognition</a>
- <a href="https://huggingface.co/tasks/text-generation" target="_blank" class="text-blue-600 hover:underline">Text Generation</a>

</v-clicks>

<v-click>

<div class="mt-4 text-green-600 font-bold">
Same pattern, different task
</div>

</v-click>

---
layout: default
---

# Zero-Shot Classification

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

<v-click>

## Classify text into categories YOU define

</v-click>

<v-click>

```python
classifier = pipeline("zero-shot-classification")

classifier(
    "I need to finish my homework",
    candidate_labels=["school", "sports", "food"]
)
```

</v-click>

<v-click>

<div class="mt-4 text-green-600 font-bold">
Even categories it wasn't trained on!
</div>

</v-click>

</div>
<div>

<v-click>

## Use cases:

- Sorting emails
- Categorizing feedback
- Organizing content

</v-click>

<div class="mt-6">

<a href="https://huggingface.co/tasks/zero-shot-classification" target="_blank" class="text-blue-600 hover:underline">
  Try the demo →
</a>

</div>

<div class="mt-2 text-blue-600">
→ Then try in notebook
</div>

</div>
</div>

---
layout: default
---

# Question Answering

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

<v-click>

## Answer questions from a passage of text

</v-click>

<v-click>

```python
qa = pipeline("question-answering")

qa(
    question="What is AI?",
    context="AI stands for Artificial Intelligence.
    It refers to computer systems that can
    perform tasks that typically require
    human intelligence."
)
```

</v-click>

</div>
<div>

<v-click>

## You provide:
- **Context** — the text to search
- **Question** — what you want to know

## Model returns:
- **Answer** — extracted from context
- **Confidence** — how sure it is

</v-click>

<div class="mt-4">

<a href="https://huggingface.co/tasks/question-answering" target="_blank" class="text-blue-600 hover:underline">
  Try the demo →
</a>

</div>

<div class="mt-2 text-blue-600">
→ Then try in notebook
</div>

</div>
</div>

---
layout: image-right
image: /images/slide-15-exploration-checklist.png
backgroundSize: contain
---

# Your Exploration Mission

<v-clicks>

## Try at least 3 different pipeline types

For each one:

1. Run the example code
2. Try your own inputs
3. Find something **surprising**
4. Find something that **breaks it**

Record observations in your notebook

</v-clicks>

<div class="mt-4 text-blue-600">
Open your notebook for the full list of pipelines!
</div>

---
layout: center
class: text-center
---

# Part 5: Challenge — Find the Limits

---
layout: image-right
image: /images/slide-16-break-it.png
backgroundSize: contain
---

# Challenge: Break the Models

<v-clicks>

## Challenge 1: Trick Sentiment
Find **3 sentences** that fool it

## Challenge 2: Multi-Pipeline
Run the **same text** through different pipelines — what does each reveal?

## Challenge 3: Chain Them
**Generate text** → **Analyze its sentiment**

Output of one = Input of next

</v-clicks>

<v-click>

<div class="mt-4 text-center text-purple-600 font-bold text-xl">
AI models have patterns — find them!
</div>

</v-click>

---
layout: default
---

# Discussion: What Did You Find?

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

<v-click>

## What kinds of inputs caused problems?

</v-click>

</div>
<div>

<v-click>

## Common failure modes:

</v-click>

<v-clicks>

- Sarcasm and irony
- Mixed sentiments
- Context-dependent meaning
- Unusual formatting

</v-clicks>

</div>
</div>

<v-click>

<div class="mt-12 text-center text-xl text-red-600 font-bold">
These limitations matter for real applications!
</div>

</v-click>

---
layout: center
class: text-center
---

# Part 6: Wrap-up

---
layout: image-right
image: /images/slide-18-next-week.png
backgroundSize: contain
---

# Save & Look Ahead

<v-click>

## Save your notebook to GitHub:

1. **File** > **Download** > **.ipynb**
2. Upload to your `ai-explorer` repo

</v-click>

<v-click>

## Next week: AI as Your Coding Partner

- Use ChatGPT/Claude to write code **FOR** you
- Understand and modify what they create

</v-click>

<v-click>

## Code pattern to remember:

```python
from transformers import pipeline
model = pipeline("task-name")
result = model("your input")
```

</v-click>

---
layout: center
class: text-center
---

# See You Next Week!

<div class="text-2xl mt-8 text-gray-600">

Youth Horizons AI Program

</div>
