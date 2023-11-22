@echo off 
set /p message="Enter your commit message: "
git pull
git add . 
git commit -m "%message%"
git push origin main