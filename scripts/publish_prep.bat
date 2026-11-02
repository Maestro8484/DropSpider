@echo off
rem Regenerate everything a stranger reads, then check the files. Double-click it.
rem   parts table from bom\BOM.csv, photos and video from the drop folder, the build guide page, then check_repo.
cd /d "%~dp0.."
echo === parts (bom\BOM.csv to docs\parts.md and the README)
python tools\make_parts.py
echo.
echo === photos and video (drop folder to media\ and the README)
python tools\make_media.py
echo.
echo === build guide page
python tools\make_build_guide.py
echo.
echo === repo check
python tools\check_repo.py
echo.
echo Changed files, if any (not yet saved to git):
git status --short
echo.
pause
