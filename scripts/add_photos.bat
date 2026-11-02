@echo off
rem Photos and clips from the drop folder into the README. Double-click it.
rem Drop folder: C:\Users\SuperMaster\Documents\_Projects\Projects-Media-Photos-Docs\DropSpider\
rem Captions: media\captions.txt (edit the words, run this again).
cd /d "%~dp0.."
python tools\make_media.py %*
echo.
echo Changed files, if any (not yet saved to git):
git status --short -- README.md media
echo.
pause
