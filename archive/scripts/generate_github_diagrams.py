#!/usr/bin/env python3
"""
Generate Excalidraw diagrams for GitHub workflow education.

This script creates .excalidraw JSON files that can be:
1. Opened directly at https://excalidraw.com
2. Embedded in Reveal.js presentations
3. Exported as SVG/PNG for static use

Usage:
    python generate_github_diagrams.py

Output:
    Creates .excalidraw files in the diagrams/ folder
"""

import json
import os
import uuid
from dataclasses import dataclass, field
from typing import Optional

# Excalidraw color palette (hand-drawn friendly colors)
COLORS = {
    "blue": "#1971c2",
    "light_blue": "#a5d8ff",
    "green": "#2f9e44",
    "light_green": "#b2f2bb",
    "orange": "#e8590c",
    "light_orange": "#ffc078",
    "purple": "#7950f2",
    "light_purple": "#d0bfff",
    "red": "#c92a2a",
    "light_red": "#ffc9c9",
    "gray": "#495057",
    "light_gray": "#dee2e6",
    "black": "#1e1e1e",
    "white": "#ffffff",
}


def generate_id() -> str:
    """Generate a unique ID for an Excalidraw element."""
    return str(uuid.uuid4())[:8]


@dataclass
class ExcalidrawElement:
    """Base class for Excalidraw elements."""

    type: str
    x: float
    y: float
    id: str = field(default_factory=generate_id)
    width: float = 0
    height: float = 0
    angle: float = 0
    strokeColor: str = COLORS["black"]
    backgroundColor: str = "transparent"
    fillStyle: str = "solid"
    strokeWidth: int = 2
    strokeStyle: str = "solid"
    roughness: int = 1
    opacity: int = 100
    groupIds: list = field(default_factory=list)
    roundness: Optional[dict] = None
    seed: int = field(default_factory=lambda: int(uuid.uuid4().int % 2147483647))
    version: int = 1
    versionNonce: int = field(default_factory=lambda: int(uuid.uuid4().int % 2147483647))
    isDeleted: bool = False
    boundElements: Optional[list] = None
    updated: int = 1704067200000
    link: Optional[str] = None
    locked: bool = False

    def to_dict(self) -> dict:
        """Convert to Excalidraw JSON format."""
        d = {
            "type": self.type,
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "angle": self.angle,
            "strokeColor": self.strokeColor,
            "backgroundColor": self.backgroundColor,
            "fillStyle": self.fillStyle,
            "strokeWidth": self.strokeWidth,
            "strokeStyle": self.strokeStyle,
            "roughness": self.roughness,
            "opacity": self.opacity,
            "groupIds": self.groupIds,
            "seed": self.seed,
            "version": self.version,
            "versionNonce": self.versionNonce,
            "isDeleted": self.isDeleted,
            "boundElements": self.boundElements,
            "updated": self.updated,
            "link": self.link,
            "locked": self.locked,
        }
        if self.roundness:
            d["roundness"] = self.roundness
        return d


@dataclass
class Rectangle(ExcalidrawElement):
    """A rectangle shape."""

    def __init__(self, x: float, y: float, width: float, height: float, **kwargs):
        super().__init__(type="rectangle", x=x, y=y, width=width, height=height, **kwargs)
        self.roundness = {"type": 3}


@dataclass
class Ellipse(ExcalidrawElement):
    """An ellipse/circle shape."""

    def __init__(self, x: float, y: float, width: float, height: float, **kwargs):
        super().__init__(type="ellipse", x=x, y=y, width=width, height=height, **kwargs)


@dataclass
class Text(ExcalidrawElement):
    """A text element."""

    text: str = ""
    fontSize: int = 20
    fontFamily: int = 1  # 1=Hand-drawn, 2=Normal, 3=Code
    textAlign: str = "center"
    verticalAlign: str = "middle"
    containerId: Optional[str] = None
    originalText: str = ""
    lineHeight: float = 1.25

    def __init__(self, x: float, y: float, text: str, fontSize: int = 20, containerId: Optional[str] = None, **kwargs):
        super().__init__(type="text", x=x, y=y, **kwargs)
        self.text = text
        self.originalText = text
        self.fontSize = fontSize
        self.containerId = containerId
        # Estimate width/height based on text
        lines = text.split('\n')
        max_line = max(lines, key=len)
        self.width = len(max_line) * fontSize * 0.6
        self.height = fontSize * 1.5 * len(lines)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "text": self.text,
            "fontSize": self.fontSize,
            "fontFamily": self.fontFamily,
            "textAlign": self.textAlign,
            "verticalAlign": self.verticalAlign,
            "containerId": self.containerId,
            "originalText": self.originalText,
            "lineHeight": self.lineHeight,
        })
        return d


