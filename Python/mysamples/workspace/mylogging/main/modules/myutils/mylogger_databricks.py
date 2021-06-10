import os
import re
import uuid
from datetime import (
    datetime as dt,
    timedelta,
    timezone
)
import time
from modules.myutils.mydbutils import (
    dbfs_path_spark2nonspark,
    dbutils_exists
)

TZ_JST = timezone(timedelta(hours = 9), "JST")

'''
[メインコード側での使い方]
APPNAME = "appname"
FNAMES_LOG = {
    "mylogger": "dbfs:/FileStore/logs/{}/mylogger.log".format(APPNAME) # FS_ROOT_SPARK + "/logs/{}/mylogger.log".format(APPNAME)
}
logger = MyLogger(
    "INFO",
    console = True,
    fname = FNAMES_LOG["mylogger"],
    appname = APPNAME)

logger.info("infotest")
logger.debug("debugtest")



'''


class TmpLogStacks(Singleton):
    '''
    Sparkの分散処理において，複数ワーカーノードが同一ログファイルに(一時ファイルをコピーしていくという)アクセスする段階で，
    アクセス順が入れ替わってログの順序がズレたり，先に入るべきログが消えたりしないように，アクセス順を担保するためのログ出力の
    状態を管理するシングルトンスタックを用意する．
    '''
    __stacks_started = {}
    __stacks_completed = {}
    def _init_instance(self):
        TmpLogStacks.__stacks_started = {}
        TmpLogStacks.__stacks_completed = {}
    
    @staticmethod
    def clear_stacks():
        TmpLogStacks.__stacks_started = {}
        TmpLogStacks.__stacks_completed = {}
    
    @staticmethod
    def push_started(fname_target, fname_tmp):
        if fname_target in TmpLogStacks.__stacks_started.keys():
            TmpLogStacks.__stacks_started[fname_target].append(fname_tmp)
        else:
            TmpLogStacks.__stacks_started[fname_target] = [fname_tmp]
        # print("Pushed started: {}".format(TmpLogStacks.__stacks_started))
        
    @staticmethod
    def push_completed(fname_target, fname_tmp):
        if fname_target in TmpLogStacks.__stacks_completed.keys():
            TmpLogStacks.__stacks_completed[fname_target].append(fname_tmp)
        else:
            TmpLogStacks.__stacks_completed[fname_target] = [fname_tmp]
        # print("Pushed completed: {}".format(TmpLogStacks.__stacks_completed))

    @staticmethod
    def get_pre_started(fname_target, fname_tmp):
        if not fname_target in TmpLogStacks.__stacks_started.keys():
            return None
        if not fname_tmp in TmpLogStacks.__stacks_started[fname_target]:
            return None
        return TmpLogStacks.__stacks_started[fname_target][TmpLogStacks.__stacks_started[fname_target].index(fname_tmp) - 1]
    
    @staticmethod
    def get_pre_completed(fname_target, fname_tmp):
        if not fname_target in TmpLogStacks.__stacks_completed.keys():
            return None
        if not fname_tmp in TmpLogStacks.__stacks_completed[fname_target]:
            return None
        return TmpLogStacks.__stacks_completed[fname_target][TmpLogStacks.__stacks_completed[fname_target].index(fname_tmp) - 1]

    @staticmethod
    def count_started(fname_target):
        if not fname_target in TmpLogStacks.__stacks_started.keys():
            return 0
        return len(TmpLogStacks.__stacks_started[fname_target])
    
    @staticmethod
    def get_last_completed(fname_target):
        if not fname_target in TmpLogStacks.__stacks_completed.keys():
            return None
        return TmpLogStacks.__stacks_completed[fname_target][-1]


