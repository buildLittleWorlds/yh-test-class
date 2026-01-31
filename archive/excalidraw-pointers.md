- Excalidraw's post announces upgrades to its AI-powered text-to-diagram tool, introducing a conversational chat interface that generates hand-drawn diagrams in real-time via streaming, making it faster and more intuitive for iterative design.
- The demo video showcases prompts like "Create a user login flowchart" producing editable, sketch-style visuals, with follow-ups such as adding two-factor authentication seamlessly updating the canvas, supporting flowcharts, ER diagrams, and more.
- User replies praise its simplicity and potential for AI integrations, though some note needs like zoom for large outputs; as an open-source collaborative whiteboard, this enhances accessibility for developers and educators over rigid tools like Mermaid.




Here’s a practical **tutorial-style guide** for writing effective **text-to-diagram prompts** in the current Excalidraw AI feature (as of early 2026, with the conversational chat + streaming improvements).

The tool works best when you treat it like giving instructions to a helpful but slightly literal colleague who draws in a hand-drawn style.

### Core Principles for Great Prompts
- **Be explicit about diagram type** — The AI usually guesses correctly, but naming it removes ambiguity.
- **Use natural but structured language** — Write like you're explaining to someone, but include key relationships, steps, actors, or components.
- **Start simple, then iterate** — The new chat interface shines here: generate → refine → add → fix → rearrange.
- **Include direction/flow when relevant** — Words like "from top to bottom", "left to right", "sequential steps", or "hierarchical" help layout.
- **Specify style tweaks if needed** — But don't overdo it — the hand-drawn aesthetic is the default strength.

### Supported Diagram Types (Common Ones That Work Reliably)
- Flowchart / process flow
- Sequence diagram
- Mind map
- Entity-Relationship (ER) diagram
- Class diagram / UML basics
- Simple network / architecture diagram
- User journey / workflow
- Gantt chart (basic)
- Tree structure / hierarchy
- Concept map
- Basic state machine

