import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/.".format(PYPATH)
sys.path.append(ROOTPATH)

import datetime

from modules.const.tz import TZ_JST
from modules.argparser.argparser_data_downloader import get_parser


def main():
    parser = get_parser(
        datetime.datetime.now(TZ_JST),
        PYPATH,
        __name__
    )
    args = parser.parse_args()

    print(args.targetDate) # `-d=-1`とかで渡す
    print(args.envFile)


if __name__ == "__main__":
    main()