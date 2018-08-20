$a = Get-Content "\\INPUT\LOCATION\OF\TEXTFILE\WITH\COMPUTERNAMES\RunGpudateRemotely.txt"

foreach ($i in $a)
    {$i + "`n" + "=========================="; Invoke-Command -Computername $i -scriptblock {gpupdate /force}
cmd /c pause}

