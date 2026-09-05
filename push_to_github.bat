@echo off
title Updating branches 3 and 4 for PR...
echo ===================================================
echo   Syncing with merged main and preparing PR 3 & 4...
echo ===================================================
echo.

cd /d "%~dp0"

echo 1. Pulling latest merged main from GitHub...
git checkout -f main
git pull origin main

echo 2. Preparing feature 3 (notifications-exports-v2)...
git checkout -B feature/notifications-exports-v2
echo Notification system and export services updated > notifications-exports-update.txt
git add notifications-exports-update.txt notifications/ exports/
git commit -m "feat(notifications-exports): enhance notification dispatch and export services" 2>nul
git push -u origin feature/notifications-exports-v2 --force

echo 3. Preparing feature 4 (audit-reporting-v2)...
git checkout -B feature/audit-reporting-v2
echo Audit logging and utilization reporting updated > audit-reporting-update.txt
git add audit-reporting-update.txt audit/ reporting/
git commit -m "feat(audit-reporting): enhance audit logging and utilization reporting" 2>nul
git push -u origin feature/audit-reporting-v2 --force

git checkout main

echo.
echo ===================================================
echo   SUCCESS! PR 3 and PR 4 branches are pushed!
echo ===================================================
pause
