@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON=py"
) else (
    where python >nul 2>nul
    if not %errorlevel%==0 (
        echo Python was not found.
        echo Install Python 3.10 or newer from https://www.python.org/downloads/
        pause
        exit /b 1
    )
    set "PYTHON=python"
)

%PYTHON% -m pip install -r requirements.txt
if errorlevel 1 (
    echo Could not install the game dependency.
    pause
    exit /b 1
)

%PYTHON% first_class.py
pause
