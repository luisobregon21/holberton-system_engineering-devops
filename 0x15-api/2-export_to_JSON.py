#!/usr/bin/python3
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
        try:
            with open(argv[1] + ".json", 'w', encoding='utf-8') as json:
                json.write('{'+'"{}": ['.format(argv[1]))
                d_len = len(dic) - 1
                idx = 0
                for task in dic:
                    if task['completed']:
                        low = "true"
                    else:
                        low = "false"
                    json.write('{' + '"task": "{}", '.format(task['title']))
                    json.write('"completed": {}, '.format(low))
                    json.write('"username": "{}"'.format(usr))
                    if idx < d_len:
                        json.write('}, ')
                        idx += 1
                json.write('}]}')
        except:
            pass
