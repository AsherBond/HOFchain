def plan_tasks(intent, entities):
    if intent == "create_api":
        tasks = [
            {"task": "Define endpoints", "details": entities},
            {"task": "Implement endpoints", "details": entities},
            {"task": "Test endpoints", "details": entities}
        ]
        return tasks
    return []

