# 🔌 API Reference — Triggering Workflows Programmatically

All workflows use the GitHub Actions [`workflow_dispatch`](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event) REST endpoint.

```
POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
```

**Base URL:** `https://api.github.com`  
**Repo:** `shezis/copilot-actions-hub`  
**Auth:** Personal Access Token (PAT) with `repo` + `workflow` scopes, or `GITHUB_TOKEN`

---

## 🤖 1. Unified Action (`copilot-unified.yml`)

Select one or more skills and MCP tools, pick an agent, and provide a free-text prompt.

### cURL

```bash
curl -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/copilot-unified.yml/dispatches \
  -d '{
    "ref": "main",
    "inputs": {
      "skill_report_writing": "true",
      "skill_ppt_generation": "true",
      "agent": "Product Manager",
      "prompt": "Analyze the competitive landscape for AI coding tools in 2025",
      "output_format": "markdown",
      "mcp_filesystem": "false",
      "mcp_web_search": "true",
      "mcp_github": "false"
    }
  }'
```

### GitHub CLI

```bash
gh workflow run copilot-unified.yml \
  --repo shezis/copilot-actions-hub \
  --ref main \
  --field skill_report_writing=true \
  --field skill_ppt_generation=false \
  --field agent="AI Engineer" \
  --field prompt="Write a technical deep-dive on RAG architecture patterns" \
  --field output_format=markdown \
  --field mcp_filesystem=false \
  --field mcp_web_search=false \
  --field mcp_github=false
```

### JavaScript (Octokit)

```javascript
import { Octokit } from "@octokit/rest";

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

await octokit.rest.actions.createWorkflowDispatch({
  owner: "shezis",
  repo: "copilot-actions-hub",
  workflow_id: "copilot-unified.yml",
  ref: "main",
  inputs: {
    skill_report_writing: "true",
    skill_ppt_generation: "true",
    agent: "Software Architect",
    prompt: "Document the system architecture and generate a presentation for stakeholders",
    output_format: "markdown",
    mcp_filesystem: "false",
    mcp_web_search: "false",
    mcp_github: "true",
  },
});
```

### Python (requests)

```python
import os
import requests

response = requests.post(
    "https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/copilot-unified.yml/dispatches",
    headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    },
    json={
        "ref": "main",
        "inputs": {
            "skill_report_writing": "true",
            "skill_ppt_generation": "false",
            "agent": "Security Engineer",
            "prompt": "Perform a security assessment report on OWASP Top 10 for our API",
            "output_format": "markdown",
            "mcp_filesystem": "false",
            "mcp_web_search": "true",
            "mcp_github": "false",
        },
    },
)
# 204 No Content = success
print(f"Status: {response.status_code}")
```

---

## 📝 2. Report Writing (`report-writing.yml`)

```bash
# ── cURL ──────────────────────────────────────────────────────────────────
curl -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/report-writing.yml/dispatches \
  -d '{
    "ref": "main",
    "inputs": {
      "topic": "State of LLMs in Enterprise Software 2025",
      "agent": "AI Engineer",
      "report_type": "Research",
      "format": "markdown",
      "depth": "Detailed (10-20 pages)",
      "additional_context": "Focus on cost, latency, and security trade-offs",
      "mcp_filesystem": "false",
      "mcp_web_search": "true",
      "mcp_github": "false"
    }
  }'
```

```bash
# ── GitHub CLI ────────────────────────────────────────────────────────────
gh workflow run report-writing.yml \
  --repo shezis/copilot-actions-hub \
  --ref main \
  --field topic="State of LLMs in Enterprise Software 2025" \
  --field agent="AI Engineer" \
  --field report_type="Research" \
  --field format="markdown" \
  --field depth="Detailed (10-20 pages)" \
  --field additional_context="Focus on cost, latency, and security trade-offs" \
  --field mcp_filesystem=false \
  --field mcp_web_search=true \
  --field mcp_github=false
```

