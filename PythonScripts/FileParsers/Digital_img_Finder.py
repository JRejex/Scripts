'''

Script Purpose: Searching for Digital Images with Python
Script Version: 3.0 September 21th, 2021
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

# Import 3rd Party Modules
#from binascii import hexlify                # hex function
''' importing of any required 3rd party libraries '''
from prettytable import PrettyTable
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


# End of Script Module Importing


# Script Constants

'''
Python does not support constants directly
however, by initializing variables here and
specifying them as UPPER_CASE you can make your
intent known
'''
# Psuedo Constants

SCRIPT_NAME    = "Searching for Digital Images with Python"
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

def DirProcessor(fileDir):
    # 2) Verify that the path provided exists and is a directory
    try: 
        if os.path.isdir(fileDir):
            fileNames = set(os.listdir(fileDir))
            return fileNames
        else: 
            print("Error; Invalid directory path. Try something like 'C:/somedir/somedir'")
    except Exception as err:
        print(err)
    

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
    dirChoice = ( input("\nEnter directory path {Default= ~/Pictures}: ") or ( os.path.expanduser('~').replace('\\', '/') + "/Pictures" ))        # Defaults to users picture directory and replaces \ with /
    dirChoice = dirChoice.replace('"', '').replace("'", '').replace('\\', '/') + "/"                                                 
    tbl = PrettyTable(['File','Ext','Format','Width','Height','Mode'])


# script   
    print("Processing Directory ...\n")
    fileNames = DirProcessor(dirChoice)           
    
    
    print("Processing Files ...\n")
    for file in fileNames:                          # 3) Iterate through each file in that directory and examine it using PIL.
        filePath = dirChoice + file
        #print("\nChecking file...: ",file)
        if os.path.isdir(filePath):
            print("This is a Directory : ", filePath)
        try:
            with Image.open(filePath) as im:
                imFormat = im.format
                imType = im.mode
                imWidth = im.width
                imHeight = im.height
                imExt = ("." + im.format.lower() )
            
            tbl.add_row( [ filePath, imExt, imFormat, imWidth, imHeight, imType] )

        except Exception as err:
            print("Exception PIL.Image.open() Failed: ", filePath, str(err))
        
    tbl.align = "l"     
    print(tbl)              # 4) Generate a prettytable report of your search results
    print("\nScript End")
  
# End of Script Main
