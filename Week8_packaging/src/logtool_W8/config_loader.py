import json
import os

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


config = {
    "log_level": "WARNING"
}

print(
    get_log_level(config)
)