@dataclass
class Arrow(ExcalidrawElement):
    """An arrow element."""

    points: list = field(default_factory=list)
    startArrowhead: Optional[str] = None
    endArrowhead: str = "arrow"
    startBinding: Optional[dict] = None
    endBinding: Optional[dict] = None

    def __init__(self, x: float, y: float, points: list, **kwargs):
        super().__init__(type="arrow", x=x, y=y, **kwargs)
        self.points = points
        # Calculate width/height from points
        if points:
            xs = [p[0] for p in points]
            ys = [p[1] for p in points]
            self.width = max(xs) - min(xs)
            self.height = max(ys) - min(ys)

    def to_dict(self) -> dict:
        d = super().to_dict()
        d.update({
            "points": self.points,
            "startArrowhead": self.startArrowhead,
            "endArrowhead": self.endArrowhead,
            "startBinding": self.startBinding,
            "endBinding": self.endBinding,
        })
        return d


class ExcalidrawDiagram:
    """Builder for Excalidraw diagrams."""

    def __init__(self):
        self.elements = []

    def add(self, element: ExcalidrawElement) -> str:
        """Add an element and return its ID."""
        self.elements.append(element)
        return element.id

    def add_box_with_text(
        self,
        x: float,
        y: float,
        text: str,
        width: float = 150,
        height: float = 60,
        bg_color: str = COLORS["light_blue"],
        stroke_color: str = COLORS["blue"],
        font_size: int = 18,
    ) -> str:
        """Add a rectangle with centered text. Returns the rectangle ID."""
        rect = Rectangle(
            x=x, y=y, width=width, height=height,
            backgroundColor=bg_color,
            strokeColor=stroke_color,
        )
        rect_id = self.add(rect)

        # Center the text in the box
        text_elem = Text(
            x=x + width/2 - len(text) * font_size * 0.3,
            y=y + height/2 - font_size * 0.75,
            text=text,
            fontSize=font_size,
            strokeColor=stroke_color,
            containerId=rect_id,
        )
        self.add(text_elem)

        # Update rect to know about its text
        rect.boundElements = [{"id": text_elem.id, "type": "text"}]

        return rect_id

    def add_arrow_between(
        self,
        start_x: float,
        start_y: float,
        end_x: float,
        end_y: float,
        color: str = COLORS["gray"],
        label: Optional[str] = None,
    ) -> str:
        """Add an arrow from start to end point."""
        arrow = Arrow(
            x=start_x,
            y=start_y,
            points=[[0, 0], [end_x - start_x, end_y - start_y]],
            strokeColor=color,
        )
        arrow_id = self.add(arrow)

        # Add label if provided
        if label:
            mid_x = (start_x + end_x) / 2
            mid_y = (start_y + end_y) / 2 - 25
            text = Text(
                x=mid_x - len(label) * 6,
                y=mid_y,
                text=label,
                fontSize=14,
                strokeColor=color,
            )
            self.add(text)

        return arrow_id

    def add_elbow_arrow(
        self,
        start_x: float,
        start_y: float,
        end_x: float,
        end_y: float,
        color: str = COLORS["gray"],
        direction: str = "right-down",
    ) -> str:
        """Add a 90-degree elbow arrow."""
        if direction == "right-down":
            mid_x = end_x
            points = [[0, 0], [mid_x - start_x, 0], [mid_x - start_x, end_y - start_y]]
        elif direction == "down-right":
            mid_y = end_y
            points = [[0, 0], [0, mid_y - start_y], [end_x - start_x, mid_y - start_y]]
        else:
            points = [[0, 0], [end_x - start_x, end_y - start_y]]

        arrow = Arrow(
            x=start_x,
            y=start_y,
            points=points,
            strokeColor=color,
        )
        return self.add(arrow)

    def to_json(self) -> dict:
        """Export as Excalidraw JSON format."""
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": [e.to_dict() for e in self.elements],
            "appState": {
                "gridSize": None,
                "viewBackgroundColor": "#ffffff",
            },
            "files": {},
        }

    def save(self, filepath: str):
        """Save to an .excalidraw file."""
        with open(filepath, "w") as f:
            json.dump(self.to_json(), f, indent=2)
        print(f"Created: {filepath}")


