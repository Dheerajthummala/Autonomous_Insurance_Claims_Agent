MANDATORY_FIELDS = [
    "Policy Number",
    "Incident Date",
    "Claim Type",
    "Estimated Damage"
]

def find_missing_fields(fields: dict) -> list:
    return [f for f in MANDATORY_FIELDS if not fields.get(f)]
