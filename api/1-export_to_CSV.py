#!/usr/bin/python3
"""
This script for a given employee ID, returns information about
his/her TODO list progress, and exports data in the CSV format.


Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress
in this exact format:
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE
(with 1 tabulation and 1 space before the TASK_TITLE)
"""
from requests import get
from sys import argv
import csv


def api_todo():
    """
    This function accepts an integer as a parameter, which is the employee ID
    """
    url_base = "https://jsonplaceholder.typicode.com"
    url_users = "{}/users/{}".format(url_base, argv[1])
    #url_users = "https://jsonplaceholder.typicode.com/users?id="
    res = get(url_users)
    json_users = res.json()
    user_name = json_users.get("username")

    url_todos = "{}/todos?userId={}".format(url_base, argv[1])
    #url_todos = "https://jsonplaceholder.typicode.com/todos"
    res = get(url_todos)
    json_todos = res.json()
    done_tasks = []

    for tasks in json_todos:
        done_tasks.append(
            [argv[1], user_name, tasks.get("completed"), tasks.get("title")])

    csv_file = argv[1] + ".csv"
    with open(csv_file, mode="w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in done_tasks:
            writer.writerow(task)


if __name__ == "__main__":
    api_todo()
