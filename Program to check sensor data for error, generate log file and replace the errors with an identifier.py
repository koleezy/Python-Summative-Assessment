#!/usr/bin/env python
# coding: utf-8

# In[20]:


#python program to check the generated sensor data for errors and print a log file containing the errors 
#and also replace the error cells with a unique numeric identifier
import random
from datetime import datetime
import csv
import pandas as pd
from datetime import timedelta, date
from random import randrange
import datetime 
from pandas import *


def errorcheck(excel_file):
    #This function is used to check for error in the sensor data, generate a log file and replace the error values with
    # the number 100 which will serve as our unique identifier
    
    output_filename= input('Enter filename for error log:').upper() #Enter the name you wish to call the error log
    file_parse = excel_file.parse()                             #This parse the sensor data
    erlog_dict= file_parse.to_dict()                            #This converts the excel table to a dictionary
    with open("Error log file for Pipeline Thickness Sensor Data1.txt", "a") as f: #This ouputs the log file
        print('\t\t********ERROR LOG FILE'+' FOR '+ output_filename +'*********\n',file=f)
        for key,value in erlog_dict.items():
            count=0
    
            for sub_key,sub_value in value.items():
        
                if sub_value =='err':                       #This checks for error in the dictionary
                    count+=1
                    print(str(key)+' error has occured in '+ 'Sensor '+str(sub_key+1)+' at the time ' + str(erlog_dict['Time'][sub_key]),file=f)    #This specifies exactly where the err cell is found 
                                                                                                                                                    #in the dictionary
                          
                    value[sub_key]= 100       #This replaces the error reading with numerical value '100'
            if count==0:
                {}
            elif count==1:
                print('\n\'There is only '+str(count)+' sensor that contain error in '+ str(key)+'\''+'\n',file=f)#This tells us how many sensors 
                                                                                                                   #contains error for a particular reading 
            else:
                print('\n\'There are '+str(count)+' sensors that contain error in '+ str(key)+'\''+'\n',file=f)#This tells us how many sensors 
                                                                                                                   #contains error for a particular reading 
    print(output_filename + ' LOG DATA SAVED!!!!')
    
    

    
    df = pd.DataFrame.from_dict(erlog_dict) #This coverts the dictionary to a dataframe
    df.to_csv('Pipeline Thickness Sensor with replaced values1.csv') #converts to .csv table an exports the file
    


sn_data_xls = ExcelFile(r'C:\Users\Kolsoma\Pipeline Thickness Sensor Data with Error Values.xlsx')   #This specifies the path to sensor data containing eerror


#The function created is tested below
errorcheck(sn_data_xls)







    
        
            






