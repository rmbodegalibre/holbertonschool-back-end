#!/usr/bin/python3

"""This module defines an API that saved data of a given employee"""

import requests
import sys


def api_todo():
    us_id = int(sys.argv[1])
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(us_id)).json()
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            us_id
        )).json()


    with open('{}.csv'.format(us_id), 'w') as f:
        for todo in user_todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                us_id,
                user_data['username'],
                todo['completed'],
                todo['title']
            ))

if __name__ == "__main__":
    api_todo()
