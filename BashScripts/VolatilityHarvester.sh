#!/bin/bash
while getopts f:o:h flag
do
    case "${flag}" in
        f) memfile=${OPTARG};;
        o) outfile=${OPTARG};;
        h) hostname=${OPTARG};;

    esac
done
echo "Memory Dump: $memfile";
echo "Out File: $outfile";
echo "Hostname: $hostname";

#memfile=/forensic_memdumps/EndpointServer1.dmp
#outfile=/forensic_cases/EndpointServer1/Reports/
#hostname=EndpointServer1

sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.info.Info >> $outfile/$hostname.info.txt
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.malfind.Malfind >> $outfile/$hostname.malfind.txt
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.cmdline.CmdLine >> $outfile/$hostname.cmdline.txt
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.netscan.NetScan >> $outfile/$hostname.netscan.txt
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.pslist.PsList >> $outfile/$hostname.pslist.txt
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.windows.registry.userassist.UserAssist >> $outfile/$hostname.userassist.txt
 #Scans for network objects present in a particular windows memory image
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.netscan.NetScan >> $outfile/$hostname.netscan.txt
sudo /forensic_programs/volatility3/vol.py -vv -f $memfile windows.netstat.NetStat >> $outfile/$hostname.netstat.txt
