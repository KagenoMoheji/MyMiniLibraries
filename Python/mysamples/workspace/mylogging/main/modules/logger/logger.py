import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
from logging import getLogger
from logging.config import dictConfig

def init_logging(CONF_LOGGER, filename = None):
    '''
    - Args
        - CONF_LOGGER:func: loggingの辞書型設定を戻り地とする関数．
        - filename:str: ログ出力ファイル名．ファイル出力したくない場合はNoneを．
    '''
    NAME_FILEHANDLER = "fileHandler"
    conf_logger = CONF_LOGGER(filename)

    if filename:
        os.makedirs("/".join(filename.split("/")[:-1]) + "/", exist_ok = True)
    else:
        del conf_logger["handlers"][NAME_FILEHANDLER]
        for logger in conf_logger["loggers"]:
            if NAME_FILEHANDLER in conf_logger["loggers"][logger]["handlers"]:
                pre_handlers = conf_logger["loggers"][logger]["handlers"]
                conf_logger["loggers"][logger]["handlers"] = [handler for handler in pre_handlers if handler != NAME_FILEHANDLER]

    dictConfig(conf_logger)

def get_logger(appname):
    return getLogger(appname)