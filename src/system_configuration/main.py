import sys
import argparse
from PyQt6.QtWidgets import QApplication
from system_configuration.utils import config_utils
from system_configuration.utils import logging_utils
from system_configuration.views.main_view import MainWindow

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="This script runs a PyQt application.")
    parser.add_argument("--config", type=str, default="config/config.ini", help="Path to the configuration file (default: config/config.ini)")
    args = parser.parse_args()
    
    # Get configuration
    config = config_utils.get_config(args.config)

    # Set up logging with the specified configuration file
    logging_utils.setup_logging(filename=config['logging_filename'], level=config['logging_level'])
    logger = logging_utils.get_logger("system_configuration")
    
    logger.info("Starting application")
    app = QApplication(sys.argv)
    window = MainWindow(width=config['window_width'], height=config['window_height'], title=config['window_title'])

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()