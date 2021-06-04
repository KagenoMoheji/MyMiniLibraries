import time


def process_timer_sec(func):
    '''
    処理時間計測デコレータ。
    処理時間を計測したい関数にアノテーション"@process_timer_sec"をつけると処理時間計測結果を標準出力する。
    - Args
        - func:(*args, **kwargs) -> Any: 処理時間計測する関数
    - Return
        - ret:Any: funcの戻り値
    '''
    def run(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print ("""
-------[process_timer_sec]-------
function: {0}
time: {1}[sec]
---------------------------------
""".format(
      func.__name__,
      time.time() - start))
        return ret
    return run
