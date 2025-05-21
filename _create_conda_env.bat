@echo off
title _Create Conda Environment

REM Ensure conda is initialized
call conda init >nul 2>&1

REM Check if config file exists
if not exist _conda_env_name.txt (
    echo [ERROR] _conda_env_name.txt file not found!
    pause
    exit /b 1
)

REM Read environment name
set /p environment_name=<_conda_env_name.txt
echo [INFO] Environment name read from file: %environment_name%

REM Check if environment exists
call conda env list | findstr /R /C:"\b%environment_name%\b" > nul

if %errorlevel% equ 0 (
    echo [INFO] Conda environment '%environment_name%' already exists.
    pause
    exit /b 0
)

REM Create new environment
echo [INFO] Creating conda environment '%environment_name%' with Python 3.12...
call conda create -n %environment_name% python=3.12 -y

if %errorlevel% neq 0 (
    echo [ERROR] Conda environment creation failed!
    pause
    exit /b 1
)

echo [SUCCESS] Conda environment '%environment_name%' successfully created.
pause
