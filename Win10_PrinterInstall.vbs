On Error Resume Next

'START Declaring Variables
'*************************************************************************
Dim strMsg,inp01,strTitle,strFlag
Dim oShell, sPrntUtilityPath, sDrvrName, sDrvrFile, sPrntrIP, sPrntrName, sDrvrLocation
'*************************************************************************

'SETUP OBJECTS
'*************************************************************************
Set oShell = WScript.CreateObject("Wscript.Shell")
'*************************************************************************

'Set default value for Variables
'*************************************************************************
strTitle = "Answer Box"
strFlag = False
sPrntUtilityPath = "C:\Windows\System32\Printing_Admin_Scripts\en-US\"
strPrndrvr = "C:\Windows\System32\Printing_Admin_Scripts\en-US\Prndrvr.vbs"
strPrnport = "C:\Windows\System32\Printing_Admin_Scripts\en-US\prnport.vbs"
strPrnmngr = "C:\Windows\System32\Printing_Admin_Scripts\en-US\prnmngr.vbs"
'*************************************************************************

'Set text and formatting for Input Box
'*************************************************************************
strMsg = strMsg & "Enter 1 for All Building XX Printers" & vbCR
strMsg = strMsg & "Enter 2 for Building XX Dell Printer" & vbCR
strMsg = strMsg & "Enter Q or q to Quit" & vbCR
'*************************************************************************

'The While loop that takes your selection from the InputBox and runs the 
'function for the printer you selected.
'*************************************************************************
Do While strFlag = False
inp01 = InputBox(strMsg,"Make your selection")
Select Case inp01
    Case "1"	'All Building 1200 NIPR Printers
        KM64Rm233
	KM64Rm101
	KM64Rm102
	KM64Rm207

    Case "2"	'Launches Building XX Dell Printer install
	Dell1204	'Launches the Dell1204 function	

    Case "Q"
        MsgBox "Goodbye",64,strTitle
	strFlag = True  'Exits the loop
    Case "q"
        MsgBox "Goodbye",64,strTitle
	strFlag = True  'Exits the loop
    Case Else
        MsgBox "You made an incorrect selection!",64,strTitle
End Select
Loop

Wscript.Quit   'Exits the script

Function Sample
'MsgBox "Installing the Sample driver",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "Sample PCL6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "XXX.XX.XXX.XXX"
sPrntrName= "Sample Printer"
'*************************************************************************
Install  ' Launches the Install function
End Function

Function KM64Rm233
'MsgBox "Installing the Rm233 KONICA MINOLTA c353 Series PS(P) driver"',64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "KONICA MINOLTA PS Color Laser Class Driver" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "XXX.XX.XXX.XXX" 
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function KM64Rm101
'MsgBox "Installing the Rm101 KONICA MINOLTA c353 PS(P) driver",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "KONICA MINOLTA PS Color Laser Class Driver" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function KM64Rm102
'MsgBox "Installing the Rm102 KONICA MINOLTA c252 PS(P) driver",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "KONICA MINOLTA PS Color Laser Class Driver" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= "Mission Planning Rm102 Konica Printer Duplex"
'*************************************************************************
Install  ' Launches the Install function
End Function

Function KM64Rm207
'MsgBox "Installing the Rm207 KONICA MINOLTA c252 PS(P) driver",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "KONICA MINOLTA PS Color Laser Class Driver" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= "UDM Rm207 Konica Printer Duplex"
'*************************************************************************
Install  ' Launches the Install function
End Function

Function Dell1204
'MsgBox "Installing the Building 1204 Dell driver",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "Dell 5130cdn PCL6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function DellMission
'MsgBox "Installing the Building 1200 Mission Planning Color Printer",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "Dell 5130cdn Color Laser PCL6"
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function DellIT
'MsgBox "Installing the Building 1200 IT Color Printer",64,strTitle
'Sets values for the Variables
'*************************************************************************
sDrvrName = "Dell 5130cdn Color Laser PCL6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function HP1RSIA
'Sets values for the Variables
'*************************************************************************
sDrvrName = "HP Universal Printing PCL 6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function HP1RSCBT
'Sets values for the Variables
'*************************************************************************
sDrvrName = "HP Universal Printing PCL 6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function HP1RSSched
'Sets values for the Variables
'*************************************************************************
sDrvrName = "HP Universal Printing PCL 6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function

Function HP1RSDuty
'Sets values for the Variables
'*************************************************************************
sDrvrName = "HP Universal Printing PCL 6" 
sDrvrLocation = ""
sDrvrFile = ""
sPrntrIP = "X.X.X.X"
sPrntrName= ""
'*************************************************************************
Install  ' Launches the Install function
End Function




Function Install   
'******************* Installs the printer driver
strRunCmd = "cscript " & strPrndrvr & " -a -m " & sDrvrName & " -v 3 -e Windows x64 -h " & sDrvrLocation & " -i " & sDrvrFile
oShell.Run strRunCmd
'*************************************************************************

'******************* Creates the printer port
strRunCmd = "cscript " & strPrnport & " -a -r IP_" & sPrntrIP & " -h " & sPrntrIP & " -o RAW -n 9100"
oShell.Run strRunCmd
'*************************************************************************

'******************* Installs the printer
strRunCmd = "cscript " & strPrnmngr & " -a -p " & AddQuotes(sPrntrName) & " -m " & AddQuotes(sDrvrName) & " -r IP_" & sPrntrIP
oShell.Run strRunCmd
'*************************************************************************
MsgBox "Done Installing"
End Function


Function AddQuotes (strInput)
' This function only adds "quotes" around the string provided
	AddQuotes = Chr(34) & strInput & Chr(34)
End Function
