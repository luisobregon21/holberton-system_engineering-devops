#!/usr/bin/python3
''' returns information about his/her TODO list progress '''

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        url = 'https://jsonplaceholder.typicode.com/'
        usr = requests.get(url+'users/{}'.format(argv[1])).json()["name"]
        request = requests.get(url+'todos?userId={}'.format(argv[1]))
        dic = request.json()
        num = 0
        taskname = ""
        for task in dic:
            if task['completed'] is True:
                num += 1
                taskname += "  " + task['title'] + '\n'
        print("Employee {} is done with tasks({}/20):".format(usr, num))
        print(taskname, end="")
