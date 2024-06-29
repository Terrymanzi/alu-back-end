#!/usr/bin/python3
"""
This module retrieves and displays TODO list progress for a given employee ID.
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee data including TODO list progress using REST API."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(employee_id):
    """Display the TODO list progress for the given employee ID."""
    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        display_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
