@echo off
title _install_requirements

REM Initialize conda
call "%USERPROFILE%\anaconda3\Scripts\activate.bat" >nul 2>&1

REM Check existence of environment name file
if not exist _conda_env_name.txt (
    echo [ERROR] _conda_env_name.txt file not found!
    pause
    exit /b 1
)

set /p environment_name=<_conda_env_name.txt

if "%environment_name%"=="" (
    echo [ERROR] Environment name is empty in _conda_env_name.txt!
    pause
    exit /b 1
)

REM Check if the environment exists
conda env list | findstr /C:"%environment_name%" > nul
if %errorlevel% equ 0 (
    echo [INFO] Found environment '%environment_name%'.
) else (
    echo [ERROR] Conda environment '%environment_name%' does not exist.
    pause
    exit /b 1
)

REM Activate the environment
echo [INFO] Activating conda environment '%environment_name%'...
call conda activate %environment_name%
if %errorlevel% neq 0 (
    echo [ERROR] Unable to activate conda environment %environment_name%.
    pause
    exit /b 1
)

echo [INFO] Conda environment '%environment_name%' activated.
echo [INFO] Going to install libraries from requirements.txt...

if exist requirements.txt (
    echo [INFO] Installing requirements...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] pip install failed!
        pause
        exit /b 1
    )
    echo [SUCCESS] Installation successfully done.
    pause
) else (
    echo [ERROR] File requirements.txt does not exist.
    pause
    exit /b 1
)
