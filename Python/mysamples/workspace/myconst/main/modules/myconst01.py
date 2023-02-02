from modules.mysingleton import Singleton
from modules.exception.const import ConstError, UndefinedConstError
from modules.exception.instantiation import NotInstantiatedError, ReinstantiateWithArgsError

class GlobalConsts01(Singleton):
    '''
    グローバルクラス定数をシングルトンクラスと__setattr__()による再代入制約により実現．
    # Usage
    1. GlobalConstsシングルトンクラスを継承
    2. (サブクラスにてクラス変数として初期値Noneで登録)
    3. `GlobalConsts01._init_instance()`内でクラス変数の値を設定
        - 静的であれば手入力で設定
        - 初期化時のみ引数から動的に設定するならば引数を使う
    4. サブクラスを実行可能Pythonの処理の初めにクラス定数の初期値を引数に渡してインスタンス化
    5. サブクラスのクラス定数を使う箇所で適宜，毎回インスタンス化(引数なしでOK)して使う
        - インスタンス化しないと再代入制約は機能しないので注意！
    '''
    def __setattr__(self, key, val):
        '''
        - 定数クラスのクラス変数の登録されていなければ例外投げる
        - 定数クラスの(GlobalConsts01)初期化時以外でクラス変数の書き換えしようとすると，例えクラス変数が初期値Noneであっても例外投げる
        '''
        if key not in self.__class__.__dict__:
            raise UndefinedConstError("Undefined const '{}'.".format(key))
        raise ConstError("Can't rebind const '{}'.".format(key)) # これは「いずれにしろ登録と初期値代入は_init_instance()で済ませているので再代入エラー」
        # if GlobalConsts.__dict__[key] is not None: # これは「登録してあり初期値代入済みなので再代入エラー」
        #     raise ConstError("Can't rebind const '{}'.".format(key))
        # if key in GlobalConsts.__dict__: # これは「初期値代入がどうあれ登録済みなので再代入エラー」
        #     raise ConstError("Can't rebind const '{}'.".format(key))




'''
# 定数クラスの参考
- https://qiita.com/nadu_festival/items/c507542c11fc0ff32529#%E3%83%A1%E3%82%BF%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AE%E5%88%A9%E7%94%A8
- https://ytyaru.hatenablog.com/entry/2018/10/29/000000
- https://maku77.github.io/python/syntax/const.html
- https://cream-worker.blog.jp/archives/1077207909.html
- https://www.headboost.jp/python-property/


# クラス内で自分のクラスを取得する方法メモ
class A(Exception):
    def __init__(self):
        print(A.__name__) # A
        # print(self.__name__) # ERROR
        print(self.__class__.__name__) # A
        print(type(A)) # <class 'type'>
        print(type(A).__class__) # <class 'type'>
        print(type(A).__name__) # type
        print(type(A).__class__.__name__) # type
        print(type(self).__class__) # <class 'type'>
        print(type(self).__name__) # A
        print(type(self).__class__.__name__) # type

A()
'''