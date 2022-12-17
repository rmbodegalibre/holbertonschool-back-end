#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

import json
import requests
from sys import argv


def api_todo():
    # us_id = int(sys.argv[1])
    data_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            argv[1]
        )).json()

    with open('{}.json'.format(argv[1]), 'w') as f:
        list_task = []
        for todo in todos_user:
            data_local = {}
            data_local['task'] = todo['title']
            data_local['completed'] = todo['completed']
            data_local['username'] = data_user['username']

            list_task.append(data_local)
        json_data = json.dumps({'{}'.format(argv[1]): list_task})
        f.write(json_data)

if __name__ == "__main__":
    api_todo()
