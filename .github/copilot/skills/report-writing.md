---
name: report-writing
description: Write professional reports in Markdown, HTML, or PDF with clear structure, citations, and actionable recommendations.
---

# Report Writing Skill

## Overview and purpose
Use this skill when a task requires a polished report for technical, business, research, audit, or project communication. The goal is to help the coding agent produce complete, decision-ready reports that are easy to scan, professionally written, and saved in a predictable location.

This skill should transform raw notes, code findings, metrics, or research into an organized deliverable with clear conclusions, supporting evidence, and practical next steps.

## Capabilities
- Define report scope, audience, and objective before drafting.
- Create concise or in-depth reports based on a `depth` parameter.
- Produce reports in Markdown, HTML, or PDF.
- Structure content with executive summaries and logical sections.
- Synthesize technical evidence, benchmarks, risks, and recommendations.
- Add citations, references, links, tables, and code snippets where useful.
- Convert a completed Markdown report to PDF with Pandoc when `format=pdf`.
- Keep terminology consistent for the intended audience.

## Standard report structure
Always use this structure unless the request explicitly asks for a different outline:

1. **Executive Summary**  
   State the purpose, top findings, key recommendation, and business/technical impact.
2. **Table of Contents**  
   Include for medium or long reports.
3. **Introduction**  
   Explain context, scope, goals, assumptions, and methodology.
4. **Body**  
   Organize into clear themed sections and subsections.
5. **Findings**  
   Summarize observations, evidence, trends, risks, and opportunities.
6. **Conclusions**  
   Provide direct takeaways and recommended actions.
7. **References**  
   List citations, source links, documents, datasets, commits, or standards.

## Output file conventions
- Save report outputs in the `reports/` directory.
- Use the naming convention `reports/<topic-slug>.<ext>`.
- Prefer lowercase kebab-case for `<topic-slug>`.
- Examples:
  - `reports/api-performance-review.md`
  - `reports/customer-onboarding-analysis.html`
  - `reports/security-gap-assessment.pdf`

## Format guidelines

### Markdown
- Use ATX headings (`#`, `##`, `###`).
- Keep paragraphs short and scannable.
- Use bullet lists for takeaways and numbered lists for procedures.
- Use tables for comparisons, metrics, timelines, or options.
- Use fenced code blocks with language tags when showing code.

### HTML
- Preserve the same structure as the Markdown version.
- Use semantic elements when possible: `header`, `main`, `section`, `table`, `footer`.
- Keep styling simple, readable, and print-friendly.
- Ensure links, references, and headings remain accessible.

### PDF
- Draft the source content in Markdown first for easier revision.
- Convert the Markdown file to PDF with Pandoc when `format=pdf`.
- Ensure page titles, headings, tables, and code blocks render cleanly.
- Keep margins and typography professional and readable in print.

## Length guidelines by depth parameter
Use the requested `depth` to control coverage and length:

- `depth=brief`: 1-2 pages or 400-800 words. Focus on summary, top findings, and actions.
- `depth=standard`: 3-5 pages or 800-1,800 words. Include context, analysis, findings, and recommendations.
- `depth=deep`: 6+ pages or 1,800+ words. Add methodology, evidence, benchmarks, trade-offs, appendices, and fuller references.

If no depth is provided, default to `standard`.

## Quality standards
- Use professional, precise, audience-appropriate language.
- Support claims with citations, data, measurements, or traceable sources.
- Separate facts, analysis, assumptions, and recommendations clearly.
- Turn findings into actionable insights whenever possible.
- Avoid filler, repetition, unsupported claims, and vague conclusions.
- Make recommendations specific, prioritized, and outcome-oriented.

## PDF conversion with Pandoc
When `format=pdf`, create the Markdown source first, then convert it.

Example command:

```bash
mkdir -p reports
pandoc reports/<topic-slug>.md -o reports/<topic-slug>.pdf
```

If custom metadata or styling is needed, extend the command as appropriate, for example with title metadata or a PDF engine.

## Best practices
- Start with the audience: executive, technical, operational, or mixed.
- Write headings that communicate meaning, not just topic labels.
- Use tables for comparisons, rankings, requirements, and metric snapshots.
- Use code blocks only where they improve understanding.
- Highlight findings with callout bullets or short summary lists.
- Keep references complete enough for verification.
- End with clear next steps, owners, or decision points when relevant.

## Delivery checklist
Before finalizing, confirm that the report:
- Follows the standard section order.
- Is saved under `reports/` with the correct filename.
- Matches the requested format and depth.
- Includes citations and references.
- Contains clear findings, conclusions, and recommended actions.

