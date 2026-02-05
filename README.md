# Autonomous Insurance Claims Processing Agent

## Overview
This project is a lightweight agent that processes **FNOL (First Notice of Loss)** insurance documents and routes claims to the correct workflow.

The agent reads an FNOL document, extracts important details, checks for missing information, classifies the claim, and decides how it should be handled. It also explains why that decision was made.

---

## How It Works
FNOL documents (especially ACORD forms) often produce noisy text when extracted from PDFs.

To handle this reliably:
- **Ollama is used only to extract structured fields** from the raw document text
- **All validation and routing logic is rule-based**, written in plain Python

If required information is missing or unclear, the claim is safely routed to **Manual Review**.

---

## Routing Rules
- Missing mandatory fields → **Manual Review**
- Estimated damage < 25,000 → **Fast-track**
- Injury-related claims → **Specialist Queue**
- Fraud-related keywords → **Investigation Flag**

---

## Project Flow

---

→ Text Extraction
→ AI Field Extraction (Ollama)
→ Field Validation
→ Rule-Based Routing
→ JSON Output
## How to Run
```bash
pip install -r requirements.txt
python main.py
