import json
import os
# load from .evn
from dotenv import load_dotenv

load_dotenv()

def load_config(path):
    with open(path, "r") as file:
        return json.load(file)

def get_log_level(config):

    return (
        os.getenv("LOG_LEVEL")
        or config.get("log_level")
        or "INFO"
    )

def get_api_url(config):

    return (
        os.getenv("API_URL")
        or config.get("api_url")
    )

def get_token_(config):

    return (
        os.getenv("API_TOKEN")
        or config.get("api_token")
    )
