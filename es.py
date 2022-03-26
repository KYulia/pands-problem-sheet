#My solution: Code researched and modified for weekly task7 (es.py) written by Yulia Kiriy 
#2 sources of code were used to research and understand the approach and the method for the exercise
#Source1: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#Source2: https://python-forum.io/thread-12065.html

#The following programm asks the user to enter the name of the text file being analysed...
#The programm then counts the number of times the letter (entered by the user) occurs 

fname = input("Enter file name: ") #The name of the text file is entered
x=input("Enter letter to be searched:") #the letter is chosen by the user
k = 0 #Initialization of the variable

#Approach to obtain the count of the occurance of one letter in a textfile 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==x):
                    k=k+1
#Displaying the results of the search and count                    
print("Occurrences of the letter:") 
print(k)