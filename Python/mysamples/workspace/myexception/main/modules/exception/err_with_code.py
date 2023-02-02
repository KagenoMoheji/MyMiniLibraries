'''
バッチ処理等のログの最後に表示させるエラーコードを一意に紐づけた例外クラスを一元管理するモジュール．
エラーコードを最後に表示させることで，商用環境の運用メンバーがどのエラーなのか一目で識別できるように配慮できる．
'''

class SampleException(Exception):
    def __init__(self, err_code, msg = None):
        self.err_code = err_code
        super().__init__(msg)
