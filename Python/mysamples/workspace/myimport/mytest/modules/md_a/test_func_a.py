import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
sys.path.append(PYPATH + "./../") # main・testディレクトリの場所．testディレクトリ下のモジュールからimportもあり得るため．
import unittest
from mytest_tools.md_tool_c import func_c # カレントディレクトリからのimportは，sys.path.append()で上のディレクトリを指定してそこからの絶対Pimportできず，カレントディレクトリからの相対importでないといけない…？


