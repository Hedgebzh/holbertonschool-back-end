#!/usr/bin/python3
'''
Task export data in the CSV format
'''
import csv
import requests
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]

    First_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    data_user = requests.get(First_url).json()
    data_name = data_user.get('username')


    Second_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    rest_data_user = requests.get(Second_url).json()


    file = user_id + '.csv'
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8', newline='') as f:

        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        # Write result in rows
        for todo in rest_data_user:
            result = [user_id, data_name, todo.get('completed'),
                      todo.get('title')]
            writer.writerow(result)
