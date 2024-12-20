import sys
from PyQt6.QtCore import QThread, pyqtSignal

class PuppetWorker(QThread):
    # Define signals to forward stdout and stdin to the GUI
    stdout_signal = pyqtSignal(str)
    stdin_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run_simulate(self):
        # Simulating a background task (could be any process)
        for i in range(5):
            self.stdout_signal.emit(f"Output: {i}\n")
            self.sleep(1)  # Simulate work being done
        self.stdout_signal.emit("Task Completed.\n")

    def send_input(self, input_data):
        # Forward stdin to the GUI or process
        self.stdin_signal.emit(f"Received input: {input_data}\n")