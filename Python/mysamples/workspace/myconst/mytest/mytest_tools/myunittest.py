import re
import unittest
import traceback

class MyTestCase(unittest.TestCase):
    def assertException(self, func, expect_exception, check_err_msg = False):
        '''
        - Args
            - func::例外処理テストをする関数．
            - expect_exception::Exceptionクラスを継承した例外クラスのインスタンス．例外クラスに渡すエラーメッセージは正規表現可．
        - Returns
            - 引数funcの戻り値
        '''
        def run(*args, **kwargs):
            '''
            - Args
                - funcの引数．
            - Returns
                - funcの戻り値
            '''
            ret = None
            try:
                ret = func(*args, **kwargs)
                # TODO: Failureが出たらそこで止まるのではなく，すべての試験を一周してから全体の結果を出す方法どうやる？
                self.fail(msg = "No Exception!") # https://docs.python.org/ja/3/library/unittest.html#unittest.TestCase.fail
            except unittest.TestCase.failureException as e:
                raise e
            except Exception as e:
                # エラー名の比較
                self.assertEqual(
                    expect_exception.__class__.__name__,
                    e.__class__.__name__)
                
                if check_err_msg:
                    # エラー短文の比較
                    ## 完全一致より正規表現マッチングの方が良い．
                    # self.assertEqual(
                    #     traceback.format_exception_only(type(expect_exception), expect_exception)[0].rstrip("\n"),
                    #     traceback.format_exception_only(type(e), e)[0].rstrip("\n"))
                    self.assertRegex(
                        traceback.format_exception_only(type(e), e)[0]
                            .replace("[", "#") # []のエスケープ対応が難しかったので，置換で対応．
                            .replace("]", "#")
                            .rstrip("\n"),
                        "^{}$".format(traceback.format_exception_only(type(expect_exception), expect_exception)[0]
                                    .replace("\[", "#") # []のエスケープ対応が難しかったので，置換で対応．
                                    .replace("\]", "#")
                                    .rstrip("\n")))
            return ret
        return run