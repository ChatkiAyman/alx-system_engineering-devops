#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information
"""
import requests
import sys


def main():
        """ api request"""
            url_task = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                            int(sys.argv[1]))
                url_name = "https://jsonplaceholder.typicode.com/users/{}".format(
                                int(sys.argv[1]))
                    response = requests.get(url_task)
                        response_name = requests.get(url_name)
                            data = response.json()
                                data_name = response_name.json().get('name')
                                    task_done = ['\t {}\n'.format(dic.get('title')) for dic in data
                                                             if dic.get('completed') is True]

                                        if data_name and data:
                                                    print("Employee {} is done with tasks({}/{}):".format(
                                                                    data_name, len(task_done), len(data)))
                                                            print("".join(task_done), end='')


                                                            if __name__ == "__main__":
                                                                    """ Entry point"""
                                                                        main()
