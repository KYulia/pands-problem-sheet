#My solution: Code for weekly task8 (plottask.py) written by Yulia Kiriy 
#reference: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
#The following code plots a graph of 3 different functions f(x), g(x), h(x)

#Importing the required mathematics libraries for plotting graphs 
import matplotlib.pyplot as plt
import numpy as np

#Defining the x-axis, in the range from 0 to 4, divided in 1000 points. 
x = np. linspace (0, 4, 1000) 

#Definition of the 3 required functions
def f(x): return x
def g(X): return x*x
def h(X): return x*x*x

#plotting the f(x) graph
plt.plot(x, f(x), label = "f(x)")
#plotting the g(x) graph
plt.plot(x, g(x), label = "g(x)")
#plotting the h(x) graph
plt.plot(x, h(x), label = "h(x)")
 
#naming the x axis
plt.xlabel('x - axis')
#naming the y axis
plt.ylabel('y - axis')
#Graph title
plt.title('Graph of functions f(x), g(x), h(x)')
 
#Shwoing a legend on the plot
plt.legend()
#Function to show the plot
plt.show()