import requests

"""
requests.get() Return  response

Include
- response.status_code
- response.json()    # dict / list type
- response.text      # raw string type

"""

def task2_GetAPI():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )

    print(response.status_code)

    data = response.json()
    print(data["title"])
    print(data["completed"])


def task2_GetMultipleObject():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    data = response.json()

    for i in range(0, 5):
        print(f'ID: {data[i]["id"]}')
        print(f'Title: {data[i]["title"]}')

def task2_postLog():
    log = {
        "level": "ERROR",
        "message": "UART timeout"
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=log
    )
    print(f'Status_code: {response.status_code}')
    print(response.json())

def task2_HTTP_Get_Post():
    print('\ntask2_GetAPI')
    task2_GetAPI()
    print('\ntask2_GetMultipleObject')
    task2_GetMultipleObject()
    print('\ntask2_postLog')
    task2_postLog()