# =============================================================================
# GitHub Workflow Diagrams
# =============================================================================

def create_basic_git_workflow():
    """Create: Clone → Edit → Commit → Push diagram."""
    diagram = ExcalidrawDiagram()

    # Title
    title = Text(x=200, y=30, text="Basic Git Workflow", fontSize=28, strokeColor=COLORS["black"])
    diagram.add(title)

    # Boxes
    box_y = 120
    box_w, box_h = 140, 60
    spacing = 200

    # Clone
    diagram.add_box_with_text(
        x=50, y=box_y, text="git clone",
        width=box_w, height=box_h,
        bg_color=COLORS["light_blue"], stroke_color=COLORS["blue"]
    )

    # Edit
    diagram.add_box_with_text(
        x=50 + spacing, y=box_y, text="Edit Files",
        width=box_w, height=box_h,
        bg_color=COLORS["light_green"], stroke_color=COLORS["green"]
    )

    # Add + Commit
    diagram.add_box_with_text(
        x=50 + spacing * 2, y=box_y, text="git add\ngit commit",
        width=box_w, height=box_h,
        bg_color=COLORS["light_orange"], stroke_color=COLORS["orange"]
    )

    # Push
    diagram.add_box_with_text(
        x=50 + spacing * 3, y=box_y, text="git push",
        width=box_w, height=box_h,
        bg_color=COLORS["light_purple"], stroke_color=COLORS["purple"]
    )

    # Arrows
    arrow_y = box_y + box_h / 2
    for i in range(3):
        start_x = 50 + box_w + spacing * i
        end_x = 50 + spacing * (i + 1)
        diagram.add_arrow_between(start_x, arrow_y, end_x, arrow_y)

    # Annotations
    annotations = [
        (50 + box_w/2 - 60, box_y + box_h + 20, "Copy repo\nto your computer"),
        (50 + spacing + box_w/2 - 50, box_y + box_h + 20, "Make your\nchanges"),
        (50 + spacing*2 + box_w/2 - 50, box_y + box_h + 20, "Save a\nsnapshot"),
        (50 + spacing*3 + box_w/2 - 60, box_y + box_h + 20, "Upload to\nGitHub"),
    ]
    for ax, ay, atext in annotations:
        ann = Text(x=ax, y=ay, text=atext, fontSize=14, strokeColor=COLORS["gray"])
        diagram.add(ann)

    return diagram


def create_fork_pr_workflow():
    """Create: Fork → Branch → PR → Merge workflow diagram."""
    diagram = ExcalidrawDiagram()

    # Title
    title = Text(x=180, y=30, text="Contributing to Open Source", fontSize=28, strokeColor=COLORS["black"])
    diagram.add(title)

    # Original repo (top)
    diagram.add_box_with_text(
        x=300, y=80, text="Original Repo",
        width=160, height=50,
        bg_color=COLORS["light_gray"], stroke_color=COLORS["gray"]
    )

    # Fork arrow down
    diagram.add_arrow_between(380, 130, 380, 170, label="Fork")

    # Your fork
    diagram.add_box_with_text(
        x=300, y=180, text="Your Fork",
        width=160, height=50,
        bg_color=COLORS["light_blue"], stroke_color=COLORS["blue"]
    )

    # Clone arrow down
    diagram.add_arrow_between(380, 230, 380, 270, label="Clone")

    # Local repo
    diagram.add_box_with_text(
        x=300, y=280, text="Local Copy",
        width=160, height=50,
        bg_color=COLORS["light_green"], stroke_color=COLORS["green"]
    )

    # Branch + Edit (right side)
    diagram.add_box_with_text(
        x=520, y=280, text="New Branch",
        width=140, height=50,
        bg_color=COLORS["light_orange"], stroke_color=COLORS["orange"]
    )

    # Arrow to branch
    diagram.add_arrow_between(460, 305, 520, 305, label="branch")

    # Edit arrow down
    diagram.add_arrow_between(590, 330, 590, 380, label="edit")

    # Make changes
    diagram.add_box_with_text(
        x=520, y=390, text="Your Changes",
        width=140, height=50,
        bg_color=COLORS["light_orange"], stroke_color=COLORS["orange"]
    )

    # Push arrow up to fork
    diagram.add_elbow_arrow(520, 415, 460, 205, direction="down-right")
    push_label = Text(x=480, y=350, text="push", fontSize=14, strokeColor=COLORS["gray"])
    diagram.add(push_label)

    # PR arrow from fork to original
    diagram.add_arrow_between(380, 180, 380, 130, color=COLORS["purple"])
    pr_label = Text(x=390, y=145, text="Pull Request", fontSize=14, strokeColor=COLORS["purple"])
    diagram.add(pr_label)

    return diagram


