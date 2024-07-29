from HOFchain import (
    parse_input, generate_code_template, plan_tasks,
    generate_tests, generate_deployment_script
)

# Input text from user
input_text = "Create a REST API with endpoints for user registration and login."

# Step 1: Parse Input
intent, entities = parse_input(input_text)
print("Intent:", intent)  # Debugging statement
print("Entities:", entities)  # Debugging statement

# Step 2: Generate Code Template
code_template = generate_code_template(intent, entities)
print("Generated Code Template:", code_template)  # Debugging statement

# Step 3: Plan Tasks
tasks = plan_tasks(intent, entities)
print("Planned Tasks:", tasks)  # Debugging statement

# Step 4: Generate Tests
tests = generate_tests(intent, entities)
print("Generated Tests:", tests)  # Debugging statement

# Step 5: Generate Deployment Script
deployment_script = generate_deployment_script(intent, entities)
print("Generated Deployment Script:", deployment_script)  # Debugging statement

# Output results
(code_template, tasks, tests, deployment_script)

