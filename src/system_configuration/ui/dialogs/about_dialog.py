from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from system_configuration.config.settings import APP_NAME, APP_VERSION, APP_DESCRIPTION

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set the window title
        self.setWindowTitle("About")
        
        # Set the dialog's fixed size
        self.setFixedSize(400, 250)
        
        # Create a vertical layout for the dialog
        layout = QVBoxLayout()
        
        # Add the application name and version
        app_name_label = QLabel(APP_NAME)
        app_name_label.setAlignment(Qt.AlignCenter)
        app_name_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        version_label = QLabel(f"Version: {APP_VERSION}")
        version_label.setAlignment(Qt.AlignCenter)
        
        # Add a description or credits text
        description_label = QLabel(APP_DESCRIPTION)
        description_label.setAlignment(Qt.AlignCenter)
        
        # Add the labels to the layout
        layout.addWidget(app_name_label)
        layout.addWidget(version_label)
        layout.addWidget(description_label)
        
        # Create an OK button to close the dialog
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)  # Close the dialog when clicked
        
        # Add the OK button at the bottom
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(ok_button)
        
        layout.addLayout(button_layout)
        
        # Set the layout for the dialog
        self.setLayout(layout)
        