(Mermaid-like syntax understanding powers most of these under the hood, but you don't need to write Mermaid code — plain English usually works better.)

### Prompt Structure Template (Recommended)
Use some variation of this pattern for the best first-shot results:

```
Create a [diagram type] that shows [main subject / purpose].

Key elements:
- [actor / entity 1] → [action/relationship] → [actor / entity 2]
- [step 1]: [description]
- [decision point]: yes → ..., no → ...
- [branch/alternative path]

Layout: [top-down / horizontal / radial / etc.]
Make it clear and not overcrowded.
```

### Good Prompt Examples vs. Weaker Ones

**Strong (usually gives clean, useful result on first try)**  
- "Create a flowchart for user login process including: guest → enter email/password → validate credentials → decision: valid? → yes: redirect to dashboard, no: show error + forgot password link → two-factor authentication step if enabled → success."
- "Draw a sequence diagram showing how a customer places an order in an e-commerce system: Customer, Website Frontend, API, Database, Payment Gateway, Inventory Service. Show happy path + out-of-stock failure."
- "Make a mind map of healthy breakfast options with central node 'Healthy Breakfast', main branches 'Quick (under 5 min)', 'Protein-rich', 'Vegan', and 4–5 examples under each with calories."
- "Generate an ER diagram for a simple library system: entities Books, Authors, Members, Loans; include primary keys, relationships (one-to-many, many-to-many), and cardinalities."

**Weaker / Vague (often messy or wrong type)**  
- "login process"  
- "diagram of how app works"  
- "make something beautiful about coffee"  
- "flowchart" (no content)

**Iterative Refinement Examples (use in chat follow-ups)**  
- "Add 2FA via SMS or authenticator app after password check"  
- "Make the decision diamond larger and red when it's an error path"  
- "Move the payment step before inventory check"  
- "Change layout to vertical instead of horizontal"  
- "Use different colors for admin vs regular user paths"  
- "Remove the guest checkout branch"  
- "Convert this to a swimlane diagram with lanes: User, Server, Database"

### Quick Tips & Best Practices
- **Start broad, then zoom in** — First prompt = overall structure; follow-ups = details & fixes.
- **Use decision words** — "if … then … else", "decision:", "branch:", "yes/no" help create proper diamonds.
- **Name actors clearly** — "User", "Frontend", "API", "Database" → better arrows & lanes than vague pronouns.
- **Ask for Mermaid code view** — If the result is close but needs precision, some versions show underlying Mermaid — you can copy/edit/re-generate.
- **Avoid ultra-complex single prompts** — 15–25 entities/steps is usually the sweet spot for one generation; split into parts if bigger.
- **Streaming = watch & stop** — If it's going wrong mid-generation, you can usually interrupt and rephrase.
- **Zoom complaint workaround** — If the diagram gets huge, ask: "Regenerate more compact" or "Use smaller font / tighter layout".

Experiment in the free version first (limits apply), or go Plus for basically unlimited generations. The more specific + iterative you are, the closer it gets to production-ready sketches.

Try one right now — something small like "flowchart how to make a cup of tea with decision for milk first or after". You'll see how forgiving and fast the new chat version is! ☕


Here are **more concise examples** of effective text-to-diagram prompts for Excalidraw AI. These are shorter, punchier versions that still produce clean results in one shot (or with minimal follow-up).

### Flowchart
1. User login process: email/password → validate → if valid: dashboard, else: error + forgot password → optional 2FA.
2. Make tea: boil water → add tea bag → steep 3 min → decision: add milk? → yes: pour milk then sugar, no: sugar only.
3. Password reset: user requests → email link → click link → new password → confirm → success.

### Sequence Diagram
1. Order placement: Customer → Frontend → API → Payment Gateway → Inventory → Database.
2. Login sequence: User → App → Auth Service → Database → JWT → App.
3. API call with error: Client → Server → validate token → if invalid: 401, else: process request → response.

### Mind Map
1. Healthy breakfast: center "Healthy Breakfast" → branches: Quick (smoothie, yogurt), Protein (eggs, Greek yogurt), Vegan (oatmeal, chia pudding).
2. Project management tools: center "PM Tools" → Trello (kanban), Jira (agile), Notion (all-in-one), Asana (tasks).
3. Coffee types: center "Coffee" → Espresso, Drip, Cold brew, Latte, Cappuccino.

### ER Diagram
1. Library: Books (ISBN PK), Authors, Members (ID PK), Loans (Book–Member many-to-many).
2. Blog: Users (ID PK), Posts (ID PK, author FK), Comments (post FK, user FK).
3. Online store: Products, Orders, Customers, OrderItems (order–product).

### Other Quick Ones
- Class diagram: Animal (name, eat()) → Dog (bark()) → Cat (meow()).
- User journey: Visitor → Homepage → Product page → Add to cart → Checkout → Payment → Confirmation.
- Simple tree: Company → Departments (HR, Engineering, Sales) → Teams under each.

**Pro tip for even shorter prompts**:  
Just name the type + subject + main flow if obvious.  
Examples that still work well:  
- "flowchart user signup with email verification"  
- "sequence diagram fetch user profile"  
- "mind map morning routine"  
- "ER diagram todo app (users, tasks, tags)"

Paste one directly into Excalidraw's chat — the streaming update usually nails it fast. If the layout feels off, follow up with "vertical" or "more compact". Enjoy sketching!


Here’s the latest on using **AI to generate diagrams in Excalidraw** (as of January 2026). The core feature lives in **Excalidraw+** (the paid/cloud version at plus.excalidraw.com), where the text-to-diagram tool has seen major upgrades.

### How to Access & Use It
- Open Excalidraw → click the **toolbar** → **More tools** → **Text to diagram** (or look for the ✨ AI icon).
- A **chat-style interface** appears (big 2025/early-2026 improvement).
- Type your prompt → it **streams** the diagram live as it builds (very fast now).
- Once generated, edit freely by hand — drag, resize, recolor, add notes, etc.
- Bonus: Many generations show the underlying **Mermaid code** — view/edit it, then re-generate for precision tweaks.

Free excalidraw.com has very limited/no AI generations; **Excalidraw+** unlocks extended usage (unlimited or high quota depending on plan).

### What Works Best Right Now
- **Flowcharts**, **sequence diagrams**, **mind maps**, **ER diagrams**, **software architecture**, **Gantt charts** (basic), **user journeys**, simple **UML**.
- Streaming makes iterative refinement feel magical: generate → "add error handling branch in red" → "make it vertical" → "add swimlanes: User / API / DB".
- People combine it with other AIs: ChatGPT/Claude → describe idea → get Mermaid/JSON/ASCII → paste into Excalidraw AI for hand-drawn polish.

### Fresh Prompt Examples (2026-era, from recent usage & docs)
Short & effective ones that users report nailing clean results:

- "Flowchart: user signs up → verify email → set profile → dashboard"
- "Sequence diagram: customer browser → frontend → auth service → database → JWT returned"
- "Mind map centered on 'Remote Work Tools' with branches: Communication, Project Mgmt, Time Tracking, 3–4 examples each"
- "ER diagram library system: Books (ISBN), Authors (many-to-many), Members, Loans"
- "Software architecture: monolith frontend + backend → microservices (payments, inventory, users) → PostgreSQL + Redis"
- "Gantt chart simple project: Planning 2w, Development 6w, Testing 3w, Launch"

Refinement follow-ups (in the chat):
- "Switch to top-down layout"
- "Color decision nodes yellow"
- "Make actors swimlanes"
- "Compact version, smaller text"
- "Add icons from library for database and API"

### Pro Tips from Recent User Posts & Docs
- Start vague for structure, then get specific in chat — avoids overcrowded first tries.
- For huge/complex → generate pieces separately, then combine on canvas.
- If layout is messy → "regenerate more compact" or edit Mermaid code.
- Export → PNG/SVG for docs/slides, or share live link.
- Integrations/tricks: Some devs feed Claude/GPT prompts to output Excalidraw JSON or Mermaid → import → AI refine.
- Emerging: Open-source experiments (e.g. excalidraw-cli, MCP servers) let agents/LLMs create/edit Excalidraw files programmatically — mostly dev/automation use for now.

It's legitimately one of the most practical AI diagramming tools out there — fast, editable, beautiful hand-drawn style, and the chat/streaming makes it addictive for quick visuals in docs, tweets, pitches, or research.

If you try a specific type (e.g. architecture or user flow), share your prompt/result — happy to help refine it! 🚀



