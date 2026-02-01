# TikTok Ad Creation AI Agent

## Overview

This project implements a **conversational AI agent** that helps a user create a TikTok Ad configuration step by step.

The focus of this assignment is **not UI or model training**, but:
- Prompt design thinking
- Business rule enforcement
- OAuth and API reasoning
- Graceful handling of failures

The agent is implemented as a **lightweight Python CLI** and uses **mocked TikTok Ads APIs**, as allowed by the assignment.

---

## What This Agent Does

The agent:
1. Collects ad inputs conversationally
2. Enforces TikTok business rules **before submission**
3. Produces a structured ad payload
4. Attempts submission via a mocked TikTok Ads API
5. Interprets and explains API failures clearly

---

## Conversational Flow

The agent collects the following inputs **step by step**:

1. **Campaign Name**
   - Required
   - Minimum 3 characters

2. **Objective**
   - Must be one of:
     - `Traffic`
     - `Conversions`

3. **Ad Text**
   - Required
   - Maximum 100 characters

4. **Call To Action (CTA)**
   - Required

5. **Music Choice**
   - Handled via explicit business logic (see below)

The agent maintains internal state and only validates once all required fields are collected.

---

## Music Logic (Primary Evaluation Area)

The agent fully supports all three music scenarios required by the assignment.

### Case A: Existing Music ID
- User provides a music ID
- The agent treats it as existing music
- The ID is validated via the API layer (mocked)
- If validation fails:
  - The agent explains why
  - Suggests what the user can do next

### Case B: Uploaded / Custom Music
- User selects `upload`
- The agent simulates a successful music upload
- A mock music ID is generated internally
- Submission proceeds normally

### Case C: No Music
- If objective = `Traffic`
  - No music is allowed
- If objective = `Conversions`
  - No music is **blocked before submission**
  - The agent explains the restriction and asks the user to choose a valid alternative

This rule is enforced **locally**, not after an API failure.

---

## Structured Output

When all validations pass, the agent produces a structured ad payload in the following format:

```json
{
  "campaign_name": "string",
  "objective": "Traffic | Conversions",
  "creative": {
    "text": "string",
    "cta": "string",
    "music": {
      "type": "existing | uploaded | none",
      "music_id": "string | null"
    }
  }
}
```
## Submission & API Failure Handling
Ad submission is attempted via a mocked TikTok Ads API.

The agent can simulate failures such as:
- Invalid OAuth token
- Invalid music ID
- Geo-restriction

Instead of returning raw errors, the agent:
- Interprets the failure
- Explains the cause in plain language
- Suggests corrective actions
- Prevents blind retries when not appropriate

This mirrors real-world external API behavior.

## Prompt Design

A prompts.py file is included to document:
- System-level constraints
- Business rule enforcement
- Structured output expectations

In this implementation, the agent logic is deterministic and handled in Python for predictability.
The prompts file demonstrates how the system would be integrated with an LLM if required.

## Tech Stack

Language: Python
Interface: CLI
LLM: Optional (not required for this implementation)
APIs: Mocked TikTok Ads API
Backend: Lightweight, no UI

No model fine-tuning, vector databases, or frontend components are used, as per assignment instructions.
