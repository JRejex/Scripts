'''

Script Purpose: Data Frame parsing with Pandas
Script Version: 1.0 September 2022
Script Author:  James Rejouis

Script Revision History:
Version 1.0 September 2022 Initial Version
'''

# Standard Library Imports
    
# 3rd Party Library Imports
print("Please wait, importing libraries")
import pandas as pd        # import Pandas 3rd party library
import numpy as np     # import numpy 3rd party library

# Main Script Starts Here
if __name__ == '__main__':

    '''
    Creating a Panda Dataframe from a JSON File    
    '''
    print("Assignment 2 - STARTER SCRIPT")
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)

    # Create a Panda Dataframe from a JSON File
    df1 = pd.read_csv(r'./ipObservations.csv')  # 1) Create a Panda DataFrame from the ipObservations.csv.   
    print(df1.head(3))
    print("Removing IPv6 rows from Dataframe...", end="")
    df2 = df1.loc[df1["FRAME-TYPE"] != "IPV6" ] # 2) Remove any rows that contain a Frame Type of "IPV6"
    print("Done.")
    #print(df2.head(40))
    print("Assigning Numeric Translations...")
    numericTranslations = ['IPV4=1','ARP=2','TCP=1','UDP=2','BROADCAST=3','LOCAL=1','MULTICAST=2','RESERVED=3','United States=4','France=5','Argentina=6','Japan=7','Ireland=8','Russian Federation=9','United Kingdom=10','Netherlands=11','EPH=65536','NA=0']
    print(numericTranslations)
    df3 = df2 # 3) For the columns SRC-PORT, DST-PORT, FRAME-TYPE, PROTOCOL, SRC-COUNTRY, and DST-COUNTRY, you will replace the string data with a numeric value.  i.e. IPV4 = 1, TCP=1, UPD =2 and so on.  You will create the numeric translation as you see fit.
    
    # FRAME-TYPE Numeric Translations
    df3 = df3.replace({'IPV4': 1})
    df3 = df3.replace({'ARP': 2})
    
    # PROTOCOL Numeric Translations
    df3 = df3.replace({'TCP': 1})
    df3 = df3.replace({'UDP': 2})
    df3 = df3.replace({'BROADCAST': 3})
    
    # SRC-COUNTRY/DST-COUNTRY Numeric Translations
    df3 = df3.replace({'LOCAL': 1})
    df3 = df3.replace({'MULTICAST': 2})
    df3 = df3.replace({'RESERVED': 3})
    df3 = df3.replace({'United States': 4})
    df3 = df3.replace({'France': 5})
    df3 = df3.replace({'Argentina': 6})
    df3 = df3.replace({'Japan': 7})
    df3 = df3.replace({'Ireland': 8})
    df3 = df3.replace({'Russian Federation': 9})
    df3 = df3.replace({'United Kingdom': 10})
    df3 = df3.replace({'Netherlands': 11})
    
    #SRC-PORT/DST-PORT Numeric Translations
    df3 = df3.replace({'EPH': 65536})
    df3 = df3.replace({'NA': 0})
    print("Sorting Dataframe by highest observed connection")
    df4 = df3.sort_values(by='Observed', ascending=False) # 4) You will then sort and display the output of your DataFrame with the highest observed connection first.
    print(df4)
    df4.to_csv("Rejouis-WK-2.csv") # 5) Finally you will save your resulting DataFrame as a .csv file 


    
    
