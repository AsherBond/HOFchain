def extract_intent(input_text):
    # Improved implementation using simple keyword matching
    if "create" in input_text.lower() and "api" in input_text.lower():
        return "create_api"
    # More complex logic or machine learning models can be used for better accuracy
    return "unknown"

def extract_entities(input_text):
    # Extract relevant entities such as "REST API", "endpoints", etc.
    entities = {}
    if "endpoints" in input_text:
        start_index = input_text.find("endpoints for") + len("endpoints for")
        endpoints_str = input_text[start_index:].strip()
        endpoints = [e.strip().rstrip(".") for e in endpoints_str.split("and")]
        entities["endpoints"] = endpoints
    return entities

def parse_input(input_text):
    intent = extract_intent(input_text)
    entities = extract_entities(input_text)
    return (intent, entities)

