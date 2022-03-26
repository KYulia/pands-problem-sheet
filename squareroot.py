#My solution: Code for weekly task6 (squareroot.py) written by Yulia Kiriy 
# Source of knowledge: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html

#The following programm is using the Newton-Raphson method ...
#... to find an approximation for the square root of a number entered by the user

#The approximation function is defined
def NR_Method(y, epsilon, guess):
    #Using the NR-method calculations
    while abs(guess * guess - y ) >= epsilon: 
     guess = guess - (((guess**2)-y)/(2*guess)) #Calculating the new guess
    print('The square root of '+ str(y) + ' using Newton method is aproximatelly ' + str(guess)) #Printing the results of the approximation
    
y = float(input("Please enter a positive number: ")) #Interaction with the user of the programme
epsilon = 0.1 #Defining the difference
guess = y/2.0 #First guess 
NR_Method(y, epsilon, guess) #Callling the function to find the approximation
