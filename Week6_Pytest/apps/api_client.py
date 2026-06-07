# api_client.py

import requests

def get_post():

    response = requests.get("dummy")

    return response.json()

def upload_log(log):
    pass

def upload_all(logs):

    for log in logs:
        upload_log(log)