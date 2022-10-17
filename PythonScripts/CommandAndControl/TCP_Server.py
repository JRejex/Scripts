'''

Script Purpose: Create a TCP Server
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
import socket       # Import Python Standard Socket Library
import re
import requests    # Python Standard Library for url requests
import ipaddress
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

SCRIPT_NAME    = "Script: Create a TCP Server"
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
Simple Server to receive data from client

In this example a connection is made between a client
and simple server running on the same machine over a 
pre-defined and agreed upon port.

This server application will wait for a connection request
over a pre-defined port.

Once a connection is established the server will receive data sent 
over the port and display the contents of the recevied data.

'''
# Setup Logging
print("Server Starting up\n")
OUTPUT_SAVE = "./OUTPUT/"  # Directory to store log output
        
# Create the directory if necessary
if not os.path.exists(OUTPUT_SAVE):
    os.makedirs(OUTPUT_SAVE)    
    
logName = os.path.basename("TCP-Serverlog.txt")
logOutputPath = OUTPUT_SAVE+logName
logging.basicConfig(filename=logOutputPath,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
 
try: 
    
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Create Socket for listening
    
    localHost = socket.gethostname()    # Get my local host address
    
    localPort = 5555                    # Specify a local Port 
                                        # to accept connections on
    
    serverSocket.bind((localHost, localPort))  # Bind mySocket to localHost
    
    serverSocket.listen(1)              # Listen for connections

    print('\nWaiting for Connection Request')    
    
    ''' Wait for a connection request
        Note this is a synchronous Call meaning the program will halt until
        a connection is received.  Once a connection is received
        we will accept the connection and obtain the 
        ipAddress of the connecting computer
    '''
    while True:
        conn, client = serverSocket.accept()
        logging.info("Connection Attempted: %s:%s", str(client[0]), str(client[1]))
        print("Connection Attempted from Client: ", client)
        if ipaddress.IPv4Address(client[0]) in ipaddress.IPv4Network('10.139.0.0/20'):   # Check if client is operating on same local IP range as Server
            logging.info("Connection Allowed")
            print("Connection Allowed")        
            while True:
                    buffer = conn.recv(2048)  # Wait for Data
                    if not buffer:       # If no message is sent break and await new connection
                        break
                    logging.info("Message Received: %s", str(buffer.decode())) 
                    print("Message Received: ", str(buffer.decode()))   # Message received
                    
                    # Create md5hash of message
                    responseBuffer = hashlib.md5(buffer)
                    responseHash = responseBuffer.hexdigest().encode()
                    
                    # Respond back to client with md5hash
                    conn.send(responseHash)
                    logging.info("Sent MD5hash: %s to Client: %s", str(responseHash.decode()), str(client[0]))
                    print("Sent MD5hash {",responseHash.decode(),"} to client :", client)
        else:
            # Drop Connection
            conn.close()
            logging.info("Dropped Connection, Client %s not on local IP Range", str(client[0]))
            print("Dropped Connection, Client {",client[0],"} is not on the same local IP range")
            print("Awaiting new connection...")

        
except Exception as err:
    sys.exit(str(err))


  
# End of Script Main
