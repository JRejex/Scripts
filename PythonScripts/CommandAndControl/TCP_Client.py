'''

Script Purpose: Create TCP Client
Script Version: 3.0 October 12th, 2021
Script Author: James Rejouis

Script Revision History:

'''

# Script Module Importing

# Python Standard Library Modules
from __future__ import print_function       # print function
from datetime import datetime         

import hashlib
import os           # Operating/Filesystem Module
import time         # Basic Time Module
import sys
import socket      # Import Python Standard Socket Library
import re
import requests    # Python Standard Library for url requests
import logging

# Import 3rd Party Modules
from binascii import hexlify    # hex function
''' importing of any required 3rd party libraries '''
#from prettytable import PrettyTable
#from bs4 import BeautifulSoup           # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4


# End of Script Module Importing


# Script Constants

'''
Python does not support constants directly
however, by initializing variables here and
specifying them as UPPER_CASE you can make your
intent known
'''
# Psuedo Constants

SCRIPT_NAME    = "Script: 10 - Create TCP Client"
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

'''
Simple Client Data Transfer in the clear

In this example a connection is made between a client
and simple server running on the same machine over a 
pre-defined and agreed upon port.

This client application will transfer a simple text message
to the server.  The server will will simply display the contents  
of the message.

'''
# Setup Logging
print("Server Starting up\n")
OUTPUT_SAVE = "./OUTPUT/"  # Directory to store log output
        
# Create the directory if necessary
if not os.path.exists(OUTPUT_SAVE):
    os.makedirs(OUTPUT_SAVE)    
    
logName = os.path.basename("TCP-Clientlog.txt")
logOutputPath = OUTPUT_SAVE+logName
logging.basicConfig(filename=logOutputPath,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


wordList = ("How_1", "Now_2", "Brown_3", "Cow_4", "The_5", "Fox_6", "Jumped_7", "Over_8", "Another_9", "Fence_10")
print("Client Application")
print("Establish a connection to a server")
print("Available on the same host using PORT 5555")

PORT = 5555          # Port Number of Server
    
try:
    # Create a Socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get my local host address
    localHost = socket.gethostname()
    
    print("\nAttempt Connection to: ", localHost, PORT)
    
    clientSocket.connect((localHost, PORT))
    
    # Sending message if there was a connection
    print("Socket Connected ...")
    for word in wordList:
        print("\nSending Message: ", word)
        clientSocket.send(word.encode())
        logging.info("Sent message: %s", word)
        # Accept response from Server
        
        print('Waiting for Server Response')   
        buffer = clientSocket.recv(2048)        # Wait for Data
        logging.info("Response: %s", buffer.decode())
        print("Response: ", buffer.decode())      
        
except Exception as err:
    sys.exit(err)

            

  
# End of Script Main



