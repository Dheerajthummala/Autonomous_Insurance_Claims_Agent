from pypdf import PdfReader
import requests
import json


def extract_pdf_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text
import re


def extract_fields_with_ollama(document_text: str) -> dict:
    prompt = f"""
You are an insurance FNOL extraction assistant.

Extract the following fields from the document below.
Return ONLY valid JSON. Do NOT include explanations or markdown.

If a field is missing or unclear, set its value to null.

Fields:
- Policy Number
- Policyholder Name
- Incident Date
- Incident Time
- Location
- Description
- Claim Type
- Estimated Damage
- Asset Type
- Asset ID
- Injuries Present (yes/no)

Document:
\"\"\"
{document_text}
\"\"\"

JSON:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    raw_text = response.json().get("response", "").strip()

    if not raw_text:
        raise ValueError("Ollama returned empty response")

    # 🔑 Extract JSON block safely
    match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in Ollama response")

    json_text = match.group(0)

    return json.loads(json_text)
