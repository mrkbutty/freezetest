# freezetest

**Describe the bug**
Running a windows exe via PATH instead of full path to exe changes the python sys.path.
When using frozen scripts which use dynamic imports of local modules it fails because cannot find module.

**To Reproduce**
See repo at: https://github.com/mrkbutty/freezetest

No problem running direct from dist:

```
>dist\freezetest.exe
Hello, from main file: freezetest.py
I think progdir is C:\Code\freezetest\dist
I think path is ['C:\\Code\\freezetest\\dist', 'C:\\Code\\freezetest\\dist\\lib\\library.zip', 'C:\\Code\\freezetest\\dist\\lib']
Hello, from subfunc file: C:\Code\freezetest\dist\tools\submod.py
I think progdir is C:\Code\freezetest\dist
I think path is ['C:\\Code\\freezetest\\dist', 'C:\\Code\\freezetest\\dist\\lib\\library.zip', 'C:\\Code\\freezetest\\dist\\lib']
```


Issue when running after dist moved C:\tmp\dist and C:\tmp\dist is added into windows PATH and I run from working directory C:\:

```
>freezetest
Hello, from main file: freezetest.py
I think progdir is c:\tmp\dist
I think path is ['C:\\', 'c:\\tmp\\dist\\lib\\library.zip', 'c:\\tmp\\dist\\lib']
Traceback (most recent call last):
  File "C:\Code\freezetest\.venv\Lib\site-packages\cx_Freeze\initscripts\__startup__.py", line 113, in run
    module_init.run(name + "__main__")
  File "C:\Code\freezetest\.venv\Lib\site-packages\cx_Freeze\initscripts\Console.py", line 15, in run
    exec(code, module_main.__dict__)
  File "freezetest.py", line 19, in <module>
  File "freezetest.py", line 15, in main
  File "c:\program files\python38\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tools.submod'
Steps to reproduce the behavior
```

**Expected behavior**
I did not expect the sys.path to change depending on how the exe was executed.


**Desktop (please complete the following information):**
 - Platform information: Microsoft Windows [Version 10.0.19043.1415]
 - OS architecture: amd64
 - cx_Freeze version: 6.9
 - Python version: 3.8.10

**Additional context**
Took me a long time to figure this out after converting from pyinstaller to cx_freeze because I wanted the easier to setup multiple exe support.  I could not figure why unfrozen would work, but installed program in the path would not work.