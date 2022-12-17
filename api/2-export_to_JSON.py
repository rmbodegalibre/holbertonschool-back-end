#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

import json
import requests
import sys


def api_todo():
    us_id = int(sys.argv[1])
    data_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(us_id)).json()
    todos_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            us_id
        )).json()

    with open('{}.json'.format(us_id), 'w') as f:
        list_task = []
        for todo in todos_user:
            data_local = {}
            data_local['task'] = todo['title']
            data_local['completed'] = todo['completed']
            data_local['username'] = data_user['username']

            list_task.append(data_local)
        json_data = json.dumps({'{}'.format(us_id): list_task})
        f.write(json_data)

if __name__ == "__main__":
    api_todo()
