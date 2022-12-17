#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

import json
import requests


if __name__ == '__main__':
    data_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    data_employees = {}

    for user in data_users:
        todos_user = requests.get(
            'https://jsonplaceholder.typicode.com/user/{}/todos'.format(
                user['id']
            )).json()

        tasks_user = []
        for todo in todos_user:
            data_task = {}
            data_task['username'] = user['username']
            data_task['task'] = todo['title']
            data_task['completed'] = todo['completed']
            tasks_user.append(data_task)

        data_employees['{}'.format(user['id'])] = tasks_user

    with open('todo_all_employees.json', 'w') as f:
        json_data = json.dumps(data_employees)
        f.write(json_data)
