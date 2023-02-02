from inspect import ismethod

from modules.exception.instantiation import NotInstantiatedError, ReinstantiateWithArgsError

class Singleton(object):
    '''
    シングルトンクラス。
    [継承するサブクラスにおける実装ルール]
    ・初回インスタンス生成時のみ実行する処理(フィールドに格納するなど)は、Singletonクラスのサブクラスにおいてprivate関数"_init_instance()"にオーバーライド(@staticmethod付けない！)する形で行う。
    ・"_init_instance()"に呼び出される初回インスタンス生成時のみに呼び出されるその他関数(たぶん@staticmethod付けない方がいい)の関数名は、"_"で始まるものとする。
    ・メソッドは基本"@staticmethod"を付けて静的にする。
    ・private関数の関数名は"__”で始まるものとする。
    '''
    instantiated = False
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # インスタンス生成されていなかったらここで生成。したがってインスタンス生成済みなら再生成されない。
            cls._instance = super(Singleton, cls).__new__(cls)
            # インスタンス生成時のみに実行する関数を実行。この関数では例えばフィールド(インスタンス変数)に値を格納するとか。
            cls._instance._init_instance(*args, **kwargs)
            # TODO(*1): ここらへんでinstantiated=Trueにしたい．
            # print(cls._instance.__class__.__dict__)
        else:
            # TODO(*3): 2回目以降のインスタンス化されるときにインスタンスではなくクラスを返すのは？
            if len(args) > 0 or len(kwargs) > 0:
                # シングルトンクラスの初回インスタンス化が済んであるなら，それ以外の場所はコンストラクタ引数無しで良くね，という制約を設ける
                raise ReinstantiateWithArgsError(cls.__name__)
        return cls._instance

    def _init_instance(*args, **kwargs):
        pass
    
    def __getattribute__(self, key):
        '''
        - Refs
            - https://ttsubo.hatenablog.com/entry/2014/05/04/215202
            - https://stackoverflow.com/a/371833/15842506
        '''
        if key == "__dict__":
            # `{Singletonのサブクラス}.__dict__`は取得できるのに，`{Singletonのサブクラス}().__dict__`は空になる事象に対し，空にならないようにする．
            return object.__getattribute__(self, "__class__").__dict__
        # MEMO: 「フィールド変数へアクセスしようとしている」以外の型は何か？
        print("[{0}]{1}: {2}({3}, {4})".format(
            object.__getattribute__(self, "instantiated"),
            key,
            object.__getattribute__(self, key),
            type(object.__getattribute__(self, key)),
            ismethod(object.__getattribute__(self, key))
        ))
        res = object.__getattribute__(self, key)
        if not ismethod(res) and \
            not object.__getattribute__(self, "instantiated"): # TODO(*2): 機能してなさそう(*3へ移る)
            # インスタンス化せずにフィールド変数とかにアクセスしようとしていたらエラー # TODO: まだ解決してない(*2へ移る)
            # TODO: クラス名を渡せるようにしたい！ただmaxrecursionerrorがな・・・
            raise NotInstantiatedError(self)
        return res

