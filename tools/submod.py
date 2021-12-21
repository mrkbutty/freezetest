import sys
import os

def getprogdir():
    if getattr(sys, 'frozen', False):
        return getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    else:
        return os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

def subfunc():
    print(f'Hello, from subfunc file: {__file__}')
    print(f'I think progdir is {getprogdir()}')
    print(f'I think path is {sys.path}')
