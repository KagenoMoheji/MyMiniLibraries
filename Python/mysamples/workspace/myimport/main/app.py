import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
'''
- importのRootPathをどこにするか
    - 基本的に本番用コードを配置する"main/"をRootPathにすると良さげ．
        - importできるPythonコードの範囲に制限をある程度設け，"mytest/"からテストコードを間違って呼び出すことを防げるから．
    - 本番リリースが無い個人開発とかで楽したいなら"main/"・"mytest/"の上にあるPJディレクトリをRootPathにしても良いかな．
'''
ROOTPATH = "{}/."
sys.path.append(ROOTPATH)
from modules.md_a.a import funcA
