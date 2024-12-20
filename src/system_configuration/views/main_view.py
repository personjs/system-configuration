from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QMenu, QWidget, QSpacerItem, QSizePolicy, QHBoxLayout, QTextEdit
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QProcess
from system_configuration.controllers.main_controller import MainController
from system_configuration.services.config_service import ConfigService
from system_configuration.services.logging_service import LoggingService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.config_service = ConfigService()
        self.logger = LoggingService().get_logger(__name__)
        
        _title = self.config_service.get('Window', 'title')
        _width = self.config_service.getint('Window', 'width')
        _height = self.config_service.getint('Window', 'height')

        # Set title and size of the window
        self.setWindowTitle(_title)
        self.resize(_width, _height)

        # Create a central widget and layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        # Create a scrollable console-like output widget
        self.console_output = QTextEdit(self)
        self.console_output.setReadOnly(True)  # Make it read-only
        layout.addWidget(self.console_output)
        
        # Create a spacer item to push the button to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)
        
        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()

        # Apply button
        self.apply_button = QPushButton("Apply", self)
        button_layout.addWidget(self.apply_button)
        
        # Create the "Cancel" button
        self.cancel_button = QPushButton("Cancel", self)
        button_layout.addWidget(self.cancel_button)
        
        # Add button layout to the main layout
        layout.addLayout(button_layout)

        # Initialize the controller
        self.controller = MainController(self)

        # Connect the button click event to controller's method
        self.apply_button.clicked.connect(self.controller.apply_simulate)
        self.cancel_button.clicked.connect(self.controller.close_application)

        # Create and set the menu bar
        self.create_menu_bar()
        
        # Create QProcess for long-running task
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.controller.handle_output)
        self.process.readyReadStandardError.connect(self.controller.handle_error)
        self.process.finished.connect(self.controller.handle_finished)

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
        for theme in self.controller.get_themes():
            theme_action = QAction(f"&{theme.capitalize()}", self)
            theme_action.setCheckable(True)
            theme_action.setChecked(self.controller.get_current_theme() == theme)
            
            theme_menu.addAction(theme_action)
            
            # Connect each theme action to the controller's method
            theme_action.triggered.connect(lambda checked, theme=theme: self.controller.on_theme_action_triggered(theme))
            
        # Initialize the theme
        self.controller.set_theme(self.controller.get_current_theme())
        
    def get_theme_actions(self):
        for action in self.menuBar().actions():
            for sub_action in action.menu().actions():
                sub_action_text = sub_action.text().replace("&", "").strip().lower()
                if sub_action_text == "themes":
                    return sub_action.menu().actions()