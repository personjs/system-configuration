from system_configuration.services.logging_service import LoggingService

class NetworkController:
    def __init__(self, view):
        self.view = view
        self.logger = LoggingService().get_logger(__name__)
        self.logger.debug("Initialized")
