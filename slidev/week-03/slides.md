---
theme: default
title: "Week 3: AI as Your Coding Partner"
info: |
  Youth Horizons AI Program - Week 3
  Using ChatGPT and Claude to Build Things
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# AI as Your Coding Partner

## Using ChatGPT and Claude to Build Things

<div class="mt-12 text-gray-500">
Youth Horizons AI Program - Week 3
</div>

---

# Today's Roadmap

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

<v-clicks>

- **Review** (10 min)
  - What pipelines did you explore?

- **How to Prompt for Code** (20 min)
  - The CLEAR framework

- **Guided: Build a Mini Tool** (25 min)
  - Text Analyzer with AI help

</v-clicks>

</div>
<div>

<v-clicks>

- **Challenge: Your Own Tool** (30 min)
  - Pick a project, build it!

- **Reading & Modifying Code** (25 min)
  - Become a code detective

- **Share & Reflect** (10 min)
  - Save to GitHub, look ahead

</v-clicks>

</div>
</div>

---
layout: center
---

# Part 1: Review & Setup

---

# Quick Review

<div class="mt-8 space-y-8">

<v-clicks>

<div class="text-2xl">
What pipelines did you explore last week?
</div>

<div class="grid grid-cols-4 gap-4 text-center">
  <div class="p-4 bg-blue-100 rounded-lg">Sentiment?</div>
  <div class="p-4 bg-green-100 rounded-lg">Summarization?</div>
  <div class="p-4 bg-purple-100 rounded-lg">NER?</div>
  <div class="p-4 bg-orange-100 rounded-lg">Text Generation?</div>
</div>

<div class="text-2xl mt-8">
Did anyone find a cool failure mode?
</div>

<div class="text-gray-500 text-xl mt-4">
Let's share! What worked? What broke?
</div>

</v-clicks>

</div>

---
layout: image-right
image: /images/slide-04-big-idea.png
backgroundSize: contain
---

# Today's Big Idea

<v-clicks>

**You DON'T need to memorize Python syntax**

The four steps:

1. **Know** what you want to build
2. **Ask** AI to write the code
3. **Understand** what the AI wrote
4. **Modify** it to do what YOU want

</v-clicks>

<v-click>

<div class="mt-8 p-4 bg-blue-100 rounded-lg">
This is how professional programmers work in 2026
</div>

</v-click>

---
layout: center
---

# Part 2: How to Prompt for Code

---
layout: image-right
image: /images/slide-05-ai-assistants.png
backgroundSize: contain
---

# The AI Assistants

Three tools you can use:

<v-clicks>

<div class="mt-4">
<a href="https://chat.openai.com" target="_blank" class="text-xl text-blue-600 hover:underline">ChatGPT</a>
<span class="text-gray-500 ml-2">- Most popular</span>
</div>

<div class="mt-4">
<a href="https://claude.ai" target="_blank" class="text-xl text-blue-600 hover:underline">Claude</a>
<span class="text-gray-500 ml-2">- Great at code</span>
</div>

<div class="mt-4">
<a href="https://huggingface.co/chat/" target="_blank" class="text-xl text-blue-600 hover:underline">HuggingChat</a>
<span class="text-gray-500 ml-2">- Free & open source</span>
</div>

</v-clicks>

<v-click>

<div class="mt-8 p-4 bg-yellow-100 rounded-lg font-bold">
Open one of these in another tab now!
</div>

</v-click>

---
layout: image-right
image: /images/slide-06-clear-framework.png
backgroundSize: contain
---

# The CLEAR Framework

When asking AI to write code:

<v-clicks>

- **C** - Context
  - "I'm working in Google Colab..."

- **L** - Language/Libraries
  - "Using Python and transformers..."

- **E** - Explain the goal
  - "I want to analyze sentiment..."

- **A** - Ask specifically
  - "Write a function called..."

- **R** - Requirements
  - "Include comments, handle errors..."

</v-clicks>

---
layout: image-right
image: /images/slide-07-bad-vs-good.png
backgroundSize: contain
---

# Bad vs Good Prompt

<v-clicks>

<div class="p-3 bg-red-100 rounded-lg mb-4">
<strong>Bad prompt:</strong><br>
"Write code that does sentiment analysis"
</div>

<div class="text-sm text-red-600 mb-6">
No context, no details, no requirements
</div>

<div class="p-3 bg-green-100 rounded-lg mb-4">
<strong>Good prompt:</strong><br>
"I'm working in Google Colab with Python. Using Hugging Face transformers, write a function called analyze_reviews that..."
</div>

<div class="text-sm text-green-600">
Clear context, specific request, defined output
</div>

</v-clicks>

<v-click>

<div class="mt-4 text-xl font-bold">
Which will give better results?
</div>

