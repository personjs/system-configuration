import sys
from PyQt5.QtWidgets import QApplication
from system_configuration.utils.logger import logger
from system_configuration.ui.main_window import MainWindow

def main():
    logger.info("Starting the application")
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    exit_code = app.exec_()
    logger.info("Application closed")
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
