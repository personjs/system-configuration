from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QPushButton, QMenu, QWidget, QSpacerItem, QSizePolicy, QHBoxLayout, QTextEdit
from PyQt6.QtGui import QAction
from system_configuration.controllers.main_controller import MainController
from system_configuration.services.config_service import ConfigService
from system_configuration.services.logging_service import LoggingService
from system_configuration.services.theme_service import ThemeService
from system_configuration.views.puppet_view import PuppetTab
from system_configuration.views.network_view import NetworkTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.config_service = ConfigService()
        self.theme_service = ThemeService()
        self.logger = LoggingService().get_logger(__name__)

        _title = self.config_service.get('Window', 'title')
        _width = self.config_service.getint('Window', 'width')
        _height = self.config_service.getint('Window', 'height')

        # Set title and size of the window
        self.setWindowTitle(_title)
        self.resize(_width, _height)

        # Create a central widget and layout
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        self.create_tabs()
        self.create_button_menu()

        # Initialize the controller
        self.controller = MainController(self)

        # Connect the button click event to controller's methods
        self.apply_button.clicked.connect(self.controller.apply)
        self.cancel_button.clicked.connect(self.controller.close_application)

        # Create and set the menu bar
        self.create_menu_bar()

        self.logger.debug("Main Window Initialized.")

    def create_menu_bar(self):
        # Create menu bar
        menubar = self.menuBar()

        # Create 'View' menu
        view_menu = QMenu("&View", self)
        menubar.addMenu(view_menu)

        # Create 'Theme' submenu
        theme_menu = QMenu("&Themes", self)
        view_menu.addMenu(theme_menu)

        # Dynamically create actions for each theme
        for theme in self.theme_service.get_themes():
            theme_action = QAction(f"&{theme.capitalize()}", self)
            theme_action.setCheckable(True)
            theme_action.setChecked(self.theme_service.get_theme() == theme)
            theme_menu.addAction(theme_action)
            # Connect each theme action to the controller's method
            theme_action.triggered.connect(lambda checked, theme=theme: self.controller.on_theme_action_triggered(theme))

        # Initialize the theme
        self.controller.set_theme(self.theme_service.get_theme())

    def get_theme_actions(self):
        for action in self.menuBar().actions():
            for sub_action in action.menu().actions():
                sub_action_text = sub_action.text().replace("&", "").strip().lower()
                if sub_action_text == "themes":
                    return sub_action.menu().actions()

    def create_tabs(self):
        self.tab_widget = QTabWidget(self)

        self.network_tab = NetworkTab()
        self.tab_widget.addTab(self.network_tab, "Network")

        self.puppet_tab = PuppetTab()
        self.tab_widget.addTab(self.puppet_tab, "Puppet")

        # Add the tab widget to the layout
        self.layout.addWidget(self.tab_widget)

    def create_button_menu(self):
        # Create a spacer item to push the button to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout.addItem(spacer)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()

        # Apply button
        self.apply_button = QPushButton("Apply", self)
        button_layout.addWidget(self.apply_button)

        # Create the "Cancel" button
        self.cancel_button = QPushButton("Cancel", self)
        button_layout.addWidget(self.cancel_button)

        # Add button layout to the main layout
        self.layout.addLayout(button_layout)
