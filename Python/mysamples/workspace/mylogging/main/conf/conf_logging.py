def CONF_LOGGER(filename):
    '''
    '''
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s.%(msecs)03d@%(filename)s:%(levelname)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default", # "formatters"から選択
                "stream": "ext://sys.stdout"
            },
            "fileHandler": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "default", # "formatters"から選択
                "filename": filename
            }
        },
        "loggers": {
            "__main__": {
                "level": "INFO",
                "handlers": ["consoleHandler", "fileHandler"], # "handlers"から選択
                "propagate": False
            },
            "modules": {
                "level": "INFO",
                "handlers": ["consoleHandler", "fileHandler"], # "handlers"から選択
                "propagate": False
            }
        },
        # "root": {
        #     "level": "WARNING"
        # }
    }