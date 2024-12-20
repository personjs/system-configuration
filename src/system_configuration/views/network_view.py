from PyQt6.QtWidgets import QVBoxLayout, QLabel, QWidget
from system_configuration.services.logging_service import LoggingService
from system_configuration.controllers.network_controller import NetworkController

class NetworkTab(QWidget):
    def __init__(self):
        super().__init__()

        self.logger = LoggingService().get_logger(__name__)

        self.layout = QVBoxLayout()

        label = QLabel("Network Tab Content", self)
        self.layout.addWidget(label)

        self.controller = NetworkController(self)

        self.setLayout(self.layout)

        self.logger.debug("Tab Initialized")
