import logging
from .config_loader import load_config
from .config_loader import get_log_level

def setup_logger():
    # create logger name 'logtool'
    logger = logging.getLogger("logtool")

    # choose level arcoding to json config file
    config = load_config("config.json")
    log_level = get_log_level(config)

    if log_level == "DEBUG":
        logger.setLevel(logging.DEBUG)

    elif log_level == "INFO":
        logger.setLevel(logging.INFO)

    elif log_level == "WARNING":
        logger.setLevel(logging.WARNING)

    elif log_level == "ERROR":
        logger.setLevel(logging.ERROR)

    else:
        logger.setLevel(logging.INFO)

    # avoid duplicate
    if not logger.handlers:
        # "Formatter"
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        # "Handler 1" for Terminal (StreamHandler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # "Handler 2" for write to 'tool.log' (FileHandler)
        file_handler = logging.FileHandler("logtool.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger