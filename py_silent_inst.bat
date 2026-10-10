@echo off
setlocal EnableDelayedExpansion

:: === НАСТРОЙКИ ===
set PYTHON_VERSION=3.13.0
set INSTALL_DIR=C:\Python%PYTHON_VERSION%
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

echo [INSTALL] Загрузка Python %PYTHON_VERSION%...
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile 'python_installer.exe'"

if not exist python_installer.exe (
    echo [ERROR] Не удалось скачать установщик. Проверьте интернет-соединение.
    exit /b 1
)

echo [INSTALL] Тихая установка Python в %INSTALL_DIR%...
start /wait "" python_installer.exe ^
    /quiet ^
    InstallAllUsers=0 ^
    TargetDir="%INSTALL_DIR%" ^
    Include_pip=1 ^
    Include_tcltk=1 ^
    PrependPath=1 ^
    AssociateFiles=1 ^
    Shortcuts=0

if %ERRORLEVEL% neq 0 (
    echo [ERROR] Установка завершилась с кодом ошибки %ERRORLEVEL%
    del python_installer.exe
    exit /b 1
)

del python_installer.exe

echo [SUCCESS] Python установлен в %INSTALL_DIR%
echo [INFO] Версия: 
"%INSTALL_DIR%\python.exe" --version
echo [INFO] Pip доступен: 
"%INSTALL_DIR%\Scripts\pip.exe" --version

pause