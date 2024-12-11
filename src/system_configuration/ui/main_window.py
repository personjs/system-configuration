from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QTabWidget
from system_configuration.config.settings import APP_THEME, DEFAULT_WINDOW_TITLE, DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT

# Utils
from system_configuration.utils.logger import logger
from system_configuration.utils.theme import apply_theme

# Dialogs
from system_configuration.ui.dialogs.about_dialog import AboutDialog

# Widgets
from system_configuration.ui.widgets.network_tab import NetworkTab
from system_configuration.ui.widgets.puppet_tab import PuppetTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        logger.debug("Main window initialized")

        self.setWindowTitle(DEFAULT_WINDOW_TITLE)
        self.resize(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)

        # Create the menu bar
        self.menu_bar = self.menuBar()
        self.create_menu()

        # Create the tab widget and add tabs
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Add tabs
        self.tab_widget.addTab(NetworkTab(), "Network")
        self.tab_widget.addTab(PuppetTab(), "Puppet")

        # Apply the initial theme
        apply_theme(QApplication.instance(), APP_THEME)
        self.update_theme_menu()

    def closeEvent(self, event):
        logger.info("Application is closing")
        event.accept()

    def create_menu(self):
        # Create 'Help' menu
        help_menu = self.menu_bar.addMenu("Help")

        # Create an 'About' action and connect it to the about_dialog method
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

        # Create 'View' menu for toggling themes
        view_menu = self.menu_bar.addMenu("View")

        # Create a 'Themes' submenu
        themes_menu = QMenu("Themes", self)

        # Create actions for Light and Dark themes
        self.light_theme_action = QAction("Light", self)
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.triggered.connect(self.set_light_theme)

        self.dark_theme_action = QAction("Dark", self)
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.triggered.connect(self.set_dark_theme)

        # Add the theme actions to the 'Themes' submenu
        themes_menu.addAction(self.light_theme_action)
        themes_menu.addAction(self.dark_theme_action)

        # Add 'Themes' submenu to 'View' menu
        view_menu.addMenu(themes_menu)

    def show_about_dialog(self):
        # Show the About dialog
        dialog = AboutDialog(self)
        dialog.exec_()

    def set_light_theme(self):
        """ Set the Light theme and apply it. """
        global APP_THEME
        APP_THEME = "light"
        apply_theme(QApplication.instance(), APP_THEME)  # Apply the theme from theme.py
        self.update_theme_menu()

    def set_dark_theme(self):
        """ Set the Dark theme and apply it. """
        global APP_THEME
        APP_THEME = "dark"
        apply_theme(QApplication.instance(), APP_THEME)  # Apply the theme from theme.py
        self.update_theme_menu()

    def update_theme_menu(self):
        """ Update the checkmark in the menu based on the current theme. """
        if APP_THEME == "light":
            self.light_theme_action.setChecked(True)
            self.dark_theme_action.setChecked(False)
        elif APP_THEME == "dark":
            self.light_theme_action.setChecked(False)
            self.dark_theme_action.setChecked(True)
