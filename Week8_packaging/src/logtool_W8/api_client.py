import requests
from .logger_config import setup_logger

# init logger
logger = setup_logger()


def upload_log(log_data):
    logger.info("Uploading log")

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=log_data
    )

    return response