'''

Script Purpose: File Processing Object
Script Version: 3.0 September 12th, 2021
Script Author: James Rejouis

Script Revision History:

'''

# Script Module Importing

# Python Standard Library Modules
from __future__ import print_function       # print function
         

import hashlib
import os           # Operating/Filesystem Module
import time         # Basic Time Module
import sys

# Import 3rd Party Modules
from binascii import hexlify                # hex function
''' importing of any required 3rd party libraries '''
from prettytable import PrettyTable



# End of Script Module Importing


# Script Constants

'''
Python does not support constants directly
however, by initializing variables here and
specifying them as UPPER_CASE you can make your
intent known
'''
# Psuedo Constants

SCRIPT_NAME    = "File Processing Object"
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
    # Determine if directory exists/list
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
class FileProcessor:
    def __init__(self):
        ''' Create object variables and Constants '''
        self.filePath = ''
        self.fileSize = ''
        self.modifiedTime = ''
        self.createTime = ''
        self.fileHash = ''
        self.hashType = ''
        self.VALID_HASH_TYPES = ['MD5', 'SHA1', 'SHA256', 'SHA384', 'SHA512']   # Added SHA384
        self.lastErr = ''        
        
    def SetFilePath(self, filePath):
        ''' Set the file path if valid 
            Obtain file size and timestamps
            return True if valid and set the self.filePath object variable
        '''
        if os.path.isfile(filePath):                # i) verify the file exists
            if os.access(filePath, os.R_OK):
                self.filePath = filePath            # ii) Extract key file system metadata from the file
                stats = os.stat(self.filePath)
                self.fileSize = stats.st_size
                self.modifiedTime = time.ctime(stats.st_mtime)
                self.createTime       = time.ctime(stats.st_ctime)
                self.lastErr = ''
                #Added headers
                self.hexStr = ''
                self.header = ''
                #Added File Owner & File Mode
                self.fileOwner = os.stat(self.filePath).st_uid
                self.fileMode = os.stat(self.filePath).st_mode
                
                return True
            else:
                self.filePath = ''
                self.lastErr = 'Invalid File Path'
                return False
            
    def SetHashType(self, hashType):
        # Set the Hash Type verify it is supported
        if hashType in self.VALID_HASH_TYPES:
            self.hashType = hashType    
            self.lastErr = ''
            return True
        else:
            self.hashType = ''
            self.lastErr = 'Invalid Hash Type'
            return False

    def __InitializeHashObject(self):

        if self.hashType == 'MD5':
            self.hashObj = hashlib.md5()
        elif self.hashType == 'SHA1':
            self.hashObj = hashlib.sha1()
        elif self.hashType == 'SHA256':
            self.hashObj = hashlib.sha256()
        elif self.hashType == 'SHA384':             # Added SHA384 as an option
            self.hashObj = hashlib.sha384()              
        elif self.hashType == 'SHA512':
            self.hashObj = hashlib.sha512()  
        else:
            self.hashObj = hashlib.md5()

    def HashFile(self):
        ''' Using the object variables hash the file '''
        try:
            if self.hashType:
                self.__InitializeHashObject()
            else:
                self.lastErr = 'Hash Type not Set'
                return False
            with open(self.filePath, 'rb') as fileToHash:
                fileContents = fileToHash.read()
                self.hashObj.update(fileContents)
                self.fileHash = self.hashObj.hexdigest()
                self.lastErr = ''
                return True
        except Exception as err:
            self.lastErr = str(err)
            return False
            
    def GetFileHeader(self, filePath):                      
       # i) Extract the first 20 bytes of the header and store them in an instance attribute
        with open(filePath, 'rb') as binFile:
            self.header = binFile.read(20)
            self.hexStr = hexlify(self.header)   

    def PrintFileDetails(self):
        #i) Print the metadata
        
        print("Path:               ", self.filePath)
        print("File Size:          ", '{:,}'.format(self.fileSize), "Bytes")
        print("File Created Time:  ", self.createTime)
        print("File Modified Time: ", self.modifiedTime)
        print("File Owner UID: ", self.fileOwner)
        print("File Mode: ", self.fileMode)
        #ii) Print the hex representation of the header    
        print("Hex Header:         ", self.hexStr)
        # Added Hashing as a bonus feature
        print("Hash Type:          ", self.hashType)
        print("Hash Value:         ", self.fileHash)

 
        ''' #To add pretty table comment above print statements, and uncomment this snippet. Also uncomment tbl print statement at the end of script
        tbl.add_row( [ self.filePath, '{:,}'.format(self.fileSize), self.createTime, self.modifiedTime, self.hashType, self.fileHash, self.hexStr ] )
        tbl.align = "l" 
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
    
    
# User input
    dirChoice = ( input("\nEnter directory path {Default CWD}: ") or os.getcwd() ).replace('\\', '/')        # Defaults to cwd and replace \ with /
    dirChoice = dirChoice.replace('"', '').replace("'", '') + "/"                                                 # Added / for compatibility
    hashChoice = str( input( "Enter hash algorithm {Default SHA384}: ") or 'SHA384' )       
    #tbl = PrettyTable(['FilePath','Size','CreatedTime','ModifiedTime','HashType','HashValue','Hexheader'])
    #fileName = 'C:/Users/Administrator/Desktop/scripts/redhat.txt'
    #dirChoice = 'C:/Users/Administrator/Desktop/scripts/'
    #hashChoice = 'SHA384'
# script   
    obj = FileProcessor()
    print("Processing Directory ...\n")
    fileNames = DirProcessor(dirChoice)           # using the os.listdir() method extract the filenames from the directory path
    
    
    print("Processing Files ...\n")
    for file in fileNames:                          # Loop through each filename and instantiate and object using the FileProcessor Class
        filePath = dirChoice + file
        print("\nChecking file...: ",file)
        if obj.SetFilePath(filePath):                   # Using the object
            
            if obj.SetHashType(hashChoice):
                if obj.HashFile():
                    obj.hashType
                    obj.fileHash
                else:
                    print("Hashing Failed: ", obj.lastErr)
            else:
                print("Failed to Set HashType: ", obj.lastErr)  
                
            obj.GetFileHeader(filePath)                     # i) invoke the GetFileHeader Method
            obj.PrintFileDetails()                          # ii) invoke the PrintFileDetails Method   
            
        elif os.path.isdir(filePath):
            print("This is a Directory : ", filePath)
        else:
            print("File Name Err: ", obj.lastErr)
    #print(tbl) 
    print("\nScript End")
  
# End of Script Main
