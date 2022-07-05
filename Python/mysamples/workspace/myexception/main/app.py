import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
sys.path.append(PYPATH + ".")

import traceback
from modules.exception.test import TestError

if __name__ == "__main__":
    try:
        raise TestError("テスト例外だよ！")
    except Exception as e:
        raise type(e)("コメントを書き換えたテスト例外だよ！ Detail:{err}".format(
            err = traceback.format_exc()
        ))