</v-click>

---

# Practice: Write Your Prompt

<div class="mt-4">

**Task:** You want code that:

<v-clicks>

1. Summarizes a paragraph
2. Finds all people/places/organizations
3. Displays everything nicely

</v-clicks>

</div>

<v-click>

<div class="grid grid-cols-2 gap-8 mt-8">
<div class="p-4 bg-gray-100 rounded-lg">

**Fill in the CLEAR framework:**
- C - Context: ___
- L - Language: ___
- E - Explain: ___
- A - Ask: ___
- R - Requirements: ___

</div>
<div class="p-4 bg-blue-100 rounded-lg">

**Then combine it into one prompt!**

Share with a classmate - how could you make it clearer?

</div>
</div>

</v-click>

---
layout: center
---

# Part 3: Building a Mini Tool

## Guided Activity

---
layout: image-right
image: /images/slide-09-text-analyzer.png
backgroundSize: contain
---

# Our Goal: Text Analyzer

We'll build a tool that:

<v-clicks>

- Takes any paragraph of text

- Analyzes **sentiment** (positive/negative)

- Creates a **summary** (1-2 sentences)

- Finds **named entities** (people, places, orgs)

- Displays results nicely

</v-clicks>

<v-click>

<div class="mt-4 text-sm">
Try the demos:
<a href="https://huggingface.co/tasks/text-classification" target="_blank" class="text-blue-600 hover:underline">Sentiment</a> |
<a href="https://huggingface.co/tasks/summarization" target="_blank" class="text-blue-600 hover:underline">Summarization</a> |
<a href="https://huggingface.co/tasks/token-classification" target="_blank" class="text-blue-600 hover:underline">NER</a>
</div>

</v-click>

---

# Step 1: Ask AI for the Code

<div class="mt-4">

Go to your AI assistant and paste this prompt:

</div>

<div class="mt-4 p-4 bg-gray-100 rounded-lg text-sm">

```
I'm working in Google Colab with Python. Using the Hugging Face
transformers library, write a complete text analysis tool that:

1. Takes a paragraph of text as input
2. Analyzes the sentiment (positive/negative)
3. Summarizes it in 1-2 sentences
4. Finds all named entities (people, places, organizations)
5. Displays all results in a nicely formatted way

Requirements:
- Include the pip install command at the top
- Add helpful comments explaining each step
- Create a function called analyze_text() that I can reuse
- Include an example at the end showing how to use it
```

</div>

<v-click>

<div class="mt-4 text-center font-bold">
Copy what it gives you into your notebook!
</div>

</v-click>

---

# Steps 2-3: Run & Understand

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

**Run it - did it work?**

<v-clicks>

Common issues:

- Missing `!pip install` at the top
- Model name typos
- Indentation errors (Python is picky!)

</v-clicks>

</div>
<div>

<v-click>

**Let's understand it together:**

- What libraries does it import?
- How does it create pipelines?
- What's the function structure?
- How does it format output?

</v-click>

</div>
</div>

<v-click>

<div class="mt-8 p-4 bg-yellow-100 rounded-lg text-center">
<strong>Key pattern to remember:</strong>
<code class="block mt-2">from transformers import pipeline</code>
<code class="block">model = pipeline("task-name")</code>
<code class="block">result = model("input")</code>
</div>

</v-click>

---

# Step 4: Ask AI to Modify It

<div class="mt-8">

Now ask the AI to change the code:

</div>

<v-clicks>

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-4 bg-blue-100 rounded-lg text-center">
"Modify it to also <strong>count words</strong>"
</div>

<div class="p-4 bg-green-100 rounded-lg text-center">
"Classify the text as: news, opinion, story, or educational"
</div>

<div class="p-4 bg-purple-100 rounded-lg text-center">
"Use <strong>emoji</strong> for the results display"
</div>

</div>

</v-clicks>

<v-click>

<div class="mt-12 text-center text-2xl">
The AI can iterate! Just ask for changes.
</div>

</v-click>

---
layout: center
---

# Part 4: Challenge Time!

## Build Your Own Tool

---
layout: image-right
image: /images/slide-13-challenge-options.png
backgroundSize: contain
---

# Pick Your Challenge

<v-clicks>

**A: Review Analyzer**
- Analyze product/movie reviews
- Calculate overall sentiment
- Find best & worst reviews

**B: Homework Helper**
- Summarize any topic
- Extract key facts
- Generate quiz questions

**C: Story Starter**
- Generate story openings
- Analyze mood of each
- Continue your favorite

**D: Your Own Idea**
- What do YOU want to build?

</v-clicks>

---

# Build Time!

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

<v-clicks>

**Your workflow:**

1. Write your prompt using CLEAR

2. Ask AI to generate the code

3. Copy to notebook and run

