from setuptools import setup, find_packages, Command
import os
import shutil

def parse_requirements(filename):
    """Parse the requirements.txt file and return a list of dependencies."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Read dependencies from requirements.txt
install_requires = parse_requirements('requirements.txt')

class CleanCommand(Command):
    """Custom clean command to tidy up the project directory."""

    description = "Clean temporary files"
    user_options = []

    def initialize_options(self):
        """Initialize any options for this command (none for now)."""
        pass

    def finalize_options(self):
        """Finalize the options (none for now)."""
        pass

    def run(self):
        """Run the cleaning process."""
        # Delete __pycache__ directories
        for dirpath, dirnames, filenames in os.walk("."):
            if dirnames == "__pycache__":
                shutil.rmtree(dirpath)
                print(f"Removed {dirpath}")

        # Delete .pyc files
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                if filename.endswith(".pyc"):
                    os.remove(os.path.join(dirpath, filename))
                    print(f"Removed {os.path.join(dirpath, filename)}")

        # Remove build, dist, and egg-info directories
        build_dir = os.path.join(".", "build")
        dist_dir = os.path.join(".", "dist")
        egg_info_dir = os.path.join(".", f"{os.path.basename(os.getcwd())}.egg-info")

        for directory in [build_dir, dist_dir, egg_info_dir]:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"Removed {directory}")

setup(
    name="system_configuration",
    version="1.0.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    setup_requires=['setuptools>=42'],
    extras_require={
        'dev': parse_requirements('requirements-dev.txt'),
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'system_configuration=system_configuration.main:main',
        ],
    },
    cmdclass={
        "clean": CleanCommand,  # Register the custom clean command
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
