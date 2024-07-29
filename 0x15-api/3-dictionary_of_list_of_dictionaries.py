#!/usr/bin/python3
"""api module"""
import json
import requests
"""api module"""


def main():
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(url_tasks).json()
    data_json = {}

    for obj in tasks:
        user = data_json.get(obj.get("userId"))
        if user:
            user.append({
                "task": obj.get('title'),
                "completed": obj.get('completed'),
                "username": user[0]["username"]
                })
        else:
            data = []
            url_name = "https://jsonplaceholder.typicode.com/users/{}".format(
                int(obj.get("userId")))
            username = requests = requests.get(url_name).json().get("username")
            data.append(
                {
                    "task": obj.get("title"),
                    "completed": obj.get("completed"),
                    "username": username
                }
            )
            data_json[obj.get("userId")] = data
            file_name = "todo_all_employees.json"
            with open(file_name, "w") as file:
                json.dump(data_json, file)


if __name__ == "__main__":
    main()
