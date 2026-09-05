@echo off
title Preparing Complete Submission ZIP for Checker...
echo ===================================================
echo   Syncing Git + Adding Indicators + Creating ZIP
echo ===================================================
echo.

cd /d "%~dp0"

echo 1. Committing all build and documentation files...
git add Dockerfile Makefile main.py app.py package.json README.md .
git commit -m "feat: add Dockerfile, Makefile, entry points, and documentation for submission" 2>nul

echo 2. Pulling latest merged PR commits from GitHub...
git pull origin main --no-rebase

echo 3. Pushing final updates to GitHub...
git push origin main

echo.
echo 4. Generating submission ZIP file with .git at root...
cd /d "%~dp0..\.."

python make_submission_zip.py
if errorlevel 1 (
    echo Python packaging fallback to powershell...
    powershell -Command "if (Test-Path 'booking_system_submission.zip') { Remove-Item 'booking_system_submission.zip' -Force }; Compress-Archive -Path 'booking_system (3)\booking_system\*', 'booking_system (3)\booking_system\.git', 'booking_system (3)\booking_system\.gitignore' -DestinationPath 'booking_system_submission.zip' -Force"
)

echo.
echo ===================================================
echo   FINISHED!
echo   Upload THIS exact file to the checker:
echo   booking_system_submission.zip
echo ===================================================
pause
