from system_configuration.services.config_service import ConfigService
from system_configuration.services.logging_service import LoggingService

class ThemeService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThemeService, cls).__new__(cls)
            cls._instance._setup_theme()
        return cls._instance

    def _setup_theme(self):
        self.config_service = ConfigService()
        self.themes = ["light", "dark"]
        self.theme = self.config_service.get('Window', 'theme', fallback='dark')
        self.logger = LoggingService().get_logger(__name__)

    def get_themes(self):
        return self.themes

    def get_theme(self):
        return self.theme

    def set_theme(self, theme: str):
        # Set the theme and apply the corresponding styles
        if theme not in self.themes:
            self.logger.error(f"Invalid theme: {theme}")
            return

        # Update the current theme
        self.theme = theme
        self.config_service.set('Window', 'theme', theme)
        self.logger.debug(f"Theme set to {theme}")
