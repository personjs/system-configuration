from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QMenuBar, QMenu, QAction
from system_configuration.utils import logging_utils
from system_configuration.controllers import main_controller

logger = logging_utils.get_logger(__name__)

class MainWindow(QMainWindow):
    def __init__(self, width: int, height: int, title: str, theme: str):
        super().__init__()

        # Set title based on configuration
        self.setWindowTitle(title)
        
        # Set window size based on configuration
        self.resize(width, height)
        
        self.create_menu(theme)

        # Layout and widgets
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("This is a PyQt application.")
        layout.addWidget(self.label)

        self.button = QPushButton("Click Me!")
        layout.addWidget(self.button)
                
        logger.debug("Main window initialized")
        
    def create_menu(self, theme):
        # Create menu bar
        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)

        # Create View menu
        view_menu = QMenu("&View", self)
        self.menubar.addMenu(view_menu)

        # Create Theme submenu
        theme_menu = QMenu("&Theme", self)
        view_menu.addMenu(theme_menu)

        # Create theme actions
        self.dark_theme_action = QAction("&Dark", self)
        self.dark_theme_action.setCheckable(True)
        self.light_theme_action = QAction("&Light", self)
        self.light_theme_action.setCheckable(True)

        # Add actions to the theme menu
        theme_menu.addAction(self.dark_theme_action)
        theme_menu.addAction(self.light_theme_action)

        # Set initial theme based on configuration (e.g., from config.ini)
        if theme == "dark":
            self.set_dark_theme()
        elif theme == "light":
            self.set_light_theme()
        
        # Connect actions to slots
        self.dark_theme_action.triggered.connect(self.set_dark_theme)
        self.light_theme_action.triggered.connect(self.set_light_theme)
        
    def set_dark_theme(self):
        # Apply dark theme styles
        self.setStyleSheet("background-color: #222; color: #fff;")
        self.dark_theme_action.setChecked(True)
        self.light_theme_action.setChecked(False)

    def set_light_theme(self):
        # Apply light theme styles (default Qt styles)
        self.setStyleSheet("")
        self.dark_theme_action.setChecked(False)
        self.light_theme_action.setChecked(True)