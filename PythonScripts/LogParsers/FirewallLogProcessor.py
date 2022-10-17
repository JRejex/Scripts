'''

Script Purpose: Parsing a firewall log file
Script Version: 3.0 September 6th, 2021
Script Author: James Rejouis

Script Revision History:

'''

# Script Module Importing

# Python Standard Library Modules
from __future__ import print_function       # print function

import os           # Operating/Filesystem Module
import time         # Basic Time Module

# Import 3rd Party Modules

''' importing of any required 3rd party libraries '''

# End of Script Module Importing


# Script Constants

'''
Python does not support constants directly
however, by initializing variables here and
specifying them as UPPER_CASE you can make your
intent known
'''
# Psuedo Constants

SCRIPT_NAME    = "Parsing a firewall log file"
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
    
    '''
    File Processing
    '''
    
    #import os
    
    uniqueWorms = set()
    #tbl = prettyTable(['
    splitLines = []         # initialize array
    setofWorms = set()         # initialize set

    with open("redhat.txt", 'r') as logFile:        # Open firewall log
        for eachLine in logFile:
            ''' your code starts here '''
            splitLines += eachLine.split()          # Split eachline into individual fields
    for field in splitLines:
        if 'Worm' in field:             
            setofWorms.add(field)                   # Add worm names to set
    setofWorms = sorted(setofWorms)                 # Sort
    for uniqueWorm in setofWorms:
        print(uniqueWorm)                           # iterate and print unique worm names


# End of Script Main
