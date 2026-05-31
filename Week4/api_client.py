import requests


def upload_log(log_data):

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=log_data
    )

    return response