def route_claim(fields: dict, missing_fields: list):
    description = (fields.get("Description") or "").lower()
    claim_type = (fields.get("Claim Type") or "").lower()
    injuries = (fields.get("Injuries Present") or "").lower()

    if missing_fields:
        return "Manual Review", "Mandatory fields are missing or unclear"

    if any(word in description for word in ["fraud", "staged", "inconsistent"]):
        return "Investigation Flag", "Suspicious keywords detected"

    if injuries == "yes" or claim_type == "injury":
        return "Specialist Queue", "Injury-related claim"

    try:
        if int(fields.get("Estimated Damage")) < 25000:
            return "Fast-track", "Estimated damage below 25,000"
    except:
        pass

