import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/./../main".format(PYPATH) # 本番コードの場所をimportのRootPathにする．本番コード内のモジュールimportが本番コードのRootPathを基準にしてるから．
sys.path.append(ROOTPATH)
import unittest
# mytest下にあるモジュールは相対インポートしてくることとする．
from mytest_tools.myunittest import MyTestCase

from modules.myconst01 import GlobalConsts01
from modules.exception.const import ConstError, UndefinedConstError
from modules.exception.instantiation import NotInstantiatedError, ReinstantiateWithArgsError

class CommonInits(GlobalConsts01):
    # PYPATH = None
    # ROOTPATH = None
    # # DIR_ENV = None
    # DIR_OUTPUT_LOGS = None

    def _init_instance(self,
        pypath,
        rootpath,
        dir_output_logs = None):
        CommonInits.PYPATH = pypath
        CommonInits.ROOTPATH = rootpath
        CommonInits.DIR_OUTPUT_LOGS = \
            dir_output_logs if dir_output_logs is not None \
            else "{}/logs".format(CommonInits.PYPATH)
        CommonInits.instantiated = True # TODO: なくしたい



class TestGlobalConsts01(MyTestCase):
    # @unittest.skip("成功なのでスキップ")
    def test_equals_consts(self):
        self.assertEqual(CommonInits().PYPATH, PYPATH)
        self.assertEqual(CommonInits().ROOTPATH, ROOTPATH)
        self.assertEqual(CommonInits().DIR_OUTPUT_LOGS, "{}/logs".format(PYPATH))
        
    def test_const_error(self):
        def run_test_const_error():
            CommonInits().PYPATH = "hoge"
        self.assertException(
            run_test_const_error,
            ConstError("Can't rebind const 'PYPATH'."),
            check_err_msg = True
        )()
    
    def test_undefined_const_error(self):
        def run_test_undefined_const_error():
            CommonInits().GHOST = "ghost"
        self.assertException(
            run_test_undefined_const_error,
            UndefinedConstError("Undefined const 'GHOST'."),
            check_err_msg = True
        )()
    
    def test_reinstantiate_with_args_error(self):
        def run_test_reinstantiate_with_args_error():
            print(CommonInits("hogehoge").PYPATH)
        self.assertException(
            run_test_reinstantiate_with_args_error,
            ReinstantiateWithArgsError(CommonInits.__name__), # TODO: エラー出るべき
            check_err_msg = True
        )()
    
    # @unittest.skip("Failure解消しないので一旦スキップ")
    def test_not_instantiated_error(self):
        # print("===========[{}]==========".format(self._testMethodName))
        def run_test_not_instantiated_error():
            print(CommonInits.PYPATH) # TODO: エラー出るべき
        self.assertException(
            run_test_not_instantiated_error,
            NotInstantiatedError(CommonInits.__name__), # TODO: エラー出るべき
            check_err_msg = True
        )()
    
    def test_second_consts(self):
        class LocalConsts(GlobalConsts01):
            def _init_instance(self,
                greet):
                LocalConsts.WHO = "Taro"
                LocalConsts.GREET = greet
                LocalConsts.instantiated = True # TODO: なくしたい
        LocalConsts(greet = "Hello")
        self.assertEqual(LocalConsts().WHO, "Taro")
        self.assertEqual(CommonInits().PYPATH, PYPATH)
        
        def run_second_undefined_const_error():
            LocalConsts().PYPATH = "hoge"
        self.assertException(
            run_second_undefined_const_error,
            UndefinedConstError("Undefined const 'PYPATH'."),
            check_err_msg = True
        )()


if __name__ == "__main__":
    # グローバルなクラス定数は，処理の初めに宣言するもの．
    CommonInits(
        PYPATH,
        ROOTPATH,
        dir_output_logs = None
    )
    # (1)クラスとインスタンスのそれぞれからフィールドとかのプロパティを取得するとどうなるか確認
    # print("(1-1): ", CommonInits.__dict__)
    # print("(1-2): ", CommonInits().__dict__)
    # (2)クラスとそのインスタンスをオブジェクトから区別する方法を確認
    # print("(2-1): ", type(CommonInits))
    # print("(2-1): ", type(CommonInits()))
    # print("(2-3): ", CommonInits.__class__.__name__)
    # print("(2-4): ", CommonInits().__class__.__name__)
    # print("(2-5): ", type(CommonInits) == CommonInits)
    # print("(2-6): ", type(CommonInits()) == CommonInits)
    # print("(2-7): ", CommonInits.__class__.__name__ == CommonInits.__class__.__name__)
    # print("(2-8): ", CommonInits().__class__.__name__ == CommonInits.__class__.__name__)

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
