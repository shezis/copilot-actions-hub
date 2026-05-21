# 🤖 Copilot Actions Hub — Workflow & Pricing Guide

> A reference for understanding how the system works end-to-end and what each operation costs.

---

## 📊 End-to-End Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          YOU (GitHub UI)                                │
│                                                                         │
│   Actions → Select Workflow → "Run workflow" → Fill inputs:             │
│   ┌──────────────┬────────────────────┬──────────────┬───────────────┐  │
│   │   Skill      │      Agent         │    Prompt    │  MCP Profile  │  │
│   │ Report Writing│  Product Manager  │ "Analyze..." │     none      │  │
│   └──────────────┴────────────────────┴──────────────┴───────────────┘  │
└─────────────────────────┬───────────────────────────────────────────────┘
                          │  workflow_dispatch
                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     GITHUB ACTIONS RUNNER                               │
│                      (~10–30 seconds, FREE)                             │
│                                                                         │
│  Step 1: Resolve agent slug  (e.g. "product-manager")                  │
│  Step 2: Assemble issue body with:                                      │
│          • Your prompt                                                  │
│          • ▶ Skill reference  → .github/copilot/skills/<skill>.md      │
│          • ▶ Agent reference  → .github/copilot/agents/<agent>.md      │
│          • ▶ Output path      → reports/ or presentations/             │
│          • ▶ MCP profile      → .github/copilot/mcp_profiles/<p>.json  │
│  Step 3: Create GitHub Issue  (assigned to @copilot)                   │
│  Step 4: Apply labels: copilot, skill:*, agent:*, type:*, audience:*   │
└─────────────────────────┬───────────────────────────────────────────────┘
                          │  Issue assigned to @copilot
                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   GITHUB COPILOT CODING AGENT                           │
│                        (Credits consumed here)                          │
│                                                                         │
│  Phase 1 — Environment Setup  (copilot-setup-steps.yml)                │
│  ├── actions/checkout@v4                                                │
│  ├── setup-python → pip install python-pptx markdown2 reportlab        │
│  ├── apt install pandoc                                                 │
│  └── setup-node  (for MCP servers, if active)                          │
│                                                                         │
│  Phase 2 — Context Loading                                              │
│  ├── Read issue body         (prompt + parameters)                      │
│  ├── Read skill definition   (.github/copilot/skills/<skill>.md)       │
│  ├── Read agent persona      (.github/copilot/agents/<agent>.md)       │
│  └── Read MCP config         (.github/copilot/mcp_config.json)         │
│                                                                         │
│  Phase 3 — Execution                                                    │
│  ├── Apply agent persona     (product manager lens, tone, structure)    │
│  ├── Generate content        (LLM calls → tokens consumed)              │
│  ├── Write output file       (reports/ or presentations/)               │
│  └── Run python-pptx script  (for .pptx output)                        │
│                                                                         │
│  Phase 4 — Delivery                                                     │
│  ├── git commit output files                                            │
│  ├── Open Pull Request                                                  │
│  └── Link PR to original issue                                          │
└─────────────────────────┬───────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         YOU (Review & Merge)                            │
│                                                                         │
│   GitHub notifies you → Review PR → Merge → File in reports/ or        │
│   presentations/ is now on main branch                                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔀 Workflow Variations — Decision Guide

```
Need Copilot to do something?
│
├─► Simple / exploratory?
│       └─► Use: copilot-unified.yml
│           Inputs: skill + agent + free-text prompt
│
├─► Generating a document / report?
│       └─► Use: report-writing.yml
│           Inputs: topic + agent + report_type + format + depth
│
├─► Building a presentation?
│       └─► Use: ppt-generation.yml
│           Inputs: topic + agent + presentation_type + slides + audience
│
└─► Environment / tooling setup issue?
        └─► Edit: copilot-setup-steps.yml
            (Called automatically — not triggered manually)
```

---

## 🧑‍💼 Agent × Skill Matrix

| Agent            | Report Writing Style                          | PPT Generation Style                        |
|------------------|-----------------------------------------------|---------------------------------------------|
| Default Copilot  | Balanced, general-purpose                     | Standard structure                          |
| AI Engineer      | Benchmarks, model comparisons, code snippets  | Architecture diagrams, technical depth      |
| Backend Developer| API specs, perf metrics, DB schemas           | Systems diagrams, implementation steps      |
| Code Reviewer    | Finding-based, severity levels, recommendations| Issue highlights, remediation roadmap      |
| Frontend Developer| UX flows, accessibility, component breakdowns| Visual mockup refs, user journey slides    |
| Product Manager  | KPIs, OKRs, market analysis, roadmap          | Exec-friendly, story-driven, metrics-first  |
| Security Engineer| OWASP/NIST framing, risk ratings, CVEs        | Threat model slides, risk vs. remediation   |
| Software Architect| ADRs, C4 diagrams, trade-off analysis        | System context, component, deployment views |

