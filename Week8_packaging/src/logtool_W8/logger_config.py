import logging

def setup_logger():
    # create logger name 'logtool'
    logger = logging.getLogger("logtool")

    # setup level to INFO
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