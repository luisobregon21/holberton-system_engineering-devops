#!/usr/bin/python3
"""
module that takes argv 1 and uses it to request to a fake api
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        num = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        usr = requests.get(url+'users/{}'.format(argv[1])).json()["name"]
        r = requests.get(url + "todos?userId={}".format(num)).json()
        tasks = 0
        total = 0
        nametask = ""
        for element in r:
            if element["completed"] is True:
                tasks += 1
                nametask += "\t " + element["title"] + "\n"
            total += 1
        print("Exployee {} is done with tasks({}/{}):".format(usr,
                                                              tasks, total))
        print(nametask, end="")
    else:
        print("length WRONG")
