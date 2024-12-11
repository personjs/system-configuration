import os

def ensure_file_exists(filepath):
    """Ensure that a file exists. If not, create it."""
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write("")  # Create an empty file if it doesn't exist
