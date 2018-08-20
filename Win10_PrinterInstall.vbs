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
strMsg = strMsg & "Enter 1 for All Building X KM Printers" & vbCR
strMsg = strMsg & "Enter 2 for Building XX Dell Printer" & vbCR
strMsg = strMsg & "Enter Q or q to Quit" & vbCR
'*************************************************************************

'The While loop that takes your selection from the InputBox and runs the 
'function for the printer you selected.
'*************************************************************************
Do While strFlag = False
inp01 = InputBox(strMsg,"Make your selection")
Select Case inp01
    Case "1"	'All Building X KMPrinters install
        KMPrinter1
	KMPrinter2
	KMPrinter3
	KMPrinter4

    Case "2"	'Launches Building X Dell Printer install
	DellPrinter1	'Launches the DellPrinter1 function	

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

Function KMPrinter1
'MsgBox "Installing the KONICA MINOLTA c353 Series PS(P) driver"',64,strTitle
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

Function KMPrinter2
'MsgBox "Installing the KONICA MINOLTA c353 PS(P) driver",64,strTitle
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

Function KMPrinter3
'MsgBox "Installing the KONICA MINOLTA c252 PS(P) driver",64,strTitle
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

Function KMPrinter4
'MsgBox "Installing the KONICA MINOLTA c252 PS(P) driver",64,strTitle
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

Function DellPrinter1
'MsgBox "Installing the Dell driver",64,strTitle
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
