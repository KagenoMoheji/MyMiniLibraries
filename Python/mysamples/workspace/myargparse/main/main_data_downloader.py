import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/.".format(PYPATH)
sys.path.append(ROOTPATH)

import traceback
import datetime

from modules.const.tz import TZ_JST
from modules.argparser.argparser_data_downloader import get_parser


def main():
    try:
        parser = get_parser(
            datetime.datetime.now(TZ_JST),
            PYPATH,
            __name__
        )
        args = parser.parse_args()
    except Exception as e:
        raise type(e)("Failed in loading cli args. Detail: {}".format(traceback.format_exc()))

    print(args.targetDate) # `-d=-1`とかで渡す
    print(args.envFile)


if __name__ == "__main__":
    main()