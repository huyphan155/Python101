import requests
from .logger_config import setup_logger
from .config_loader import load_config

# init logger
logger = setup_logger()


def upload_log(log_data):
    logger.info("Uploading log")

    # choose the config from corresponding json
    config = load_config("config.json")
    # take api_url
    api_url = config["api_url"]

    response = requests.post(
        api_url,
        json=log_data
    )

    return response