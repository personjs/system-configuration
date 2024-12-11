import pytest
from PyQt5.QtWidgets import QApplication
from system_configuration.ui.main_window import MainWindow

@pytest.fixture
def app(qtbot):
    """Create an instance of the MainWindow for testing."""
    app = QApplication([])
    window = MainWindow()
    qtbot.addWidget(window)
    return window

def test_main_window_initialization(app):
    """Test the initial state of the main window."""
    # Test that the main window is initialized properly
    assert app.isVisible()  # Check if the window is visible
    assert app.windowTitle() == "System Configuration"  # Check the window title

def test_theme_toggle(app, qtbot):
    """Test the theme toggle functionality."""
    # Initially, check for light theme or dark theme based on the current setting
    if app.APP_THEME == "light":
        assert app.light_theme_action.isChecked()
        app.set_dark_theme()  # Change theme to dark
        assert app.dark_theme_action.isChecked()
    else:
        assert app.dark_theme_action.isChecked()
        app.set_light_theme()  # Change theme to light
        assert app.light_theme_action.isChecked()
