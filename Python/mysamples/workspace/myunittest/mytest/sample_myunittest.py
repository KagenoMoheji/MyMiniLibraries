import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
sys.path.append(PYPATH + "./../") # main・testディレクトリの場所．testディレクトリ下のモジュールからimportもあり得るため．
import unittest
from mytest_tools.myunittest import MyTestCase # カレントディレクトリからのimportは，sys.path.append()で上のディレクトリを指定してそこからの絶対Pimportできず，カレントディレクトリからの相対importでないといけない…？


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