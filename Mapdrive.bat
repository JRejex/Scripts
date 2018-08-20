@ECHO OFF

rem First delete any share mapped to N:
net use /del N:

rem Now map the new N: drive
ECHO Mapping N...
net use n: \\Shareddrive\Path\HERE
