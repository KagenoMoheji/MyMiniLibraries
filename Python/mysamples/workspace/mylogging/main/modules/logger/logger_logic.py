'''
loggingのログ出力のレベル等の調整ロジックを実装する場所
'''
from logging import (
    Filter,
    Formatter,
    INFO
)
import datetime
from modules.const.tz import TZ_JST


class LoggingFilterInfoAndUnder(Filter):
    '''
    Info以下のメッセージのみにフィルタリングする．
    '''
    def filter(self, record):
        return record.levelno <= INFO

class LoggingFormatterAsJST(Formatter):
    '''
    時刻をJSTに変換する．
    - Refs
        - https://stackoverflow.com/a/47104004/15842506
        - https://gist.github.com/fortune/9cfa6f0cb4878b63e5027d8ecba6e966#%E5%AE%A3%E8%A8%80%E7%9A%84%E3%81%AA%E3%83%AD%E3%82%AE%E3%83%B3%E3%82%B0%E8%A8%AD%E5%AE%9A
    '''
    def converter(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp).astimezone(TZ_JST).timetuple()
