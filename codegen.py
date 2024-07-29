def generate_code_template(intent, entities):
    if intent == "create_api":
        return create_api_template(entities)
    return ""

def create_api_template(entities):
    endpoints = entities.get("endpoints", [])
    code = f"""
from flask import Flask

app = Flask(__name__)

# Define endpoints
{generate_endpoints_code(endpoints)}

if __name__ == "__main__":
    app.run(debug=True)
"""
    return code

def generate_endpoints_code(endpoints):
    code = ""
    for endpoint in endpoints:
        endpoint_name = endpoint.replace(" ", "_").replace(".", "")
        code += f"""
@app.route('/{endpoint_name}', methods=['GET', 'POST'])
def {endpoint_name}():
    return "{endpoint} endpoint"
"""
    return code

