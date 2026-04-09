import json
import os
from models import Task
FILE_NAME = "data.json"
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            tasks = []
            for item in data:
                task = Task(item["title"])
                task.completed = item["completed"]
                tasks.append(task)
            return tasks
    except (json.JSONDecodeError, FileNotFoundError):
        return []
def save_tasks(tasks):
    data = []
    for task in tasks:
        data.append({
            "title": task.title,
            "completed": task.completed
        })

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)