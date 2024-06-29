#!/usr/bin/python3
"""
This module retrieves and exports TODO list progress for all employees
to a JSON file.
"""

import json
import requests
import sys


def fetch_all_data():
    """Fetch data for all employees and their TODO lists using REST API."""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    return users_data, todos_data


def export_all_to_json(users_data, todos_data):
    """Export all employees' TODO lists to a JSON file."""
    data = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data if task.get("userId") == user_id
        ]
        data[str(user_id)] = tasks

    filename = "todo_all_employees.json"
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    users_data, todos_data = fetch_all_data()
    export_all_to_json(users_data, todos_data)
