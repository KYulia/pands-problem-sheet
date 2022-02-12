#My solution to weekly task 02
#Code to calculate bmi
#Written by Yulia Kiriy

#REFERENCE: Formula for BMI was obtained at https://bmi-calculator.io/bmi-calculation-formula


weight = int (input ("Enter your weight (kg): ")) #Inputting weigth in killogram
height = int (input ("Enter your height (cm): ")) #Inputting height in centimeters
height_m = height/100 #Converting height in centimeters to height in meters

bmi = (weight / (height_m * height_m) ) #Computing the BMI
print ('Your BMI (kg/m^2) is {}'.format(bmi)) #Printing the calculated BMI result