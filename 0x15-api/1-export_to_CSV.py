#!/usr/bin/python3
"""script to export data in the CSV format"""
"""run file with ./1-export_to_CSV.py 2"""
import csv
import requests
from sys import argv


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
        with open('{}.csv'.format(argv[1]), mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for dic in data:
                writer.writerow([argv[1], data_name, dic.get('completed'),
                                 dic.get('title')])


if __name__ == "__main__":
    """Entry point"""
    main()
