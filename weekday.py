#My solution: Code for weekly task5 (weekday.py) written by Yulia Kiriy 
#Modified program from source
#source https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

#The following code checks whether the day when the programm is ran, is a weekday or weekend. 

import datetime #Importing the datetime library
week_number = datetime.datetime.today().weekday() #receiving data about the day when programm is ran

if week_number < 5:
    print ("Yes, unfortunately today is a weekday ") #If week_number is 5, 4, 3, 2, 1 
else:  # 5 Sat, 6 Sun
    print ("It is the weekend, yay!") #If week number is 5 or 6