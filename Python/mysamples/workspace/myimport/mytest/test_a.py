import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/./../main".format(PYPATH) # 本番コードの場所をimportのRootPathにする．本番コード内のモジュールimportが本番コードのRootPathを基準にしてるから．
sys.path.append(ROOTPATH)
import unittest
# mytest下にあるモジュールは相対インポートしてくることとする．
# from .mytest_tools.myunittest import MyTestCase
from mytest_tools.md_tool_c import func_c


