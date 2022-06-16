import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/."
sys.path.append(ROOTPATH)
import re
from conf.conf_logging import CONF_LOGGER
from modules.logger.logger import (
    init_logging,
    get_logger
)
from modules.myutils.mylogger import MyLogger
from modules.md_a.a import (
    func_warn, func_error
)



def main():
    # アプリ全体で用いるロギングの初期設定とloggerオブジェクト取得
    init_logging(
        CONF_LOGGER,
        PYPATH + "/../logs/test.log")
    logger = get_logger(__name__)

    logger.info("Start app.")

    func_warn("hoge", get_logger = get_logger)
    func_error("fuga")



    mylogger = MyLogger(
        "INFO",
        fname = PYPATH + "/../logs/mytest.log")
    mylogger.debug("MyLogger debug")
    mylogger.info("MyLogger info")
    mylogger.error(
        "MyLogger error",
        appname = re.split(r"[\\/]", inspect.getfile(inspect.currentframe()))[-1])




if __name__ == "__main__":
    main()