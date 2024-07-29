def generate_deployment_script(intent, entities):
    if intent == "create_api":
        return """
# Dockerfile
FROM python:3.8-slim

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
"""
    return ""

