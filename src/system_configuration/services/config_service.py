import configparser
import os

class ConfigService:
    _instance = None  # Singleton instance variable
    
    def __new__(cls, config_file=None):
        # Check if an instance already exists
        if cls._instance is None:
            # If not, create a new instance and load the configuration file
            cls._instance = super(ConfigService, cls).__new__(cls)
            cls._instance._config = configparser.ConfigParser()  # Create ConfigParser object
            
            if config_file:
                cls._instance.load(config_file)  # Load the provided config file
            else:
                raise ValueError("Config file must be provided on the first initialization.")
        
        return cls._instance

    def load(self, config_file):
        """Load configuration from an INI file."""
        if os.path.exists(config_file):
            self._config.read(config_file)
        else:
            raise FileNotFoundError(f"Config file '{config_file}' not found.")

    def get(self, section, key=None, fallback=None):
        """Retrieve a value from the config file."""
        try:
            if key is None:
                return dict(self._config.items(section))
            else:
                return self._config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback

    def getint(self, section, key, fallback=None):
        """Retrieve an integer value from the config file."""
        try:
            return self._config.getint(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback

    def getboolean(self, section, key, fallback=None):
        """Retrieve a boolean value from the config file."""
        try:
            return self._config.getboolean(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback

    def getfloat(self, section, key, fallback=None):
        """Retrieve a float value from the config file."""
        try:
            return self._config.getfloat(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback
