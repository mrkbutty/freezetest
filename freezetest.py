import sys
import os
import importlib

def getprogdir():
    if getattr(sys, 'frozen', False):
        return getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    else:
        return os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

def main():
    print(f'Hello, from main file: {__file__}')
    print(f'I think progdir is {getprogdir()}')
    print(f'I think path is {sys.path}')
    impmod = importlib.import_module('tools.submod')
    impmod.subfunc()

if __name__ == '__main__':
    main()