import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
import re
from datetime import datetime as dt
from modules.myutils.mysingleton import Singleton

class MyLogger(Singleton):
    __MAP_LOGLEVEL = {
        "DEBUG": 1,
        "INFO": 2,
        "WARNING": 3,
        "ERROR": 4,
        "CRITICAL": 5
    }
    __loglevel = ""
    __fmt_log = ""
    __len_msecs = 0
    __fmt_date = ""
    __console = True
    __fname = None
    __appname = ""
    def _init_instance(self,
        loglevel,
        fmt_log = "{asctime}.{msecs:03d}@{appname}:{levelname}: {message}",
        fmt_date = "{Y:04d}-{m:02d}-{d:02d} {H:02d}:{M:02d}:{S:02d}",
        console = True,
        fname = None,
        appname = "APPNAME"):
        if not loglevel in MyLogger.__MAP_LOGLEVEL.keys():
            raise ValueError(
                "loglevel should selected from {}".format(MyLogger.__MAP_LOGLEVEL.keys()))
        MyLogger.__loglevel = loglevel
        MyLogger.__fmt_log = fmt_log
        if re.fullmatch(r"^.*{msecs:0[1-9]+d}.*$", MyLogger.__fmt_log):
            MyLogger.__len_msecs = int(re.search(r"{msecs:0([1-9]+)d}", MyLogger.__fmt_log).group(1))
        else:
            MyLogger.__len_msecs = 3
        MyLogger.__fmt_date = fmt_date
        MyLogger.__console = console
        MyLogger.__fname = fname
        MyLogger.__appname = appname

        os.makedirs("/".join(MyLogger.__fname.split("/")[:-1]) + "/", exist_ok = True)

    @staticmethod
    def __output(msg, loglevel, appname = None) -> Exception:
        if MyLogger.__MAP_LOGLEVEL[loglevel] < MyLogger.__MAP_LOGLEVEL[MyLogger.__loglevel]:
            return None
        now = dt.now()
        msecs = now.microsecond
        log = MyLogger.__fmt_log.format(
            asctime = MyLogger.__fmt_date.format(
                Y = now.year, m = now.month, d = now.day,
                H = now.hour, M = now.minute, S = now.second),
            msecs = int(msecs / pow(10, (6 - MyLogger.__len_msecs))),
            appname = appname if appname else MyLogger.__appname,
            levelname = loglevel,
            message = msg)
        if MyLogger.__fname is not None:
            try:
                with open(MyLogger.__fname, mode = "a", encoding = "utf-8") as f:
                    f.write(log + "\n")
            except Exception as e:
                return e
        if MyLogger.__console:
            print(log)
        return None

    @staticmethod
    def debug(msg, appname = None):
        MyLogger.__output(msg, "DEBUG", appname)
    @staticmethod
    def info(msg, appname = None):
        MyLogger.__output(msg, "INFO", appname)    
    @staticmethod
    def warn(msg, appname = None):
        MyLogger.__output(msg, "WARNING", appname)
    @staticmethod
    def error(msg, appname = None):
        MyLogger.__output(msg, "ERROR", appname)
    @staticmethod
    def critical(msg, appname = None):
        MyLogger.__output(msg, "CRITICAL", appname)