#!/usr/bin/python3
"""This module defines an API that saved data of a given employee"""
from requests import get
from sys import argv
import csv


def api_todo():
    """
    This function accepts an integer as a parameter, which is the employee ID
    """
    # us_id = sys.argv[1]
    url_base = "https://jsonplaceholder.typicode.com"
    url_users = "{}/users/{}".format(url_base, argv[1])
    # url_users = "https://jsonplaceholder.typicode.com/users?id=" + argv[1]
    data_users = get(url_users)
    json_users = data_users.json()
    user_name = json_users.get("username")

    url_todos = "{}/todos?userId={}".format(url_base, argv[1])
    # url_todos = "https://jsonplaceholder.typicode.com/todos?userId="+argv[1]
    data_users = get(url_todos)
    json_todos = data_users.json()
    done_tasks = []

    for tasks in json_todos:
        done_tasks.append([argv[1], user_name, tasks.get("completed"),
                           tasks.get("title")])

    csv_file = argv[1] + ".csv"
    with open(csv_file, mode="w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in done_tasks:
            writer.writerow(task)


if __name__ == "__main__":
    api_todo()
