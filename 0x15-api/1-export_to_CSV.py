#!/usr/bin/env python3
''' returns information about his/her TODO list progress '''

import os
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        url = 'https://jsonplaceholder.typicode.com/'
        usr = requests.get(url+'users/{}'.format(argv[1])).json()["username"]
        request = requests.get(url+'todos?userId={}'.format(argv[1]))
        dic = request.json()
        num = 0
        taskname = ""
        with open("USER_ID.csv", 'w', encoding='utf-8') as csv:
            for task in dic:
                csv.write('"{}","{}","{}","{}"\n'.format(
                    argv[1], usr, task["completed"], task['title']))
            csv.close()
