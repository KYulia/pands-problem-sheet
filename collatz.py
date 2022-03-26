#My solution: Code for weekly task4 (collatz.py) written by Yulia Kiriy 
#The following code uses the idea of the collatz conjecture

#Using variable 'number' to store the integer entered by the user
number = int(input("Please enter a positive integer:")) 

while number != 1: #While the number entered is not 1
        print(number) #Print the number inside the while loop
        if (number % 2) == 0: #Checking if the number is even
              number = int(number/2) #Dividing the number by 2
        else: #If the number is odd
              number = int(3 * number + 1) #Muplitplying the number by 3 and adding 1

else: print(number) #If the number is 1, end the While loop and print number 1            
