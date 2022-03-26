#Im writing a program that will input a string and outputs every second letter in reverse order
#Author Yulia Kiriy
#Weekly Task 03

#Reference source: https://www.w3schools.com/Python/python_howto_reverse_string.asp

#Defining a function which outputs every second letter of an input string
def my_function(x):
    return x[::-2]

txt = input("Please enter a sentence:") #Asking the user to enter a sentence

mytxt = my_function(txt) #Calling the function 
print(mytxt) #Printing every second letter of the sentence







