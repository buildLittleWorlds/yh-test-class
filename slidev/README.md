# Slidev Presentations

Interactive slide presentations for the Youth Horizons AI Researcher Program, built with [Slidev](https://sli.dev).

## Live Presentations

| Week | Topic | View Slides |
|------|-------|-------------|
| 1 | What's Possible with AI? | [View](https://buildlittleworlds.github.io/yh-test-class/week-01/) |
| 2 | Running Your First Models | *Coming soon* |
| 3 | AI as Your Coding Partner | *Coming soon* |

---

## Workflow for Creating New Slides

Each week's presentation follows this workflow:

### Step 1: Create the Outline

Create `slidev/week-XX/outline.md` with:

1. **Slide-by-slide descriptions** — What goes on each slide
2. **Image inventory** — Which slides need diagrams
3. **Diagram generation prompts** — Specific prompts for creating each image

Use the Week 1 outline as a template (see `slidev/week-01/outline.md`).

### Step 2: Generate Images

#### Primary Tool: Nano Banana Pro (Recommended)

Most Week 1 images were generated using **Nano Banana Pro** (Google's Gemini 3 Pro Image model), which excels at:
- Clear, readable text in diagrams
- Professional infographic layouts
- Accurate technical diagrams
- High resolution output (up to 4K)

**Access options:**
- [Google AI Studio](https://aistudio.google.com/) (Gemini API)
- Google AI Plus/Pro/Ultra subscription
- Various wrapper tools (see [nanobanana.org](https://nanobanana.org/))

**Workflow:**
1. Copy the diagram prompt from your outline
2. Paste into Nano Banana Pro
3. Iterate: "make the text larger", "use a horizontal layout", "add more contrast"
4. Download PNG to `slidev/week-XX/public/images/`

#### Alternative: Excalidraw AI

For hand-drawn style diagrams, use **Excalidraw AI** (at [plus.excalidraw.com](https://plus.excalidraw.com)):

1. Open Excalidraw → More tools → Text to diagram
2. Paste the diagram prompt from your outline
3. Iterate using chat: "make it more compact", "change to vertical layout", etc.
4. Export as PNG

See `excalidraw-pointers.md` in the repo root for detailed Excalidraw prompting tips.

**Naming convention:** `slide-XX-description.png` (e.g., `slide-03-input-model-output.png`)

### Step 3: Create the Slidev Presentation

Create `slidev/week-XX/slides.md` using the outline and images.

**Key Slidev syntax:**

```markdown
---
theme: default
title: "Week X: Title Here"
---

# Slide Title

Content here

---
layout: two-cols
---

# Left Column Title

Left content

::right::

Right content (often an image)

---
layout: image-right
image: /images/slide-XX-name.png
backgroundSize: contain
---

# Title with Image on Right

Text content here
```

**Common layouts:**
- `default` — Standard slide
- `center` — Centered content
- `two-cols` — Two columns (use `::right::` divider)
- `image-right` / `image-left` — Image on one side
- `image` — Full-bleed background image

**Animations:**
```markdown
<v-click>

This appears on click

</v-click>

<v-clicks>

- Each item
- Appears
- Separately

</v-clicks>
```

### Step 4: Test Locally

```bash
cd slidev/week-XX
npm install
npm run dev
```

Open http://localhost:3030 to preview. Use arrow keys to navigate, `o` for overview.

### Step 5: Deploy

Push to GitHub. The GitHub Action automatically builds and deploys all presentations.

```bash
git add slidev/week-XX
git commit -m "Add Week XX slides"
git push
```

The workflow triggers on changes to `slidev/**` and deploys to GitHub Pages.

---

## Folder Structure

```
slidev/
├── README.md                 # This file
├── week-01/
│   ├── slides.md             # The presentation
│   ├── package.json          # Dependencies
│   ├── package-lock.json
│   └── public/
│       └── images/           # Slide diagrams
│           ├── slide-03-input-model-output.png
│           ├── slide-04-examples.png
│           └── ...
├── week-02/                  # Future weeks follow same structure
│   └── ...
```

---

## Adding a New Week

1. **Copy the structure:**
   ```bash
   cp -r slidev/week-01 slidev/week-XX
   rm slidev/week-XX/public/images/*
   rm slidev/week-XX/node_modules  # if present
   ```

2. **Update package.json** name field

3. **Create outline** with diagram prompts

4. **Generate images** using Excalidraw AI

5. **Write slides.md** based on outline

6. **Update the GitHub Action** (if needed) to build the new week:

   Edit `.github/workflows/deploy-slides.yml` and add:
   ```yaml
   - name: Build Week XX slides
     working-directory: slidev/week-XX
     run: |
       npm ci
       npx slidev build --base /yh-test-class/week-XX/
   ```

   And in the "Prepare deployment folder" step:
   ```yaml
   mv slidev/week-XX/dist dist/week-XX
   ```

7. **Update README tables** in both `slidev/README.md` and root `README.md`

---

## Diagram Generation Tips

From the Week 1 experience (using Nano Banana Pro), effective diagram prompts:

### Be Specific About Structure
```
Diagram showing four parallel examples of the AI pattern, each as a simple flowchart:

Row 1: "What's the weather?" → [ChatGPT] → "It's sunny and 72°F"
Row 2: "A castle in the clouds" → [DALL-E] → [small image icon]
...

Align them vertically to emphasize the shared INPUT → MODEL → OUTPUT structure.
Clean diagram style, labels clearly readable.
```

### Use Visual Metaphors
```
Diagram showing how prompt specificity narrows possibilities:

Left side: Wide funnel labeled "a cat" containing many different cat images
Middle: Medium funnel labeled "a fluffy orange cat on a windowsill" with fewer options
Right side: Narrow funnel pointing to one specific outcome

Arrow across the bottom: "More detail = Fewer possibilities = More predictable result"
```

### Explain Concepts Visually
```
Two-part diagram showing AI training vs. usage:

TOP - "Training" (happens once, before you use it):
Millions of images with labels → [Neural Network] → Learns patterns

BOTTOM - "Using" (what happens when you give it a prompt):
Your prompt → [Trained Model] → Combines patterns into output

Key insight box: "The model doesn't 'understand' - it learned which patterns appear together"
```

### Iterate in Chat
After initial generation:
- "Make it more compact"
- "Change to vertical layout"
- "Use different colors for each section"
- "Add icons for database and API"

---

## Resources

**Slidev:**
- [Slidev Documentation](https://sli.dev/guide/)
- [Slidev Syntax](https://sli.dev/guide/syntax)

**Image Generation:**
- [Nano Banana Pro](https://nanobanana.org/) - Primary tool for Week 1 diagrams (Gemini 3 Pro Image)
- [Google AI Studio](https://aistudio.google.com/) - Direct access to Gemini models
- [Excalidraw AI](https://plus.excalidraw.com) - Hand-drawn style diagrams (requires Plus subscription)
- Local reference: `excalidraw-pointers.md` in repo root
