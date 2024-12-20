import sys
import argparse
from PyQt6.QtWidgets import QApplication
from system_configuration.services.config_service import ConfigService
from system_configuration.services.logging_service import LoggingService
from system_configuration.views.main_view import MainWindow

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="This script runs a PyQt application.")
    parser.add_argument("--config-file", type=str, default="config/config.ini", help="Path to the configuration file (default: config/config.ini)")
    args = parser.parse_args()
    
    # Configuration
    ConfigService(config_file=args.config_file)
    
    # Logging
    logging_service = LoggingService()
    logger = logging_service.get_logger(f"system_configuration.{__name__}")
    logger.info("Starting application")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()