def create_repo_structure():
    """Create a diagram showing GitHub repository structure."""
    diagram = ExcalidrawDiagram()

    # Title
    title = Text(x=150, y=30, text="What's in a GitHub Repository?", fontSize=28, strokeColor=COLORS["black"])
    diagram.add(title)

    # Main repo box
    diagram.add_box_with_text(
        x=50, y=80, text="my-project/",
        width=600, height=350,
        bg_color="#f8f9fa", stroke_color=COLORS["gray"]
    )

    # Files and folders
    items = [
        (80, 130, "README.md", COLORS["light_blue"], COLORS["blue"], "Explains your project"),
        (80, 200, ".gitignore", COLORS["light_gray"], COLORS["gray"], "Files Git should ignore"),
        (80, 270, "src/", COLORS["light_green"], COLORS["green"], "Your code lives here"),
        (350, 130, "LICENSE", COLORS["light_purple"], COLORS["purple"], "How others can use it"),
        (350, 200, "requirements.txt", COLORS["light_orange"], COLORS["orange"], "Dependencies needed"),
        (350, 270, ".github/", COLORS["light_red"], COLORS["red"], "GitHub Actions & settings"),
    ]

    for x, y, name, bg, stroke, desc in items:
        diagram.add_box_with_text(
            x=x, y=y, text=name,
            width=130, height=45,
            bg_color=bg, stroke_color=stroke,
            font_size=16
        )
        desc_text = Text(x=x + 140, y=y + 12, text=desc, fontSize=14, strokeColor=COLORS["gray"])
        diagram.add(desc_text)

    # Bottom note
    note = Text(
        x=100, y=360,
        text="Tip: Every repo should have a README!",
        fontSize=16,
        strokeColor=COLORS["blue"]
    )
    diagram.add(note)

    return diagram


def create_branches_diagram():
    """Create a diagram explaining Git branches."""
    diagram = ExcalidrawDiagram()

    # Title
    title = Text(x=200, y=30, text="Git Branches Explained", fontSize=28, strokeColor=COLORS["black"])
    diagram.add(title)

    # Main branch line
    main_y = 150
    for i in range(5):
        x = 80 + i * 120
        circle = Ellipse(
            x=x, y=main_y, width=30, height=30,
            backgroundColor=COLORS["light_blue"],
            strokeColor=COLORS["blue"]
        )
        diagram.add(circle)
        if i < 4:
            diagram.add_arrow_between(x + 30, main_y + 15, x + 120, main_y + 15, color=COLORS["blue"])

    main_label = Text(x=30, y=main_y + 5, text="main", fontSize=16, strokeColor=COLORS["blue"])
    diagram.add(main_label)

    # Feature branch
    branch_y = 280
    branch_start_x = 200  # Branches from 2nd commit

    # Arrow down to branch
    diagram.add_arrow_between(branch_start_x + 15, main_y + 30, branch_start_x + 15, branch_y, color=COLORS["green"])

    # Branch commits
    for i in range(3):
        x = branch_start_x + i * 120
        circle = Ellipse(
            x=x, y=branch_y, width=30, height=30,
            backgroundColor=COLORS["light_green"],
            strokeColor=COLORS["green"]
        )
        diagram.add(circle)
        if i < 2:
            diagram.add_arrow_between(x + 30, branch_y + 15, x + 120, branch_y + 15, color=COLORS["green"])

    branch_label = Text(x=100, y=branch_y + 5, text="feature", fontSize=16, strokeColor=COLORS["green"])
    diagram.add(branch_label)

    # Merge arrow back to main
    merge_x = branch_start_x + 2 * 120
    main_merge_x = 80 + 4 * 120
    diagram.add_arrow_between(merge_x + 30, branch_y + 15, main_merge_x + 15, main_y + 30, color=COLORS["purple"])

    merge_label = Text(x=merge_x + 60, y=branch_y - 50, text="merge", fontSize=14, strokeColor=COLORS["purple"])
    diagram.add(merge_label)

    # Annotations
    annotations = [
        (80, main_y + 50, "Your stable\ncode"),
        (branch_start_x, branch_y + 50, "Work on new\nfeatures here"),
        (main_merge_x - 30, main_y + 50, "Combine\nchanges"),
    ]
    for ax, ay, atext in annotations:
        ann = Text(x=ax, y=ay, text=atext, fontSize=14, strokeColor=COLORS["gray"])
        diagram.add(ann)

    return diagram


