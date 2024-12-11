import os
import logging
import pkg_resources

# Application settings
APP_NAME = "System Configuration"
APP_VERSION = pkg_resources.get_distribution("system-configuration").version
APP_THEME = "dark"
APP_DESCRIPTION = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

DEBUG = True  # Set to False for production

# UI settings
DEFAULT_WINDOW_WIDTH = 800
DEFAULT_WINDOW_HEIGHT = 600
DEFAULT_WINDOW_TITLE = f"{APP_NAME} - {APP_VERSION}"

# Paths
LOG_DIR = os.path.join(os.path.dirname(__file__), '../../../logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

# Logging settings
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOGGING_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
