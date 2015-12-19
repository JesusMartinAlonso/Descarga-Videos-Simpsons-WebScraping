@echo off

if not exist you-get.exe (
   cls
   echo you-get.exe could not be found.
   goto:error
)

set PATH=%~dp0\;%PATH%
set PATH=%~dp0\deps\ffmpeg\bin;%PATH%
set PATH=%~dp0\deps\rtmpdump;%PATH%

cls
you-get --version
echo.
prompt $g
cmd /q /k
goto:eof

:error
echo.
pause
