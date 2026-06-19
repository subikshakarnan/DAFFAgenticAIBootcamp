# Ministerial Brief Drafting Standards

**Document type:** Verification knowledge base for the Ministerial Brief Agent
**Status:** ILLUSTRATIVE — created for the DEWR Agentic AI Bootcamp. These rules are a simplified teaching stand-in and are **not** official DPMC or Australian Government policy.

---

## How this document is used

The Verification Agent runs Retrieval-Augmented Generation (RAG) over this document. For each draft brief it retrieves the relevant rule, then checks the draft against that rule and reports a pass or a specific failure. Verification is grounded in these documented rules — it is **not** the model "deciding" whether a brief feels compliant. That grounding is what makes the check defensible.

---

## The 8 rules

### Rule 1 — Purpose statement
The PURPOSE must be a single sentence beginning with **"To inform"**, **"To advise"**, or **"To seek approval"**.
*Compliant example:* "PURPOSE: To inform the Minister of current healthcare workforce conditions ahead of the meeting with the Australian Medical Association."

### Rule 2 — Key points limit
The KEY POINTS section must contain a **maximum of 5 bullet points**. Briefs that exceed five points are returned for tightening.

### Rule 3 — Statistic citation
Every statistic must cite its **source and period**, for example "(ABS Labour Force Survey, April 2026)" or "(JSA Occupation Shortage List 2025)". An uncited number is a failure.

### Rule 4 — Financial implications
A **FINANCIAL IMPLICATIONS** section is required, even when there are none. If there are none, it must explicitly state "No direct financial implications."

### Rule 5 — Classification marking
A classification marking must appear at the **top of the brief**: one of **OFFICIAL** or **OFFICIAL: Sensitive**.

### Rule 6 — Background length
The BACKGROUND section must be **300 words or fewer**.

### Rule 7 — Contact officer
A contact officer must appear at the **end of the document** with a **name, title, phone number, and date**.

### Rule 8 — Action type
The brief must state an action type: **"For Noting"** or **"For Decision/Approval"**.

---

## Verification output

For each draft the Verification Agent returns:
- **pass:** true only if all 8 rules are satisfied
- **failures:** a list naming each failed rule and what was missing (e.g. "Rule 3 — the figure '48% of healthcare occupations in shortage' has no source citation")

When `pass` is false, the Orchestrator returns the failure list to the Writing Agent for revision (maximum 2 retries).
