from typing import Any, Dict, Tuple, Union

REQUIRED_FIELDS = ("principal", "rate", "time")


def validate_simple_interest_payload(data: Any) -> Union[str, Dict[str, float]]:
    """Validate JSON input for the simple interest endpoint."""
    if not isinstance(data, dict):
        return "Request JSON body must be an object."

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        return f"Missing required field(s): {', '.join(missing_fields)}."

    validated: Dict[str, float] = {}
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        value = data[field]

        if isinstance(value, bool):
            errors.append(f"{field} must be a numeric value.")
            continue

        try:
            numeric_value = float(value)
        except (TypeError, ValueError):
            errors.append(f"{field} must be numeric.")
            continue

        if numeric_value < 0:
            errors.append(f"{field} must be non-negative.")
            continue

        validated[field] = numeric_value

    if errors:
        return " ".join(errors)

    return validated
