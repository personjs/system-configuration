import logging
from system_configuration.config.settings import LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_DATE_FORMAT, LOG_FILE_PATH

def setup_logger():
    """
    Set up the global logger for the project. This function configures logging 
    to both the console and a log file.
    """
    logger = logging.getLogger()
    logger.setLevel(LOGGING_LEVEL)
    
    # Log to a file
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(LOGGING_LEVEL)
    
    file_formatter = logging.Formatter(LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)
    file_handler.setFormatter(file_formatter)
    
    # Log to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGGING_LEVEL)
    console_formatter = logging.Formatter(LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)
    console_handler.setFormatter(console_formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Call this to initialize logging at the start of the application
logger = setup_logger()
