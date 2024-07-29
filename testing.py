def generate_tests(intent, entities):
    if intent == "create_api":
        endpoints = entities.get("endpoints", [])
        tests = [create_test(endpoint) for endpoint in endpoints]
        return tests
    return []

def create_test(endpoint):
    # Generate a test for the given endpoint
    endpoint_name = endpoint.replace(" ", "_").replace(".", "")
    return f"""
def test_{endpoint_name}():
    response = client.get('/{endpoint_name}')
    assert response.status_code == 200
"""