class MyLogger():
    __DIR_TMP_LOGS = "dbfs:/FileStore/logs/tmp" # FS_ROOT_SPARK + "/logs/tmp"
    __MAP_LOGLEVEL = {
        "DEBUG": 1,
        "INFO": 2,
        "WARNING": 3,
        "ERROR": 4,
        "CRITICAL": 5
    }
    def __init__(self,
        loglevel,
        fmt_log = "{asctime}.{msecs:03d}@{appname}:{levelname}: {message}",
        fmt_date = "{Y:04d}-{m:02d}-{d:02d} {H:02d}:{M:02d}:{S:02d}",
        console = True,
        fname = None,
        appname = "APPNAME"):
        if not loglevel in self.__MAP_LOGLEVEL.keys():
            raise ValueError(
                "loglevel should selected from {}.".format(self.__MAP_LOGLEVEL.keys()))
        self.__loglevel = loglevel
        self.__fmt_log = fmt_log
        if re.fullmatch(r"^.*{msecs:0[1-9][0-9]*d}.*$", self.__fmt_log):
            self.__len_msecs = int(re.search(r"{msecs:0([1-9][0-9]*)d}", self.__fmt_log).group(1))
            if self.__len_msecs > 6:
                # マイクロ秒の6桁を超える桁数だったら⑥桁にする
                self.__fmt_log = re.sub(r"{msec:0[1-9][0-9]*d)}", "{msecs:06d}", self.__fmt_log)
                self.__len_msecs = 6
        else:
            self.__len_msecs = 3
        self.__fmt_date = fmt_date
        self.__console = console
        self.__fname = fname
        self.__appname = appname

        # (一時・最終)ログファイル出力先のディレクトリがなければ作っておく
        dbutils.fs.mkdirs(self.__DIR_TMP_LOGS)
        dbutils.fs.mkdirs("/".join(self.__fname.split("/")[:-1]) + "/")

        # 一時ログファイルのシングルトンスタック(TmpLogStacks)の中身をクリア
        TmpLogStacks.clear_stacks()

    def __del__(self):
        # MyLoggerオブジェクトが削除される際に，一時ファイルをすべて消す
        dbutils.fs.rm(self.__DIR_TMP_LOGS, recurse = True)
    
    def __output(self, msg, loglevel, appname = None) -> Exception:
        if self.__MAP_LOGLEVEL[loglevel] < self.__MAP_LOGLEVEL[self.__loglevel]:
            return None
        now = dt.now(TZ_JST)
        log = self.__fmt_log.format(
            asctime = self.__fmt_date.format(
                Y = now.year, m = now.month, d = now.day,
                H = now.hour, M = now.minute, S = now.second),
            msecs = int(now.microsecond / pow(10, (6 - self.__len_msecs))),
            appname = appname if appname else self.__appname,
            levelname = loglevel,
            message = msg)
        if self.__fname is not None:
            try:
                fname_tmp = "{0}{1}_{2}.log".format(
                    self.__DIR_TMP_LOGS,
                    int(time.mktime(now.timetuple())),
                    str(uuid.uuid4()))
                TmpLogStacks.push_started(self.__fname, fname_tmp)
                pre_log = ""
                if TmpLogStacks.count_started(self.__fname) > 1:
                    pre_fname = TmpLogStacks.get_pre_started(self.__fname, fname_tmp)
                    while pre_fname != TmpLogStacks.get_last_completed(self.__fname):
                        time.sleep(1)
                    with open(dbfs_path_spark2nonspark(pre_fname_tmp), mode = "r", encoding = "utf-8") as f:
                        pre_log = f.read()
                    dbutils.fs.rm(pre_fname_tmp)
                else:
                    if dbutils_exists(self.__fname):
                        # 同じ最終出力ファイルが既存だった場合，そのログを取得しておく
                        with open(dbfs_path_spark2nonspark(self.__fname), mode = "r", encoding = "utf-8") as f:
                            pre_log = f.read()
                dbutils.fs.put(fname_tmp, pre_log + log + "\n")
                dbutils.fs.cp(fname_tmp, self.__fname)
                TmpLogStacks.push_completed(self.__fname, fname_tmp)
            except Exception as e:
                return e
        if self.__console:
            print(log)
        return None
    
    def debug(self, msg, appname = None):
        err = self.__output(msg, "DEBUG", appname)
        if err is not None:
            raise err
    def info(self, msg, appname = None):
        err = self.__output(msg, "INFO", appname)
        if err is not None:
            raise err
    def warn(self, msg, appname = None):
        err = self.__output(msg, "WARNING", appname)
        if err is not None:
            raise err
    def error(self, msg, appname = None):
        err = self.__output(msg, "ERROR", appname)
        if err is not None:
            raise err
    def critical(self, msg, appname = None):
        err = self.__output(msg, "CRITICAL", appname)
        if err is not None:
            raise err