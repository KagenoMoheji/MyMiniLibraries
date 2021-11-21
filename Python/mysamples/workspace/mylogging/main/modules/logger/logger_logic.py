'''
loggingのログ出力のレベル等の調整ロジックを実装する場所
'''
from logging import (
    Filter,
    INFO
)

class LoggingFilterInfoAndUnder(Filter):
    '''
    Info以下のメッセージのみにフィルタリングする．
    '''
    def filter(self, record):
        return record.levelno <= INFO
