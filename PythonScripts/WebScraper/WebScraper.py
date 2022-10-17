'''

Script Purpose: Process a target website and extract key information and suspicious content
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
import requests    # Python Standard Library for url requests

# Import 3rd Party Modules
''' importing of any required 3rd party libraries '''
#from prettytable import PrettyTable
#from binascii import hexlify
from bs4 import BeautifulSoup           # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4


# End of Script Module Importing


# Script Constants

'''
Python does not support constants directly
however, by initializing variables here and
specifying them as UPPER_CASE you can make your
intent known
'''
# Psuedo Constants

SCRIPT_NAME    = "Script: Process a target website and extract key information and suspicious content"
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

url = 'https://casl.website/login'
base = 'https://casl.website'
OUTPUT_SAVE = "./OUTPUT/"  # Directory to store output
        
# Create the directory if necessary
if not os.path.exists(OUTPUT_SAVE):
    os.makedirs(OUTPUT_SAVE)
    
page = requests.get(url)       # retrieve a page from your favorite website
soup = BeautifulSoup(page.text, 'html.parser')  # convert the page into soup
regGrab = re.compile('\>.*\<')      # grab clean title output



# Scrape page-title
pageTitles = soup.findAll('h1')  # Find the tags
for eachTitle in pageTitles:      # Process and display each title
    try:
        title = (str(regGrab.findall( str(eachTitle) )))[3:-3]
    except Exception as err:
        print(eachTitle, err)
        continue        

# Save the title
titleName = os.path.basename("page-title.txt")
titleOutputPath = OUTPUT_SAVE+titleName
print("Processing page-title:", title , titleOutputPath, end="")
with open(titleOutputPath, 'w') as outFile:
    outFile.write(title)
print("  >> Saved page-title:", titleOutputPath)

# Scrape page-links URLs
pageLinks = soup.findAll('link')  # Find the page-link tags
pageLinks2 = soup.findAll('a') 
uniqueLinks = set()
for eachLink in pageLinks:      # Process and display each link
    try:
        linkURL = eachLink['href']
        if linkURL[0:4] != 'http':       # If URL path is relative
            eachURL = base+linkURL         # try prepending the base url
            uniqueLinks.add(eachURL)
            #print(eachURL)
    except Exception as err:
        print(err)
        continue        
for eachLink in pageLinks2:      # Process and display each link
    try:
        linkURL = eachLink['href']
        if linkURL[0:4] != 'http':       # If URL path is relative
            eachURL = base+linkURL         # try prepending the base url
            uniqueLinks.add(eachURL)
            #print(eachURL)
    except Exception as err:
        #print(err)
        continue        
    
# Save the links
linkName = os.path.basename("page-links.txt")
linkOutputPath = OUTPUT_SAVE+linkName
with open(linkOutputPath, 'w') as outFile:
    for uniqueURL in uniqueLinks:
        print("Processing page-link:", uniqueURL, end="")  
        outFile.write(uniqueURL + "\n")
        print("  >> Saved page-link: ", linkOutputPath)
        
# Scrape images found on the page            
print("\nExtracting Images from: ", url)
print("Please Wait...")
images = soup.findAll('img')  # Find the image tags
for eachImage in images:      # Process and display each image
    try:
        imgURL = eachImage['src']
        print("Processing Image:", imgURL, end="")
        if imgURL[0:4] != 'http':       # If URL path is relative
            imgURL = base+imgURL         # try prepending the base url

        response = requests.get(imgURL)                 # Get the image from the URL
        imageName = os.path.basename(imgURL)
        
        imgOutputPath = OUTPUT_SAVE+imageName
        
        with open(imgOutputPath, 'wb') as outFile:
            outFile.write(response.content)
            
        # Save the image
        print("  >> Saved Image:", imgOutputPath)
    except Exception as err:
        print(imgURL, err)
        continue    

print("\nOutput Document File Location: ", os.getcwd() + "\OUTPUT")
print("\nScript End")
  
# End of Script Main



