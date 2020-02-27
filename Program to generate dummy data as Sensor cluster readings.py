#!/usr/bin/env python
# coding: utf-8

# In[37]:


#This is a program to generate dummy data in .csv format for the 32 sensor clusters each containing 16 readings per cluster
import random
from datetime import datetime
import csv
import pandas as pd
from datetime import timedelta, date
from random import randrange
import datetime 


def random_date(start,l):
    #This function helps to generate a random time series within a given range.
    #Source: https://stackoverflow.com/questions/26740227/create-random-time-stamp-list-in-python

   current = start
   while l >= 0:
    current = current + datetime.timedelta(minutes=randrange(10))
    yield current
    l-=1
test_date=[] #creating an empty list to store timeseries to be used for our dummy data table

startDate = datetime.datetime(2020, 2, 25,14,00)


for x in (list(random_date(startDate,32))): #The random_date function is being called
    
    test_date.append(x.strftime("%d/%m/%y %H:%M"))    #storing randomly generated timedata into the test_date list


sensr_dicts = {} #Creating an empty dictionary called sensr_dicts which will contain the pipe reading data





for i in range(32):
    
    values = [] #creating an empty list for values of the dictionary
    for j in range(16):
        values.append(random.uniform(0.0, 1.0))    #assigning randomly generated floating numbers to the list that will
                                                   # be values in the dictionary
    p = test_date[i]
    values.append(p)                              #assigning the elements of the test_date list to the values of the dictionaary
        
        
             
    sensr_dicts[i+1] = values                     #assigning keys to values in the pipe reading data
    

#The code below converts the pipe reading data dictionary to a .csv table and exports it

file_number = 0

r = dict(("Sensor {}".format(k,file_number),v) for k,v in dicts.items()) #This adds the string 'Sensor' to each of the
                                                                         #key index in the dictionary

df = pd.DataFrame.from_dict(r,orient='index',columns=['Reading 1', 'Reading 2',
     'Reading 3', 'Reading 4','Reading 5', 'Reading 6', 'Reading 7', 'Reading 8',
    'Reading 9', 'Reading 10', 'Reading 11','Reading 12', 'Reading 13','Reading 14',
      'Reading 15', 'Reading 16', 'Time']) #naming columns for the pipe reading data

df.to_csv('Pipeline Thickness Sensor Data.csv') # write dataframe to file

