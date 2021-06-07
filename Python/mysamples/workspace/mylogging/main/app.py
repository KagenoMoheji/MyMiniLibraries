import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
sys.path.append(PYPATH + ".")
from conf.conf_logging import CONF_LOGGER
from modules.logger.logger import (
    init_logging,
    get_logger
)
from modules.md_a.a import (
    func_warn, func_error
)



def main():
    # アプリ全体で用いるロギングの初期設定とloggerオブジェクト取得
    init_logging(
        CONF_LOGGER,
        PYPATH + "./../logs/test.log")
    logger = get_logger(__name__)

    logger.info("Start app.")

    func_warn("hoge", get_logger = get_logger)
    func_error("fuga")




if __name__ == "__main__":
    main()