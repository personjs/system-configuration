from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QTextCursor
from system_configuration.utils import logging_utils
import subprocess
import time

logger = logging_utils.get_logger(__name__)

class MainController:
    def __init__(self, view):
        self.view = view
        self.themes = ["light", "dark"]
        self.current_theme = "dark"  # Default theme
        logger.debug("Controller Initialized.")
    
    def handle_output(self):
        output = bytes(self.view.process.readAllStandardOutput()).decode('utf-8')
        self.update_console(output)
        
    def handle_error(self):
        error = bytes(self.view.process.readAllStandardError()).decode('utf-8')
        self.update_console(f"Error: {error}")
        
    def handle_finished(self):
        self.update_console("Task finished.")
        
    def apply_simulate(self):
        """Simulate a long-running task and output text during its execution."""
        command = ['python', '-c', 'import time; [time.sleep(1) for _ in range(10)]']

        # Start the process (simulating a long-running task)
        self.view.process.start(command[0], command[1:])
        self.update_console("Starting long task...")

        # Simulate periodic output during the task
        for i in range(10):
            time.sleep(1)  # Simulate work being done
            self.update_console(f"Step {i + 1}: Task is running...")
            self.view.process.write(f"Simulating task progress... Step {i + 1}\n".encode('utf-8'))  # Simulated progress output
        self.view.process.write("Task completed.\n".encode('utf-8'))

    def apply(self):
        # Handle button click action
        logger.debug("Apply clicked!")
        # command = ["puppet", "agent", "-t"]
        command = ["python", "-c", "import time; [time.sleep(1) for _ in range(10)]"]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            self.update_console(result.stdout)
            self.update_console(result.stderr)
        except subprocess.CalledProcessError as e:
            self.update_console(f"Error running ls:\n{e.stderr}")
            
    def update_console(self, text: str):
        self.view.console_output.append(text)
        # Ensure the cursor moves to the end to keep the view scrollable
        cursor = self.view.console_output.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.view.console_output.setTextCursor(cursor)
        
    def close_application(self):
        logger.info("Cancel button clicked. Exiting application...")
        QApplication.quit()

    def set_theme(self, theme: str):
        # Set the theme and apply the corresponding styles
        if theme not in self.themes:
            logger.error(f"Invalid theme: {theme}")
            return
        
        # Update the current theme
        self.current_theme = theme
        if theme == "dark":
            self.view.setStyleSheet("background-color: #222; color: #fff;")
        elif theme == "light":
            self.view.setStyleSheet("background-color: #fff; color: #222;")
        logger.debug(f"Theme set to {theme}")
        
        # After setting the theme, update the menu actions to reflect the change
        self.update_theme_menu_actions()

    def get_current_theme(self):
        # Return the current theme
        return self.current_theme
    
    def get_themes(self):
        # Return the list of available themes
        return self.themes
    
    def on_theme_action_triggered(self, selected_theme: str):
        # This method is triggered when a theme action is clicked
        if self.current_theme != selected_theme:
            self.set_theme(selected_theme)
        
    def update_theme_menu_actions(self):
        # This method is responsible for updating the checked state of theme actions in the menu
        for action in self.view.get_theme_actions():
            # Uncheck all actions
            action.setChecked(False)
        
        # Check the action for the current theme
        for action in self.view.get_theme_actions():
            action_text = action.text().replace("&", "").strip().lower()
            if action_text == self.current_theme.lower():
                action.setChecked(True)
