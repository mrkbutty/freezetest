set "PYTHON=c:\program files\python38\python.exe"
if not exist .venv "%PYTHON%" -m venv .venv
call .venv/Scripts/activate.bat
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
