from PyQt5.QtCore import pyqtSignal, QObject
from system_configuration.utils import logging_utils

logger = logging_utils.get_logger(__name__)

class MainController(QObject):
    button_clicked = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view
        logger.debug("Main controller initialized")

    def handle_button_click(self):
        logger.info("Button clicked")
        # Update the view (example)
        self.view.label.setText("Button clicked!")
        
        # self.button_clicked.emit()