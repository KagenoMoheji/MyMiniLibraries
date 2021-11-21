from modules.logger.logger_logic import (
    LoggingFilterInfoAndUnder
)


def CONF_LOGGER(filename):
    '''
    個々に記載のキーはデフォルトなので削除しないように．
    キーの追加削除するのは`main/modules/logger/logger.init_logging()`をパクって，その関数内でやる．
    したがってこちらでなにか追加したいなら`main/modules/logger/logger.init_loggin()`をパクった関数で検証してからデフォルトのここに合流させるか検討する流れを踏むこと．
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
        "filters": {
            "infoandunder": {
                "()": LoggingFilterInfoAndUnder
            }
        },
        "handlers": {
            "consoleHandler": { # (**)INFO以下はstdoutで出力
                "class": "logging.StreamHandler",
                # "level": "INFO", # こっちだと「INFO以上」になってしまう
                "filters": ["infoandunder"], # こっちで「INFO以下」でログ出力するようにする
                "formatter": "default", # "formatters"から選択
                "stream": "ext://sys.stdout"
            },
            "stderrHandler": { # (**)WARNING以上はstderrで出力
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "default", # "formatters"から選択
                "stream": "ext://sys.stderr"
            },
            "fileHandler": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "default", # "formatters"から選択
                "filename": filename
            }
        },
        "loggers": {
            "": { # 全て
                "level": "INFO",
                "handlers": ["consoleHandler", "stderrHandler", "fileHandler"], # "handlers"から選択
                "propagate": False
            },
            "__main__": { # 実行可能ファイル自体
                "level": "INFO",
                "handlers": ["consoleHandler", "stderrHandler", "fileHandler"], # "handlers"から選択
                "propagate": False
            },
            # "modules": { # パッケージでの指定もできるらしい．すごいね
            #     "level": "WARNING",
            #     "handlers": ["consoleHandler", "stderrHandler", "fileHandler"], # "handlers"から選択
            #     "propagate": False
            # }
        },
        # "root": {
        #     "level": "WARNING"
        # }
    }