import pandas as pd
from os import path
from pathlib import Path
import pathlib
import datetime
import sys
import os
import glob
from datetime import date 
from datetime import timedelta
import csv
# os.chdir("/mydir")

# cwd = os.getcwd()
# files = os.listdir(cwd) 
# file_d= "C:/xampp/htdocs/x/A.txt"
# Biscuit_files = glob.glob("C:\\xampp\\htdocs\\x\\A*.txt")

# # for i in Biscuit_files:
# #     print (i)

# combined_csv = pd.concat([pd.read_csv(f) for f in Biscuit_files ])

# #export to csv
# All_pd = pd.read_csv(file_d ,names=['msisdn'], low_memory=False)

# print(combined_csv)

largest = None
smallest = None

A = []

while True:
    
 num = input("Enter a number: ")
        
 if num == "done":
    print(A)
    break
         
 try:
    A.append(int(num))
    
 except:
    print("Invalid input")
    continue

 for x in A:

   if largest is None:
            largest = x
            
   elif largest < x:
            largest = x
            
 for x in A:

   if smallest is None:
            smallest = x
            
   elif smallest > x:
            smallest = x   
    
print("Maximum is", largest)
print("Minimum is", smallest)
