'''

Script Purpose: Extract e-mail address and urls from the memory dump provided
Script Version: 3.0 September 28th, 2021
Script Author: James Rejouis

Script Revision History:

'''

# Script Module Importing

# Python Standard Library Modules
from __future__ import print_function       # print function
from datetime import datetime         

#import hashlib
import os           # Operating/Filesystem Module
import time         # Basic Time Module
import sys
import re

# Import 3rd Party Modules
#from binascii import hexlify                # hex function
''' importing of any required 3rd party libraries '''
from prettytable import PrettyTable
from binascii import hexlify


# End of Script Module Importing


# Script Constants

'''
Python does not support constants directly
however, by initializing variables here and
specifying them as UPPER_CASE you can make your
intent known
'''
# Psuedo Constants

SCRIPT_NAME    = "Extract e-mail address and urls from the memory dump provided"
SCRIPT_VERSION = "Version 3.0"
SCRIPT_AUTHOR  = "Author: James Rejouis"

# End of Script Constants


# Script Functions
'''
If you script will contain functions then insert them
here, before the execution of the main script.  This
will ensure that the functions will be callable from
anywhere in your script
'''


def GetTime(timeStyle = "UTC"):
    '''
    Function: GetTime()
    Input timeStyle either UTC or LOCAL
          UTC is the default if not argument is provided
    Returns a string containing the current time
    
    Description:
    Script will use the local system clock, time, date and timezone
    to calcuate the current time.  Thus you should sync your system
    clock before using this script

    '''
    epochValue = time.time()
    
    if timeStyle == 'UTC':
        utcTime = time.gmtime(epochValue)
        timeString = time.asctime(utcTime)
        return 'UTC Time: '+ timeString
    elif timeStyle == 'LOCAL':
        localTime = time.localtime(epochValue)
        timeString = time.asctime(localTime)  
        return 'Local Time: '+ timeString
    else:
        return "Invalid TimeStyle Specified"
    
# End GetTime Function       


# End of Script Functions

# Script Classes
'''
If you script will contain classes then insert them
here, before the execution of the main script.  This
will ensure that the functions will be accessible from
anywhere in your script
'''

       
        
# End of Script Classes


# Main Script Starts Here

if __name__ == '__main__':
    
    # Print Basic Script Information
    
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()
    
    localTime = GetTime('LOCAL')
    print("Local Time:   ", localTime)

    utcTime = GetTime('UTC')
    print("UTC Time:     ", utcTime)    
    
    invalidTime = GetTime('BAD')
    print("Invalid Time: ", invalidTime)    
    
    
# 1) Prompts the user for a directory path to search
    enabledPrompt = 0       # Change value to 1 to enable prompt
    if enabledPrompt:
        fileChoice = ( input("\nEnter filepath: ") )        
        fileChoice = fileChoice.replace('"', '').replace("'", '').replace('\\', '/')                                               
    else:
        fileChoice = "D:\Mem_testfiles\memdump.bin"     # 1) Copy the memory dump to the virtual desktop environment persistent storage area.
        
    emailTbl = PrettyTable(['Possible Emails'])
    urlTbl = PrettyTable(['Possible Urls'])
    
    # File Chunk Size
    CHUNK_SIZE = 1024
    
    # regular expressions
    ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')  
    uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')
    
    
    # Create empty lists
    emailList = []
    urlList = []
# script    
    print("Processing File ...\n", fileChoice)
    if os.path.isdir(fileChoice):                       # Check if file choice is actually a directory
        print("This is a Directory : ", filePath)
    elif os.path.isfile(fileChoice):                        # Check if file choice is a file
        try:
            with open('test.bin', 'rb') as binaryFile:
                while True:
                    chunk = binaryFile.read(CHUNK_SIZE)
                    if chunk:
                        emails = ePatt.findall(chunk)           # Find possible emails with Regex
                        for eachEmail in emails:
                            emailList.append(eachEmail)         # Append found emails to list
                    if chunk:
                        urls = uPatt.findall(chunk)             # Find possible urls with Regex
                        for eachUrl in urls:
                            urlList.append(eachUrl)             # Append found urls to list
                    else:
                        break
                                           
            for possibleEmail in emailList:
                decodedEmail = possibleEmail.decode('ascii')        
                emailTbl.add_row( [ decodedEmail ] )
            for possibleUrl in urlList:
                decodedUrl = possibleUrl.decode('ascii')          
                urlTbl.add_row( [ decodedUrl ] )

        except Exception as err:
            print("Error: ", filePath, str(err))
        
    emailTbl.align = "l"
    urlTbl.align = "l"
    print(emailTbl)                          # Print possible Emails
    print(urlTbl)                         # Print possible Urls
    print("\nScript End")
  
# End of Script Main
