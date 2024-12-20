from PyQt6.QtWidgets import QApplication
from system_configuration.services.logging_service import LoggingService
from system_configuration.services.theme_service import ThemeService
from system_configuration.workers.puppet_worker import PuppetWorker

class MainController:
    def __init__(self, view):
        self.view = view
        self.logger = LoggingService().get_logger(__name__)
        self.theme_service = ThemeService()
        self.puppet_worker = PuppetWorker()
        self.logger.debug("Initialized")

    def apply(self):
        self.logger.debug("Apply clicked!")

    def close_application(self):
        self.logger.info("Cancel button clicked. Exiting application...")
        QApplication.quit()

    def set_theme(self, theme: str):
        self.theme_service.set_theme(theme)
        if theme == "dark":
            self.view.setStyleSheet("background-color: #222; color: #fff;")
        elif theme == "light":
            self.view.setStyleSheet("background-color: #fff; color: #222;")

        # Update the menu actions to reflect the change
        for action in self.view.get_theme_actions():
            action.setChecked(False)

        # Check the action for the current theme
        for action in self.view.get_theme_actions():
            action_text = action.text().replace("&", "").strip().lower()
            if action_text == self.theme_service.get_theme().lower():
                action.setChecked(True)

    def on_theme_action_triggered(self, selected_theme: str):
        # This method is triggered when a theme action is clicked
        if self.theme_service.get_theme() != selected_theme:
            self.set_theme(selected_theme)
