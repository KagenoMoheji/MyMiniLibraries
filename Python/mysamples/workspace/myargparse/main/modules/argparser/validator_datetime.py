from argparse import ArgumentTypeError
import re
import datetime

from modules.const.tz import TZ_JST

def valid_yyyymmdd_or_datediff(datetime_ref):
    '''
    - Args
        - datetime_ref:datetime.datetime: 基準日付．タイムゾーンに注意すること．
    - Returns
        - validate:func: 引数バリデータを返す．
    '''
    def validate(input):
        '''
        - Args
            - input:str: argparse.ArgumentParserが受け取った入力
                - `<int>d`の場合：整数の日数を`datetime_ref`に加算した結果をdatetime.datetime型にして返す
                - `yyyyMMdd`の場合：その年月日のままdatetime.datetime型にして返す
        - Returns
            - :datetime.datetime: 日付
        - MEMO
            - datetime.date型ではなくdatetime.datetimeを返す理由
                - タイムゾーンを気にした
        '''
        try:
            res_regex = re.search(r"^(.+)d$", input)
            if res_regex:
                # `<int>d`とみなして取得を試みる
                datediff = int(res_regex.group(1))
                return datetime_ref + datetime.timedelta(days = datediff)
            else:
                # `yyyyMMdd`とみなして取得を試みる
                return datetime.datetime.strftime(input, "%Y%m%d").replace(tzinfo = TZ_JST)
        except (TypeError, ValueError) as e:
            raise ArgumentTypeError(
                "[input: {}]Invalid format for `yyyyMMdd` or `<int>d`.".format(input)
            )
        except Exception as e:
            raise e
    return validate

