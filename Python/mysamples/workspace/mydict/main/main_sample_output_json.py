import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/.".format(PYPATH)
sys.path.append(ROOTPATH)

from modules.myutils.mydict import MyDict


d = MyDict({
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
})

d.output_json("{}/output.json".format(PYPATH))
