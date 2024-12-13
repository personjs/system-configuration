import sys
import argparse
from PyQt5.QtWidgets import QApplication
from system_configuration.utils import config_utils
from system_configuration.utils import logging_utils
from system_configuration.views.main_view import MainWindow
from system_configuration.controllers.main_controller import MainController

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="This script runs a PyQt application.")
    parser.add_argument("--config", type=str, default="config/config.ini", help="Path to the configuration file (default: config/config.ini)")
    args = parser.parse_args()
    
    # Get configuration
    config = config_utils.get_config(args.config)

    # Set up logging with the specified configuration file
    logging_utils.setup_logging(config['logging_filename'], config['logging_level'])
    logger = logging_utils.get_logger("system_configuration")
    
    logger.info("Starting application")
    app = QApplication(sys.argv)
    window = MainWindow(config['window_width'], config['window_height'], config['window_title'], config['window_theme'])

    # Create an instance of the controller and pass the window reference
    controller = MainController(window)
    
    # Map controllers to views
    window.button.clicked.connect(controller.handle_button_click)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()