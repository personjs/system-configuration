import logging
import inspect
from system_configuration.services.config_service import ConfigService

class LoggingService:
    _instance = None  # Singleton instance variable

    def __new__(cls):
        # Check if the singleton instance already exists
        if cls._instance is None:
            cls._instance = super(LoggingService, cls).__new__(cls)
            cls._instance._setup_logging()

        return cls._instance

    def _setup_logging(self):
        """Set up the logging configuration using ConfigService."""
        # Fetch configuration using ConfigService
        config_service = ConfigService()

        log_file = config_service.get('Logging', 'logfile', fallback='app.log')
        log_level_str = config_service.get('Logging', 'level', fallback='DEBUG').upper()

        # Convert log level string to actual logging level
        log_level = getattr(logging, log_level_str, logging.DEBUG)

        # Create the logger
        self.logger = logging.getLogger("root")
        self.logger.setLevel(log_level)

        # Create the formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create the file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        # Create the console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self, name=None):
        """Return the logger instance."""
        if name is None:
            frame = inspect.stack()[1].frame
            name = frame.f_globals["__name__"] # Use the module name by default
        return logging.getLogger(name)

    def log(self, level, message, name=None):
        """Convenience method to log messages."""
        logger = self.get_logger(name)
        extra = {}
        if level == 'debug':
            logger.debug(message, extra=extra)
        elif level == 'info':
            logger.info(message, extra=extra)
        elif level == 'warning':
            logger.warning(message, extra=extra)
        elif level == 'error':
            logger.error(message, extra=extra)
        elif level == 'critical':
            logger.critical(message, extra=extra)
        else:
            logger.info(message, extra=extra)

