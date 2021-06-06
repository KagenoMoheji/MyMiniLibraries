import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
sys.path.append(PYPATH + "./../") # main・testディレクトリの場所．testディレクトリ下のモジュールからimportもあり得るため．
import unittest
from mytest.mytest_tools.myunittest import MyTestCase
from main.modules.myutils.mydict import MyDict


# @unittest.skip("テスト完了のためスキップ")
class TestExistNestedKeys(MyTestCase):
    def setUp(self):
        '''
        setUp()はunittest.TestCaseクラスにおいて各テスト関数の前に実施される関数．
        '''
        self._dict_data = MyDict({
            "aaa": {
                "bbb": {
                    "ddd": 3
                }
            }
        })
        
    def test_return_true(self):
        '''
        存在するネストしたキーの組み合わせの場合Trueを返す．．
        '''
        self.assertTrue(self._dict_data.exist_nested_keys("aaa"))
        self.assertTrue(self._dict_data.exist_nested_keys("aaa", "bbb"))
        self.assertTrue(self._dict_data.exist_nested_keys("aaa", "bbb", "ddd"))
        
    def test_return_false(self):
        '''
        存在しないキーの場合Falseを返す．
        '''
        self.assertFalse(self._dict_data.exist_nested_keys("zzz"))
        self.assertFalse(self._dict_data.exist_nested_keys("aaa", "ccc"))
        self.assertFalse(self._dict_data.exist_nested_keys("aaa", "bbb", "ccc"))
    



# @unittest.skip("テストコード実装中のためスキップ")
class TestValidateRequiredKeyexistType(MyTestCase):
    # @unittest.skip("テスト完了のためスキップ")
    def test_true1(self):
        defdict = {}
        d = {}
        res, err = MyDict(d).validate_required_keyexist_type(defdict)
        self.assertTrue(res)
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_true2(self):
        defdict = {
            "a": str
        }
        d = {
            "a": "hello"
        }
        res, err = MyDict(d).validate_required_keyexist_type(defdict)
        self.assertTrue(res)
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_true3(self):
        defdict = {
            "a": int
        }
        d = {
            "a": 199
        }
        res, err = MyDict(d).validate_required_keyexist_type(defdict)
        self.assertTrue(res)
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_true4(self):
        defdict = {
            "a": [float]
        }
        d = {
            "a": [8.33]
        }
        res, err = MyDict(d).validate_required_keyexist_type(defdict)
        self.assertTrue(res)
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_true5(self):
        defdict = {
            "a": {
                "b": [str]
            },
            "c": int
        }
        d = {
            "a": {
                "b": ["aaa", "bbb"]
            },
            "c": 23,
            "d": False
        }
        res, err = MyDict(d).validate_required_keyexist_type(defdict)
        self.assertTrue(res)
    
#     @unittest.skip("テスト完了のためスキップ")
    def test_true6(self):
        defdict = {
            "a": {
                "[category_name]": {
                    "b": str,
                    "d": [int]
                }
            }
        }
        d = {
            "a": {
                "cat1": {
                    "b": "cat1",
                    "d": [1, 2]
                },
                "cat2": {
                    "b": "cat2",
                    "d": [3, 4]
                }
            }
        }
        res, err = MyDict(d).validate_required_keyexist_type(defdict)
        self.assertTrue(res)
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_false1(self):
        def run_false1():
            defdict = {
                "a": {
                    "b": [str]
                },
                "c": int
            }
            d = {
                "a": {
                    "b": ["aaa", 1] # ここ
                },
                "c": 23
            }
            res, err = MyDict(d).validate_required_keyexist_type(defdict)
            if not res:
                raise err
        self.assertException(
            run_false1,
            TypeError("Invalid type in list of key 'b'.")
        )()
        
    # @unittest.skip("テスト完了のためスキップ")
    def test_false2(self):
        def run_false2():
            defdict = {
                "a": {
                    "b": [str]
                },
                "c": int
            }
            d = {
                "a": {
                    "b": ["aaa", "1"]
                }
                # ここ
            }
            res, err = MyDict(d).validate_required_keyexist_type(defdict)
            if not res:
                raise err
        self.assertException(
            run_false2,
            KeyError("Not found key 'c'.")
        )()
        
    # @unittest.skip("テスト完了のためスキップ")
    def test_false3(self):
        def run_false3():
            defdict = {
                "a": {
                    "b": [str]
                },
                "c": int
            }
            d = {
                "a": {
                    "b": ["aaa", "1"]
                },
                "c": None # ここ
            }
            res, err = MyDict(d).validate_required_keyexist_type(defdict)
            if not res:
                raise err
        self.assertException(
            run_false3,
            TypeError("Invalid type in key 'c'.")
        )()
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_false4(self):
        def run_false4():
            defdict = {
                "a": {
                    "[category_name]": {
                        "b": str,
                        "d": [int]
                    }
                }
            }
            d = {
                "a": {
                    "cat1": {
                        "b": "cat1",
                        "d": [1, 2]
                    },
                    "cat2": {
                        "b": "cat2"
                        # ここ
                    }
                }
            }
            res, err = MyDict(d).validate_required_keyexist_type(defdict)
            if not res:
                raise err
        self.assertException(
            run_false4,
            KeyError("Not found key 'd'.")
        )()
    
    # @unittest.skip("テスト完了のためスキップ")
    def test_false5(self):
        def run_false5():
            defdict = {
                "a": {
                    "[category_name]": {
                        "b": str,
                        "d": [int]
                    },
                    "aaa": str # ここ
                }
            }
            d = {
                "a": {
                    "cat1": {
                        "b": "cat1",
                        "d": [1, 2]
                    },
                    "cat2": {
                        "b": "cat2",
                        "d": [3, 4]
                    }
                }
            }
            res, err = MyDict(d).validate_required_keyexist_type(defdict)
            if not res:
                raise err
        self.assertException(
            run_false5,
            KeyError("Found other keys in the same layer of key '\[category_name\]'.")
        )()
        
    # @unittest.skip("テスト完了のためスキップ")
    def test_false6(self):
        def run_false6():
            defdict = {
                "a": {
                    "b": [str]
                },
                "c": int
            }
            d = {
                "a": {}, # ここ
                "c": 23
            }
            res, err = MyDict(d).validate_required_keyexist_type(defdict)
            if not res:
                raise err
        self.assertException(
            run_false6,
            KeyError("Not found key 'b'.")
        )()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


