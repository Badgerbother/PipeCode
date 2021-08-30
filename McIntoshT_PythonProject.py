# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 21:27:37 2018

@author: Tara McIntosh

This program is designed to calculate the maximum allowable vapor velocity in a vapor
separator drum. It utilizes the Souders-Brown Equation to do so. 

SOURCES:
    “Souders–Brown Equation.” Wikipedia, Wikimedia Foundation, 24 Apr. 2018
    “Python: Create a List of Tuples from File.” Stack Overflow
    "Paint by Numbers 1-4" Blackboard. McQuade, Tyler. 3 May. 2018
    
    
SOME NOTES:
I tried a loop like this 'for i in range ()' but couldn't get it to work how I wanted,
my intention was to have a 'for i in range' loop that looped through all the k values in the csv file
and then pick the correct k value to use according to the pressure they inputted, I also wanted to use this loop to follow the k-value pattern
of 0.107-0.003 (see article) and have it generate hundreds of data points using that loop - couldn't get it to work. 
    
"""

import pandas as pd #this allows me to read the csv file in python
import numpy as np #this allowed me to put the csv data into an array
import math #this allows me to use the sqrt function
import matplotlib.pyplot as plt #this makes python act like matlab and allows me to plot my data

print("NOTE: Gauge Pressure has a limit of 126 bar in this program.") #lets the user know theres a limit on pressure values they can input

k = float(input("Enter Gauage Pressure of Vertical Drum Separation Vessel (bar): ")) #user inputs gauge pressure and then a k-value is selected using a loop
pl = float(input("Enter Liquid Density Value (kg/m3):" )) #defines variable for liquid density
pv = float(input("Enter Vapor Density Value (kg/m3):")) #defines variable for vapor density

#this reads the CSV into python and puts the data into an array
readcsv = pd.read_csv('csvk.csv') #just put the name of the csv in the quotations (don't need the location)
readcsv.replace(" ","_")
kdata = np.array(readcsv)

#this is a for/else loop
#this loop is designed so the when the user inputs the gauge pressure inside the drum
#the program will automatically select the corresponding k value (see cited article about pressures  and k) 

if k <=7:
    kc = kdata[0,0]
else:
    if k<=14:
        kc = kdata[1,0]
    else:
        if k<=21:
            kc = kdata[2,0]      
        else:
            if k<=28:
                kc = kdata[3,0]
            else:
                if k<=35:
                    kc = kdata[4,0]
                else:
                    if k<=42:
                        kc = kdata[5,0]
                    else:
                        if k<=49:
                            kc=kdata[6,0]
                        else:
                            if k<=56:
                                kc=kdata[7,0]
                            else:
                                if k<=63:
                                    kc=kdata[8,0]
                                else:
                                    if k<=70:
                                        kc=kdata[9,0]
                                    else:
                                        if k<= 77: 
                                            kc = kdata[10,0]
                                        else:
                                            if k<=84:
                                                kc =kdata[11,0]
                                            else:
                                                if k<=91:
                                                    kc=kdata[12,0]
                                                else:
                                                    if k<=98:
                                                        kc=kdata[13,0]
                                                    else:
                                                        if k<=105:
                                                            kc=kdata[14,0]
                                                        else:
                                                            if k<=112:
                                                                kc =kdata[15,0]
                                                            else:
                                                                if k<=119:
                                                                    kc = kdata[16,0]
                                                                else:
                                                                    if k<=126:
                                                                        kc =kdata[17,0]
#this next part contains the equation and a loop to stop the program so a math error does not occur
if pl > pv:
        v= (kc*math.sqrt((pl-pv)/pv)) #this is the Sonders-Brown Equation
        print("Maximum Allowable Vapor Velocity (m/s): ", v) #This prints the variable
else: #this if/else statement prevents a math error from occuring if diving by 0 or creating a negative number under a square root
    print("ERROR! Liquid Density must be greater than Vapor Density. Try Again.") 


#this part generates all of the data for plotting
    
x = kdata[:,1]    #this is a range of pressures in bar I typed out in a CSV file in excel. #It ranges from 0-126 bar  

y = kdata[:,0]*(math.sqrt((pl-pv)/pv)) #this creates a range of vapor velocity values by making 'k' (which varies) -
#everything in the first column of the csv. I then multiplied it by the rest of the equation from the user's inputs which remain constant.

#This next part creates the plot

plt.scatter(x,y) #creates the plot
plt.xlabel('Pressure (bar)') #adds an x axis label
plt.ylabel('Maximum Allowable Vapor Velocity (m/s)') #adds a y-axis label
plt.title('Vapor Velocity vs. Pressure in Vertical Drum with Horizontal Mesh Pad') #adds a title to the graph
    

                                    
        
                    
                   