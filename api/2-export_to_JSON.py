#!/usr/bin/python3
"""
Task export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]

    First_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id)

    data_user = requests.get(First_url).json()


    data_username = data_user.get('username')


    Second_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)


    rest_data_user = requests.get(Second_url).json()

    dict = {user_id: []}


    file = user_id + '.json'

    for data in rest_data_user:
        result = {
            'task': data.get('title'),
            'completed': data.get('completed'),
            'username': data_username,
        }
        dict[user_id].append(result)


    with open(file, 'w') as f:
        json.dump(dict, f)
