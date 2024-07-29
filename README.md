# HOFchain - The HOF Cognitive Chain-of-thought Prompter

HOFchain is a Python library designed to simplify the process of higher-order functional cognitive computing for Natural Language Understanding (NLU) based code generation. This library integrates functionalities for parsing input, generating code, planning tasks, and more, enabling an end-to-end solution for automating software development tasks from natural language specifications.

## Features

- **NLU Parsing**: Extracts intent and entities from natural language input.
- **Code Generation**: Generates code templates based on extracted intent and entities.
- **Task Planning**: Plans and organizes development tasks.
- **Test Generation**: Creates unit tests for the generated code.
- **Deployment Scripts**: Generates deployment scripts for deploying the generated code.

## Installation

To install HOFchain, simply clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/HOFchain.git
cd HOFchain
pip install -r requirements.txt
```

## Usage

Here’s an example of how to use HOFchain to generate a REST API from a natural language specification:

```python
from HOFchain import (
    parse_input, generate_code_template, plan_tasks,
    generate_tests, generate_deployment_script
)

# Input text from user
input_text = "Create a REST API with endpoints for user registration and login."

# Step 1: Parse Input
intent, entities = parse_input(input_text)
print("Intent:", intent)
print("Entities:", entities)

# Step 2: Generate Code Template
code_template = generate_code_template(intent, entities)
print("Generated Code Template:", code_template)

# Step 3: Plan Tasks
tasks = plan_tasks(intent, entities)
print("Planned Tasks:", tasks)

# Step 4: Generate Tests
tests = generate_tests(intent, entities)
print("Generated Tests:", tests)

# Step 5: Generate Deployment Script
deployment_script = generate_deployment_script(intent, entities)
print("Generated Deployment Script:", deployment_script)
```

## API Reference

### NLU Parsing

#### `extract_intent(input_text: str) -> str`
Extracts the intent from the input text.

#### `extract_entities(input_text: str) -> dict`
Extracts relevant entities from the input text.

#### `parse_input(input_text: str) -> tuple`
Parses the input text to extract intent and entities.

### Code Generation

#### `generate_code_template(intent: str, entities: dict) -> str`
Generates a code template based on the intent and entities.

### Task Planning

#### `plan_tasks(intent: str, entities: dict) -> list`
Plans and organizes development tasks based on the intent and entities.

### Test Generation

#### `generate_tests(intent: str, entities: dict) -> list`
Generates unit tests for the generated code based on the intent and entities.

### Deployment Scripts

#### `generate_deployment_script(intent: str, entities: dict) -> str`
Generates deployment scripts for deploying the generated code.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Example Output

Here’s an example output for the provided usage:

### Intent
```
create_api
```

### Entities
```
{'endpoints': ['user registration', 'login']}
```

### Generated Code Template
```python
from flask import Flask

app = Flask(__name__)

# Define endpoints

@app.route('/user_registration', methods=['GET', 'POST'])
def user_registration():
    return "user registration endpoint"

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "login endpoint"

if __name__ == "__main__":
    app.run(debug=True)
```

### Planned Tasks
```json
[
    {"task": "Define endpoints", "details": {"endpoints": ["user registration", "login"]}},
    {"task": "Implement endpoints", "details": {"endpoints": ["user registration", "login"]}},
    {"task": "Test endpoints", "details": {"endpoints": ["user registration", "login"]}}
]
```

### Generated Tests
```python
def test_user_registration():
    response = client.get('/user_registration')
    assert response.status_code == 200

def test_login():
    response = client.get('/login')
    assert response.status_code == 200
```

### Generated Deployment Script
```Dockerfile
# Dockerfile
FROM python:3.8-slim

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Contact

For questions or support, please open an issue on the GitHub repository or contact source@distillative.ai

---