4. Test with real input

5. Iterate and improve!

</v-clicks>

</div>
<div>

<v-click>

<div class="p-6 bg-yellow-100 rounded-lg text-center">

<div class="text-4xl mb-4">25 minutes</div>

<div class="text-2xl font-bold">GO!</div>

<div class="text-gray-600 mt-4">
Ask for help if you get stuck
</div>

</div>

</v-click>

</div>
</div>

---
layout: image-right
image: /images/slide-15-debug-iterate.png
backgroundSize: contain
---

# Debug & Iterate

<v-clicks>

**If something breaks:**

1. Copy the error message
2. Paste to AI: "I got this error:"
3. Ask it to fix the code
4. Try again!

**If you want changes:**

1. Describe what's different
2. Be specific: "Change X to do Y"
3. The AI will modify the code

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-green-100 rounded-lg">
Iteration is normal - even pros do this constantly!
</div>

</v-click>

---
layout: center
---

# Part 5: Reading & Modifying Code

---
layout: image-right
image: /images/slide-16-code-detective.png
backgroundSize: contain
---

# Code Detective

Being able to **READ** code is just as important!

<v-clicks>

**Questions to ask yourself:**

- What does this function **do**?

- What goes **in** (parameters)?

- What comes **out** (return)?

- What would be a better **name**?

</v-clicks>

<v-click>

<div class="mt-4 p-3 bg-blue-100 rounded-lg">
Read code like you're solving a mystery!
</div>

</v-click>

---

# Modify Without AI Help

<div class="mt-4">

**Challenge:** Can you modify this code yourself?

</div>

```python {all|3|11|13-14}
def email_sorter(texts):
    classifier = pipeline("zero-shot-classification")
    categories = ["urgent", "normal", "spam"]  # Add "promotional"?

    results = []
    for text in texts:
        result = classifier(text, categories)
        results.append({'message': text, 'category': result['labels'][0]})

    urgent_count = sum(1 for r in results if r['category'] == 'urgent')
    # TODO: Count spam too?

    # TODO: Warning if too many urgent/spam?

    return results, urgent_count
```

<v-click>

<div class="mt-4 text-center">
Try yourself first, then use AI if stuck. This builds real understanding!
</div>

</v-click>

---

# Ask Good Questions About Code

<div class="mt-8">

When you see code you don't understand, ask AI to explain:

</div>

<v-clicks>

<div class="grid grid-cols-1 gap-4 mt-8">

<div class="p-4 bg-gray-100 rounded-lg">
"What does this line do: <code>sum(1 for r in results if r['category'] == 'urgent')</code>"
</div>

<div class="p-4 bg-gray-100 rounded-lg">
"Explain the f-string on the print line"
</div>

<div class="p-4 bg-gray-100 rounded-lg">
"What's the difference between <code>result['labels'][0]</code> and <code>result['labels']</code>?"
</div>

</div>

</v-clicks>

<v-click>

<div class="mt-8 text-center text-xl">
Use AI to <strong>learn</strong>, not just to generate!
</div>

</v-click>

---
layout: center
---

# Part 6: Wrap-up

---

# Save & Reflect

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

**Save to GitHub:**

1. Download notebook (.ipynb)
2. Upload to your `ai-explorer` repo
3. Update your README!

</div>
<div>

**Reflection questions:**

<v-clicks>

- Most important thing about prompting?

- Confidence rating (1-5)?

- What would you build with more time?

- What's still confusing?

</v-clicks>

</div>
</div>

<v-click>

<div class="mt-8 p-4 bg-green-100 rounded-lg text-center">
<strong>Key Takeaway:</strong> CLEAR prompts + iteration = professional coding workflow
</div>

</v-click>

---
layout: image-right
image: /images/slide-20-next-week.png
backgroundSize: contain
---

# Next Week: Pick Your Path!

Weeks 4-6: Specialization

<v-clicks>

**Text & Language**
- Chatbots, writing tools, Q&A bots

**Images & Vision**
- Photo tools, art generators, detectors

**Creative AI**
- Story generators, game AI, creative tools

</v-clicks>

<v-click>

<div class="mt-8 p-4 bg-purple-100 rounded-lg text-center font-bold">
Think about which excites YOU most!
</div>

</v-click>

---
layout: center
class: text-center
---

# See you next week!

<div class="mt-8 text-gray-500">
Youth Horizons AI Program - Week 3 Complete
</div>

<div class="mt-8">

**Remember the CLEAR Framework:**

Context | Language | Explain | Ask | Requirements

</div>

<div class="mt-8">
<a href="https://github.com/buildLittleWorlds/yh-test-class" target="_blank" class="text-blue-600 hover:underline">
github.com/buildLittleWorlds/yh-test-class
</a>
</div>
