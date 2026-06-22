# Building a Multi-Agent System with watsonx Orchestrate
Chapter 1 of the DEWR Agentic AI Bootcamp. Build a **Ministerial Brief Agent**: three agents that, from one request, gather data, draft a ministerial brief in the Department's standard format, and return it for human sign-off. No code required.

<!-- VIDEO PLACEHOLDER: lab walkthrough video link/thumbnail to be re-added -->

## The agents
| Agent | Role | Attach |
|---|---|---|
| Orchestrator (Ministerial Brief Agent) | Sequences the two sub-agents | Statistics + Writing agents as collaborators |
| Statistics Agent | Returns cited workforce figures | `healthcare-workforce-openapi.yaml` (OpenAPI tool) |
| Writing Agent | Drafts the brief in the standard format | `Ministerial Brief Format.docx` (knowledge base) |

## Provided files (`Ministerial Brief Agent/`)
- `healthcare-workforce-openapi.yaml` — OpenAPI spec, imported as the Statistics Agent's data tool (Python fallback: `healthcare_workforce_tool.py`)
- `Ministerial Brief Format.docx` — brief format and rules, uploaded as the Writing Agent's knowledge base
- `DPMC Brief Standards.md` — readable text version of the format
- `Agent Prompts.md` — descriptions and instructions for all three agents

## Build order
1. **Statistics Agent** — import the tool, paste its prompt, test it returns the figures.
2. **Writing Agent** — upload the format knowledge base, paste its prompt.
3. **Orchestrator** — add the two sub-agents as collaborators, paste its prompt.

## Run it
Brief the Minister on the current state of the healthcare workforce shortage ahead of the meeting with the AMA (Australian Medical Association).

The Orchestrator calls the Statistics Agent for data, passes it to the Writing Agent to draft against the format knowledge base, and returns the finished brief for sign-off. Full walkthrough: [Chapter 1 lab guide](https://monadil.github.io/DEWRAgenticAIBootcamp/orchestrate.html).

# Great resources:
- <a href='https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=getting-started-watsonx-orchestrate'>Getting Started Tutorial</a> - Official IBM documentation.
- <a href='https://developer.watson-orchestrate.ibm.com/'>Deep Dive into ADK</a> - This is ultra useful, it covers the Agent Development Kit.

# Who, When, Why?
👨🏾‍💻 Author: IBM Client Engineering <br />
📅 Version: 2.x<br />
📜 License: This project is licensed under the MIT License </br>
