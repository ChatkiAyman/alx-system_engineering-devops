#!/usr/bin/python3
"""API Model"""
import json
import requests
from sys import argv
"""script to export data in the JSON format"""
"""run file with ./2-export_to_JSON.py 2"""


def main():
    """api_request"""
    url_task = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        int(argv[1]))
    url_name = "https://jsonplaceholder.typicode.com/users/{}".format(
        int(argv[1]))
    response = requests.get(url_task)
    response_name = requests.get(url_name)
    data = response.json()
    data_name = response_name.json().get('username')
    task_done = ['\t {}\n'.format(dic.get('title')) for dic in data
                 if dic.get('completed') is True]
    if data_name and data:
        print("Employee {} is done with tasks({}/{}):".format(
            data_name, len(task_done), len(data)))
        print("".join(task_done), end='')
        with open('{}.json'.format(argv[1]), mode='w') as file:
            json.dump({argv[1]: [{
                "task": dic.get('title'),
                "completed": dic.get('completed'),
                "username": data_name
            } for dic in data]}, file)


if __name__ == "__main__":
    main()