```javascript
// ── JavaScript (Octokit) ──────────────────────────────────────────────────
await octokit.rest.actions.createWorkflowDispatch({
  owner: "shezis",
  repo: "copilot-actions-hub",
  workflow_id: "report-writing.yml",
  ref: "main",
  inputs: {
    topic: "State of LLMs in Enterprise Software 2025",
    agent: "AI Engineer",
    report_type: "Research",
    format: "markdown",
    depth: "Detailed (10-20 pages)",
    additional_context: "Focus on cost, latency, and security trade-offs",
    mcp_filesystem: "false",
    mcp_web_search: "true",
    mcp_github: "false",
  },
});
```

```python
# ── Python ────────────────────────────────────────────────────────────────
requests.post(
    "https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/report-writing.yml/dispatches",
    headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    },
    json={
        "ref": "main",
        "inputs": {
            "topic": "State of LLMs in Enterprise Software 2025",
            "agent": "AI Engineer",
            "report_type": "Research",
            "format": "markdown",
            "depth": "Detailed (10-20 pages)",
            "additional_context": "Focus on cost, latency, and security trade-offs",
            "mcp_filesystem": "false",
            "mcp_web_search": "true",
            "mcp_github": "false",
        },
    },
)
```

---

## 📊 3. PPT Generation (`ppt-generation.yml`)

```bash
# ── cURL ──────────────────────────────────────────────────────────────────
curl -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/ppt-generation.yml/dispatches \
  -d '{
    "ref": "main",
    "inputs": {
      "topic": "Introducing Our AI Platform to Investors",
      "agent": "Product Manager",
      "presentation_type": "Pitch Deck",
      "slides_count": "15",
      "audience": "Investors",
      "include_speaker_notes": "true",
      "additional_context": "Emphasise TAM, traction metrics, and roadmap",
      "mcp_filesystem": "false",
      "mcp_web_search": "false",
      "mcp_github": "false"
    }
  }'
```

```bash
# ── GitHub CLI ────────────────────────────────────────────────────────────
gh workflow run ppt-generation.yml \
  --repo shezis/copilot-actions-hub \
  --ref main \
  --field topic="Introducing Our AI Platform to Investors" \
  --field agent="Product Manager" \
  --field presentation_type="Pitch Deck" \
  --field slides_count="15" \
  --field audience="Investors" \
  --field include_speaker_notes=true \
  --field additional_context="Emphasise TAM, traction metrics, and roadmap" \
  --field mcp_filesystem=false \
  --field mcp_web_search=false \
  --field mcp_github=false
```

```javascript
// ── JavaScript (Octokit) ──────────────────────────────────────────────────
await octokit.rest.actions.createWorkflowDispatch({
  owner: "shezis",
  repo: "copilot-actions-hub",
  workflow_id: "ppt-generation.yml",
  ref: "main",
  inputs: {
    topic: "Introducing Our AI Platform to Investors",
    agent: "Product Manager",
    presentation_type: "Pitch Deck",
    slides_count: "15",
    audience: "Investors",
    include_speaker_notes: "true",
    additional_context: "Emphasise TAM, traction metrics, and roadmap",
    mcp_filesystem: "false",
    mcp_web_search: "false",
    mcp_github: "false",
  },
});
```

```python
# ── Python ────────────────────────────────────────────────────────────────
requests.post(
    "https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/ppt-generation.yml/dispatches",
    headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    },
    json={
        "ref": "main",
        "inputs": {
            "topic": "Introducing Our AI Platform to Investors",
            "agent": "Product Manager",
            "presentation_type": "Pitch Deck",
            "slides_count": "15",
            "audience": "Investors",
            "include_speaker_notes": "true",
            "additional_context": "Emphasise TAM, traction metrics, and roadmap",
            "mcp_filesystem": "false",
            "mcp_web_search": "false",
            "mcp_github": "false",
        },
    },
)
```

---

## 📋 Input Reference

