Old Profile Copy
@echo off
echo Press Any Key to Load old Profile...
@pause
@start /min Hawks.bat
@echo Loading Profile..
Timeout /t 2
robocopy /pf /mir /r:1 /w:5 /XO /XX D:\Users\%username% %userprofile%\ /xf *.TMP /xD "D:\Users\%username%\Appdata" "D:\Users\%username%\Local Settings"
robocopy /pf /mir /r:1 /w:5 /XO /XX E:\Users\%username% %userprofile%\ /xf *.TMP /xD "E:\Users\%username%\Appdata" "E:\Users\%username%\Local Settings"
robocopy /pf /mir /r:1 /w:5 /XO /XX F:\Users\%username% %userprofile%\ /xf *.TMP /xD "F:\Users\%username%\Appdata" "F:\Users\%username%\Local Settings"
@echo Copying Outlook Appdata

robocopy /pf /mir /r:1 /w:5 /XO /XX D:\Users\%username%\Appdata\Local\Microsoft\Outlook "%userprofile%\Appdata\Microsoft\Outlook\" /xf *.TMP
robocopy /pf /mir /r:1 /w:5 /XO /XX E:\Users\%username%\Appdata\Local\Microsoft\Outlook "%userprofile%\Appdata\Microsoft\Outlook\" /xf *.TMP
robocopy /pf /mir /r:1 /w:5 /XO /XX F:\Users\%username%\Appdata\Local\Microsoft\Outlook "%userprofile%\Appdata\Microsoft\Outlook\" /xf *.TMP

robocopy /pf /mir /r:1 /w:5 /XO /XX D:\Users\%username%\%Appdata%\Microsoft\Outlook "%userprofile%\Appdata\Roaming\Microsoft\Outlook\" /xf *.TMP
robocopy /pf /mir /r:1 /w:5 /XO /XX E:\Users\%username%\%Appdata%\Microsoft\Outlook "%userprofile%\Appdata\Roaming\Microsoft\Outlook\" /xf *.TMP
robocopy /pf /mir /r:1 /w:5 /XO /XX F:\Users\%username%\%Appdata%\Microsoft\Outlook "%userprofile%\Appdata\Roaming\Microsoft\Outlook\" /xf *.TMP

robocopy /pf /mir /r:1 /w:5 /XO /XX D:\Users\%username%\AppData\Roaming\Microsoft\Signatures "%userprofile%\Appdata\Roaming\Microsoft\Signatures\" /xf *.TMP
robocopy /pf /mir /r:1 /w:5 /XO /XX E:\Users\%username%\AppData\Roaming\Microsoft\Signatures "%userprofile%\Appdata\Roaming\Microsoft\Signatures\" /xf *.TMP
robocopy /pf /mir /r:1 /w:5 /XO /XX F:\Users\%username%\AppData\Roaming\Microsoft\Signatures "%userprofile%\Appdata\Roaming\Microsoft\Signatures\" /xf *.TMP

@color 02
@cls
@echo Profile fully loaded!
pause
