import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"
sys.path.append(PYPATH + ".")
from modules.md_a.a import funcA



def main():
    pass




def __name__ == "__main__":
    main()