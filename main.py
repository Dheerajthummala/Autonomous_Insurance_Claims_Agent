import json
from extractor import extract_pdf_text, extract_fields_with_ollama
from validator import find_missing_fields
from router import route_claim

PDF_PATH = "data\ACORD-Automobile-Loss-Notice-12.05.16.pdf"


def main():
    text = extract_pdf_text(PDF_PATH)
    # # with open("data/sample_fnol_filled.txt", "r", encoding="utf-8") as f:
    #     text = f.read()


    extracted_fields = extract_fields_with_ollama(text)

    missing_fields = find_missing_fields(extracted_fields)

    route, reason = route_claim(extracted_fields, missing_fields)

    output = {
        "extractedFields": extracted_fields,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reason
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
