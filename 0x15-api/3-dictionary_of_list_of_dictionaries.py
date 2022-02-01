#!/usr/bin/python3
''' returns information about his/her TODO list progress '''

import requests

'''
need access to:
    username - in users
    tasks and task completed - todos
'''
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    try:
        with open("todo_all_employees.json", 'w', encoding='utf-8') as json:
            for idx in range(1, 11):
                usr = requests.get(url+'users/{:d}'.format(idx)).json()["username"]
                request = requests.get(url+'todos?userId={}'.format(idx))
                json.write('{ '+'"{}": ['.format(idx))
                dic = request.json()
                num = 0
                d_len = len(dic) - 1
                for task in dic:
                    if task['completed']:
                        low = "true"
                    else:
                        low = "false"
                    json.write('{' + '"username": "{}", '.format(usr))
                    json.write('"task": "{}", '.format(task['title']))
                    json.write('"completed": {}'.format(low))
                    if num < d_len:
                        json.write('}, ')
                        num += 1
                json.write('}]}')
    except:
        pass
