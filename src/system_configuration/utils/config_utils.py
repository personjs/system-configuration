import configparser

def get_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    # Parse specific sections and store values or return the config object
    window_width = int(config['Window']['width'])
    window_height = int(config['Window']['height'])
    window_title = config['Window']['title']
    window_theme = config['Window']['theme']

    logging_filename = config['Logging']['filename']
    logging_level = config['Logging']['level']

    return {
        "window_width": window_width,
        "window_height": window_height,
        "window_title": window_title,
        "window_theme": window_theme,
        "logging_filename": logging_filename,
        "logging_level": logging_level,
    }
