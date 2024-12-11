from PyQt5.QtWidgets import QApplication

def apply_theme(app, theme: str):
    """
    Apply the selected theme to the QApplication.
    
    :param app: The QApplication instance.
    :param theme: The theme name, either 'light' or 'dark'.
    """
    if theme == "light":
        light_stylesheet = """
        QWidget {
            background-color: white;
            color: black;
        }
        """
        app.setStyleSheet(light_stylesheet)
    elif theme == "dark":
        dark_stylesheet = """
        QWidget {
            background-color: #2e2e2e;
            color: white;
        }
        """
        app.setStyleSheet(dark_stylesheet)
