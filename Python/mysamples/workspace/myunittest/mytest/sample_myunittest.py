import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/./../main".format(PYPATH) # 本番コードの場所をimportのRootPathにする．本番コード内のモジュールimportが本番コードのRootPathを基準にしてるから．
sys.path.append(ROOTPATH)
import unittest
# mytest下にあるモジュールは相対インポートしてくることとする．
from mytest_tools.myunittest import MyTestCase


def sample1(msg):
    raise KeyError(msg)

def sample2(msg):
    raise KeyError(msg + "61" + msg)

def sample3(msg):
    raise ValueError(msg)

class TestException(MyTestCase):
    def test_err_sample1_success(self):
        self.assertException(
            sample1,
            KeyError("aaa") # ここで想定する例外・エラー．※メッセージは正規表現可．
        )(
            # ここにsample1の引数
            "aaa"
        )
        
    @unittest.skip("成功だけみたいのでスキップ")
    def test_err_sample1_fail(self):
        '''
        わざとエラーメッセージを違うものにする
        '''
        self.assertException(
            sample1,
            KeyError("aaa")
        )(
            "aaab"
        )
    
    def test_err_sample2_success(self):
        self.assertException(
            sample2,
            KeyError("aaa[0-9].+aaa")
        )(
            "aaa"
        )
    
    @unittest.skip("成功だけみたいのでスキップ")
    def test_err_sample3_fail(self):
        '''
        わざと異なるエラー名にする
        '''
        self.assertException(
            sample3,
            KeyError("aaa")
        )(
            "aaa"
        )


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)