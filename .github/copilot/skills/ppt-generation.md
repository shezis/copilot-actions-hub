---
name: ppt-generation
description: Create presentation outlines, slide copy, python-pptx scripts, and finished PowerPoint decks saved in presentations/.
---

# PPT Generation Skill

## Overview and purpose
Use this skill when a task requires a presentation deck for business, technical, educational, or stakeholder communication. The goal is to generate concise, audience-aware slide content and, when needed, produce a real `.pptx` file programmatically.

This skill supports the full workflow: define the story, create the outline, write slide copy, generate speaker notes, create a Python script with `python-pptx`, and save both the deck and a Markdown outline.

## Capabilities
- Create presentation outlines and narrative flow.
- Write title slides, agenda slides, content slides, summary slides, Q&A slides, and references.
- Adapt tone and depth for pitch, technical, executive, or educational audiences.
- Apply the 6x6 rule to keep slides readable.
- Generate `python-pptx` scripts for automated deck creation.
- Produce actual `.pptx` files when the environment supports Python and `python-pptx`.
- Add speaker notes for presenter guidance.
- Save a Markdown outline alongside the slide deck.

## Standard slide structure
Unless the request specifies otherwise, use this order:
1. **Title slide**
2. **Agenda**
3. **Context / problem statement**
4. **Core content slides**
5. **Summary / recommendations**
6. **Q&A**
7. **References**

## The 6x6 rule
Default to the 6x6 rule for on-slide text:
- Maximum **6 bullets per slide**
- Maximum **6 words per bullet**

Use the slide itself for signals and structure, not dense prose. Put extra explanation in speaker notes.

## Output conventions
- Save PowerPoint files in `presentations/`.
- Save Markdown outlines in the same directory.
- Use consistent names, for example:
  - `presentations/<topic-slug>.pptx`
  - `presentations/<topic-slug>.md`
  - `presentations/<topic-slug>.py`

## Style guides by presentation type

### Pitch Deck
- Emphasize problem, market, solution, traction, business model, and ask.
- Use persuasive, high-level language.
- Keep visuals and headline statements strong.

### Technical Presentation
- Emphasize architecture, implementation, trade-offs, metrics, and risks.
- Use diagrams, sequence flows, and code excerpts sparingly.
- Assume a technically literate audience.

### Executive Presentation
- Focus on decisions, impact, KPIs, risks, budget, and timeline.
- Keep slides concise and recommendation-driven.
- Minimize jargon unless essential.

### Educational Presentation
- Organize slides progressively from basics to advanced concepts.
- Use examples, definitions, and recap slides.
- Favor clarity and instructional pacing.

## Speaker notes format
For each slide, include notes in this format:
- **Purpose:** why the slide exists
- **Key message:** the single takeaway
- **Talk track:** 2-5 short sentences expanding the slide
- **Optional prompt:** likely audience question or transition

## Using python-pptx
When an actual deck is requested, generate a Python script using `python-pptx`, then run it to create the `.pptx` file.

### Sample python-pptx template
```python
from pathlib import Path
from pptx import Presentation

output_dir = Path("presentations")
output_dir.mkdir(exist_ok=True)

prs = Presentation()

# Title slide
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "Project Update"
slide.placeholders[1].text = "Quarterly review"

# Agenda slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Agenda"
text_frame = slide.shapes.placeholders[1].text_frame
for item in ["Goals", "Progress", "Risks", "Next steps"]:
    p = text_frame.add_paragraph() if text_frame.text else text_frame.paragraphs[0]
    p.text = item

# Content slide
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Key Metrics"
body = slide.shapes.placeholders[1].text_frame
body.text = "Adoption up 18%"
for line in ["Latency down 22%", "Support tickets down 9%"]:
    p = body.add_paragraph()
    p.text = line

prs.save(output_dir / "project-update.pptx")
```

## Markdown outline companion file
Always save a Markdown outline next to the `.pptx` so the content remains reviewable in source control. The outline should include:
- deck title
- audience
- presentation objective
- slide-by-slide headings
- bullet content
- speaker notes

## Best practices
- Start with the audience and desired decision or outcome.
- Use one core message per slide.
- Prefer charts, diagrams, and tables over dense text.
- Keep terminology consistent across slides and notes.
- Make summaries explicit: what changed, why it matters, what happens next.
- Ensure the deck and Markdown outline tell the same story.

