import logging

def setup_logging(filename: str, level: str):
    # Create file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - Line %(lineno)d - %(message)s'))

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

    # Add handlers to the logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.setLevel(level)

def get_logger(name):
    logger = logging.getLogger(name)
    return logger