---

## 💰 Pricing

### Component 1 — GitHub Actions Runner

| Repository Visibility | Cost |
|-----------------------|------|
| **Public** (this repo) | **FREE** — unlimited minutes on standard runners |
| Private | 2,000 min/month free → $0.008/min (Linux) after |

> Each workflow run takes **~10–30 seconds** (it only creates an issue — no heavy compute).  
> Even at private-repo rates: 30 sec = **$0.004 per run** — effectively negligible.

---

### Component 2 — GitHub Copilot Coding Agent (AI Credits)

**1 credit = $0.01 USD**

| Plan | Price | Included Credits | Overage |
|------|-------|-----------------|---------|
| Copilot Pro | $10/mo | 1,000 credits | $0.01/credit |
| Copilot Pro+ | $39/mo | 3,900 credits | $0.01/credit |
| Copilot Business | $19/user/mo | 1,900 credits/user | $0.01/credit |
| Copilot Enterprise | $39/user/mo | 3,900 credits/user | $0.01/credit |

Credits are pooled across your org and consumed by all agentic Copilot features (chat, coding agent, PR reviews, etc.).

---

### 📊 Estimated Credits per Task

Credits scale with **three factors**: Complexity, Context Size, and Output Length.

#### Report Writing

| Complexity | Context Loaded | Token Range | Credits | Cost |
|------------|---------------|-------------|---------|------|
| **Brief** (1–2 pages) | Skill + Agent files only | 8K–15K tokens | **15–30 credits** | $0.15–$0.30 |
| **Standard** (5–10 pages) | Skill + Agent + repo files | 20K–50K tokens | **50–120 credits** | $0.50–$1.20 |
| **Detailed** (10–20 pages) | Skill + Agent + multiple repo files + web | 60K–150K tokens | **150–400 credits** | $1.50–$4.00 |
| **Research-grade** | Full repo scan + external sources via MCP | 150K–500K tokens | **400–1,200 credits** | $4.00–$12.00 |

#### PPT Generation

| Complexity | Slides | Context Loaded | Token Range | Credits | Cost |
|------------|--------|---------------|-------------|---------|------|
| **Quick** | 5 | Skill + Agent | 10K–20K tokens | **20–50 credits** | $0.20–$0.50 |
| **Standard** | 10 | Skill + Agent + code samples | 30K–70K tokens | **80–180 credits** | $0.80–$1.80 |
| **Full deck** | 15–20 | Skill + Agent + repo + python-pptx exec | 80K–200K tokens | **200–500 credits** | $2.00–$5.00 |
| **Exec pitch** | 20–25 | Full context + iterative refinement | 200K–600K tokens | **500–1,500 credits** | $5.00–$15.00 |

#### Context Size Reference

| Context Scenario | What's Loaded | Token Range |
|-----------------|---------------|-------------|
| **Minimal** | Issue body + skill.md + agent.md | 5K–15K tokens |
| **Light** | + a few source files | 15K–40K tokens |
| **Medium** | + directory scan + multiple files | 40K–100K tokens |
| **Heavy** | + full repo traversal | 100K–300K tokens |
| **Max** | + MCP web search results + iteration loops | 300K–1M+ tokens |

---

### 📅 Monthly Budget Planning

| Usage Level | Tasks/Month | Typical Mix | Est. Credits Used | Best Plan |
|-------------|------------|-------------|-------------------|-----------|
| Light | 5–10 | Standard reports | 500–1,200 | Copilot Pro ($10) |
| Moderate | 10–25 | Mix of reports + PPTs | 1,500–4,000 | Copilot Pro+ ($39) |
| Heavy | 25–60 | Detailed reports + full decks | 4,000–15,000 | Copilot Business ($19/user) |
| Enterprise | 60+ | Automated pipelines | 15,000+ | Copilot Enterprise ($39/user) |

---

### 💡 Cost Optimisation Tips

1. **Be specific in your prompt** — a precise prompt = fewer iteration tokens
2. **Use Brief depth** for drafts, upgrade to Detailed only for final output
3. **Avoid MCP web search** unless external research is truly needed
4. **Reuse outputs** — reference a previous report instead of regenerating
5. **Monitor usage** at `github.com/settings/billing` → Copilot

---

## ⚠️ Prerequisites Checklist

- [ ] GitHub Copilot subscription active (any plan)
- [ ] Copilot Coding Agent enabled: **Repo Settings → Copilot → Coding agent → Enable**
- [ ] `GITHUB_TOKEN` permissions set to `issues: write`, `contents: write`, `pull-requests: write` *(already configured in all workflows)*
- [ ] For MCP web search: add `BRAVE_API_KEY` as a repo secret

---

*Last updated: May 2026 — pricing based on GitHub's AI Credits model (1 credit = $0.01). Always verify at [github.com/features/copilot](https://github.com/features/copilot) for latest rates.*
