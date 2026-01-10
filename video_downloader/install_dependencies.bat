@echo off
echo ================================================
echo YouTube Downloader Pro - Dependency Installer
echo ================================================
echo.
echo Installing required Python packages...
echo.

python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Installing packages...
pip install --upgrade pip
pip install customtkinter>=5.2.0
pip install yt-dlp>=2023.10.13
pip install packaging
pip install Pillow>=9.0.0
pip install pyinstaller>=5.0

echo.
echo ================================================
echo Installation complete!
echo ================================================
echo.
echo You can now run: python youtube_downloader.py
echo.
pause