### Agents (valid values for `agent` field)
| Value | Persona |
|---|---|
| `Default Copilot` | General-purpose |
| `AI Engineer` | LLMs, ML, data pipelines |
| `Backend Developer` | APIs, DBs, performance |
| `Code Reviewer` | Quality, security, refactoring |
| `Frontend Developer` | UI/UX, accessibility |
| `Product Manager` | KPIs, roadmaps, business value |
| `Security Engineer` | OWASP, risk, compliance |
| `Software Architect` | System design, ADRs, C4 |

### Unified Workflow — Skills (boolean)
| Field | Default | Description |
|---|---|---|
| `skill_report_writing` | `"false"` | Enable Report Writing skill |
| `skill_ppt_generation` | `"false"` | Enable PPT Generation skill |

> ⚠️ At least one skill must be `"true"` or the workflow will fail fast.

### MCP Tools (boolean, all workflows)
| Field | Default | Requires |
|---|---|---|
| `mcp_filesystem` | `"false"` | No secrets needed |
| `mcp_web_search` | `"false"` | `BRAVE_API_KEY` repo secret |
| `mcp_github` | `"false"` | `GITHUB_TOKEN` (auto-available) |

### Report Types (`report_type`)
`Technical` · `Business` · `Research` · `Executive Summary` · `Competitive Analysis` · `Risk Assessment`

### Presentation Types (`presentation_type`)
`Technical Deep Dive` · `Executive Summary` · `Pitch Deck` · `Educational / Tutorial` · `Status Update` · `Competitive Analysis`

### Output Formats (`format` / `output_format`)
`markdown` · `html` · `pdf` · `pptx`

---

## 🔑 Authentication

### Option A — Personal Access Token (PAT)
```bash
# Fine-grained PAT needs: Actions (write), Contents (write), Issues (write)
export GITHUB_TOKEN=github_pat_xxxxxxxxxxxx
```

### Option B — GitHub CLI (no token needed if already authed)
```bash
gh auth login
gh workflow run ...   # uses your existing gh session
```

### Option C — GitHub Actions (calling from another workflow)
```yaml
- name: Trigger Copilot action
  run: |
    gh workflow run copilot-unified.yml \
      --repo shezis/copilot-actions-hub \
      --ref main \
      --field skill_report_writing=true \
      --field agent="Product Manager" \
      --field prompt="Weekly status report for sprint ${{ env.SPRINT }}"
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## 📡 Polling for Completion

The dispatch endpoint returns `204 No Content` immediately. To wait for the run to finish:

```bash
# 1. Trigger and capture run ID
gh workflow run copilot-unified.yml \
  --repo shezis/copilot-actions-hub \
  --ref main \
  --field skill_report_writing=true \
  --field agent="Product Manager" \
  --field prompt="Q2 market analysis"

# 2. Get the latest run ID
RUN_ID=$(gh run list \
  --repo shezis/copilot-actions-hub \
  --workflow copilot-unified.yml \
  --limit 1 \
  --json databaseId \
  --jq '.[0].databaseId')

# 3. Watch until complete
gh run watch $RUN_ID --repo shezis/copilot-actions-hub

# 4. Check outcome
gh run view $RUN_ID --repo shezis/copilot-actions-hub
```

```python
import time

def trigger_and_wait(workflow_id: str, inputs: dict) -> dict:
    # Trigger
    requests.post(
        f"https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/{workflow_id}/dispatches",
        headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "Accept": "application/vnd.github+json"},
        json={"ref": "main", "inputs": inputs},
    )

    time.sleep(3)  # brief pause for GitHub to register the run

    # Get latest run
    runs = requests.get(
        f"https://api.github.com/repos/shezis/copilot-actions-hub/actions/workflows/{workflow_id}/runs",
        headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "Accept": "application/vnd.github+json"},
    ).json()
    run = runs["workflow_runs"][0]

    # Poll until complete
    while run["status"] not in ("completed", "cancelled", "failure"):
        time.sleep(10)
        run = requests.get(
            run["url"],
            headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}", "Accept": "application/vnd.github+json"},
        ).json()
        print(f"  status: {run['status']}")

    print(f"✅ Run {run['id']} completed: {run['conclusion']}")
    print(f"   {run['html_url']}")
    return run
```
