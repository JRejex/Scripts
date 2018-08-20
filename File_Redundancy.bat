@echo Training Folder File Backup! (Both Pilots and SOs)
@pause
 
@echo off
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"

set "datestamp=%YYYY%%MM%%DD%"
echo datestamp: "%datestamp%"

mkdir %UserProfile%\Desktop\Digital" "Training" "Folders" "Backup\(Pilots)\%datestamp%
mkdir %UserProfile%\Desktop\Digital" "Training" "Folders" "Backup\(SOs)\%datestamp%
@echo Loading in process, Do not Close Window
robocopy X:\SHAREDDRIVE\PATH\HERE %UserProfile%\Desktop\Digital" "Training" "Folders" "Backup\(Pilots)\%datestamp% /e /np /log+:Restore_Log_Pilots.txt
@echo (Pilots complete)
robocopy X:\SHAREDDRIVE\PATH\HERE %UserProfile%\Desktop\Digital" "Training" "Folders" "Backup\(SOs)\%datestamp% /e /np /log+:Restore_Log_SOs.txt
@echo (SOs complete)
@echo      
color 02
@echo File Copy Complete!
pause
exit