def create_github_vs_git():
    """Create a diagram showing Git vs GitHub."""
    diagram = ExcalidrawDiagram()

    # Title
    title = Text(x=200, y=30, text="Git vs GitHub", fontSize=28, strokeColor=COLORS["black"])
    diagram.add(title)

    # Git section (left)
    diagram.add_box_with_text(
        x=50, y=80, text="Git",
        width=250, height=280,
        bg_color="#e7f5ff", stroke_color=COLORS["blue"]
    )

    git_items = [
        "Version control tool",
        "Runs on your computer",
        "Tracks file changes",
        "Free & open source",
        "Works offline",
    ]
    for i, item in enumerate(git_items):
        t = Text(x=70, y=130 + i * 40, text=f"• {item}", fontSize=16, strokeColor=COLORS["blue"])
        diagram.add(t)

    # GitHub section (right)
    diagram.add_box_with_text(
        x=400, y=80, text="GitHub",
        width=250, height=280,
        bg_color="#fff3bf", stroke_color=COLORS["orange"]
    )

    github_items = [
        "Website / cloud service",
        "Stores repos online",
        "Collaboration features",
        "Pull requests & issues",
        "Free for public repos",
    ]
    for i, item in enumerate(github_items):
        t = Text(x=420, y=130 + i * 40, text=f"• {item}", fontSize=16, strokeColor=COLORS["orange"])
        diagram.add(t)

    # Connection arrow
    diagram.add_arrow_between(300, 220, 400, 220, color=COLORS["gray"])
    conn_label = Text(x=320, y=190, text="push/pull", fontSize=14, strokeColor=COLORS["gray"])
    diagram.add(conn_label)

    # Bottom summary
    summary = Text(
        x=120, y=400,
        text="Git = the tool    |    GitHub = where you share",
        fontSize=18,
        strokeColor=COLORS["black"]
    )
    diagram.add(summary)

    return diagram


# =============================================================================
# Main
# =============================================================================

def main():
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), "..", "diagrams")
    os.makedirs(output_dir, exist_ok=True)

    # Generate all diagrams
    diagrams = [
        ("basic-git-workflow", create_basic_git_workflow),
        ("fork-pr-workflow", create_fork_pr_workflow),
        ("repo-structure", create_repo_structure),
        ("git-branches", create_branches_diagram),
        ("git-vs-github", create_github_vs_git),
    ]

    print("Generating Excalidraw diagrams for GitHub education...\n")

    for name, creator_fn in diagrams:
        diagram = creator_fn()
        filepath = os.path.join(output_dir, f"{name}.excalidraw")
        diagram.save(filepath)

    print(f"\nDone! Created {len(diagrams)} diagrams in {output_dir}/")
    print("\nTo use these diagrams:")
    print("1. Open https://excalidraw.com")
    print("2. Click the menu (☰) → Open → select a .excalidraw file")
    print("3. Export as SVG/PNG for Reveal.js slides")


if __name__ == "__main__":
    main()
