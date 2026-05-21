"""
generate_unified.py — Called by the copilot-unified workflow.
Reads config from environment variables, loads relevant skill definitions,
calls OpenRouter, and saves output to the appropriate directory.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error


def main():
    user_prompt      = os.environ["USER_PROMPT"]
    model            = os.environ["MODEL"]
    agent            = os.environ["AGENT"]
    fmt              = os.environ["FORMAT"]
    skill_report     = os.environ.get("SKILL_REPORT", "false").lower() == "true"
    skill_ppt        = os.environ.get("SKILL_PPT", "false").lower() == "true"
    mcp_ctx          = os.environ.get("MCP_CONTEXT", "")
    api_key          = os.environ.get("OPENROUTER_API_KEY", "")

    if not api_key:
        print("ERROR: OPENROUTER_API_KEY secret is not set.", file=sys.stderr)
        print("  Add it at: Settings -> Secrets -> Actions -> New repository secret", file=sys.stderr)
        sys.exit(1)

    agent_slug = agent.lower().replace(" ", "-")
    agent_def  = _read_file(f".github/copilot/agents/{agent_slug}.md") if agent_slug != "default" else ""

    skills_active = []
    skill_defs = []
    if skill_report:
        skills_active.append("Report Writing")
        skill_defs.append(_read_file(".github/copilot/skills/report-writing.md"))
    if skill_ppt:
        skills_active.append("PPT Generation")
        skill_defs.append(_read_file(".github/copilot/skills/ppt-generation.md"))

    system_prompt = _build_system_prompt(agent, agent_def, skills_active, skill_defs, fmt)
    full_prompt   = _build_user_prompt(user_prompt, mcp_ctx)

    print(f"Calling OpenRouter: {model} | Skills: {', '.join(skills_active)}")
    content, model_used, tokens = _call_openrouter(api_key, model, system_prompt, full_prompt)

    slug   = re.sub(r"-+", "-", re.sub(r"[^a-z0-9]", "-", user_prompt[:60].lower())).strip("-")
    ext    = "md" if fmt == "markdown" else fmt
    folder = "presentations" if (skill_ppt and not skill_report) else "reports"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{slug}.{ext}"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    _write_github_output({
        "filename": filename,
        "slug": slug,
        "model_used": model_used,
        "tokens": str(tokens),
    })
    print(f"Output saved: {filename}")
    print(f"Model: {model_used}  |  Tokens: {tokens}")


def _build_system_prompt(agent, agent_def, skills_active, skill_defs, fmt):
    parts = []
    if agent_def:
        parts.append(f"## Your Role\n{agent_def}")
    elif agent != "Default":
        parts.append(f"You are an expert {agent}.")
    else:
        parts.append("You are a versatile expert assistant.")

    for skill_def in skill_defs:
        if skill_def:
            parts.append(skill_def)

    if fmt == "markdown":
        parts.append("Format output as clean Markdown. Do NOT wrap in a code block.")
    elif fmt == "html":
        parts.append("Output a complete, styled HTML document.")

    parts.append(f"Active skills: {', '.join(skills_active)}")
    return "\n\n".join(parts)


def _build_user_prompt(user_prompt, mcp_ctx):
    parts = [user_prompt]
    if mcp_ctx and mcp_ctx.strip():
        parts.append(f"## Injected context\n{mcp_ctx}")
    return "\n\n".join(parts)


def _call_openrouter(api_key, model, system_prompt, user_prompt):
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        "max_tokens": 8000,
    }).encode()

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/shezis/copilot-actions-hub",
            "X-Title": "Copilot Actions Hub",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)

    if "error" in data:
        print(f"ERROR: OpenRouter: {data['error']['message']}", file=sys.stderr)
        sys.exit(1)

    content    = data["choices"][0]["message"]["content"]
    model_used = data.get("model", model)
    tokens     = data.get("usage", {}).get("total_tokens", "N/A")
    return content, model_used, tokens


def _read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def _write_github_output(kv: dict):
    output_file = os.environ.get("GITHUB_OUTPUT", "")
    if not output_file:
        return
    with open(output_file, "a", encoding="utf-8") as f:
        for key, value in kv.items():
            f.write(f"{key}={value}\n")


if __name__ == "__main__":
    main()
