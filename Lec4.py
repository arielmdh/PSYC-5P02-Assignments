# -*- coding: utf-8 -*-
#Lec 4
""" These are notes from lecture 4


this could be a multi line comment




"""

# Learning Spyder
# Unless you specify otherwise or if it exists in your current directory, python will not take things from other directory
#You can use the console as a bash shell, use ! in front of command to use the shell terminal. 
# For example: !git add, would in theory work as your bash shell
myVar="hello world" #writing hello world to myVar
#Loops: instruction that repeats until a specified condition is met
for i in range (1,5): 

    print(i)

#FOR loop, uses variable which is defined as a series of values
#prints 1,2,3,4 because RANGE IS NOT INCLUSIVE

for i in range (1,5): 
    print("I am in the loop")
    print(i)
    
print("I am out of the loop")
#Indent: invalid indent because you can't go back after indenting, the second indent doesn't do anything
for i in range (1,5): 
    print("I am in the loop")
print("what is this")
print(i)
    
print("I am out of the loop")
#i variable, created in the first loop as 4, continues as 4 later, can see in the variable window
#new loop
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)
    
mylist = ["apple", "banana", "cherry"]
for x in range(len(mylist)):
    print(mylist[x])
#range


#WELL Loop
i=1
while i <6:
    print(i)
    i+=1
#+= means take current value and add whatever is on the right (i=i+1)
#Don't get stuck in infinite loop, control C to stop loop
#Other wats to move around or exit out of loop
#the break command will exit out of loop entirely
#if i== 3:
  #  break
#Can use even if all conditions of the loop haven't been met
#Continue command will skip the remaining commands in the loop and move on to the next loop iteration
i = 0
while i < 6:
    i+=1
    if i == 3:
        continue
    print(i)
#Skips 3 because of the if statement and continue statement saying to go back to the beginning, skip over and continue
#Scope 
    #Region of the code in which a variable or resource is visable and accessible

#"global" denotes a global scope as opposed to a local one
#Import libraries

numpy.sqrt(4)
#calls the library of numpy to answer square root question
#cannot just do sqrt(4), will not work

import numpy as np
np.sqrt(4)
#Float is a floating point integer
#can specify sub categories from libraries to import
from math import cos, pi
print('cos(pi) is', cos(pi))
#Random number generator
#tied to seed, can set your seed to a specific value or get the state of the random number generator (RNG)
import random
help (random)

help(random.randint)

import random
random.randint (0,10)

print (random.getstate())

myState = random.getstate()
random.randint(0,9)

random.setstate(myState)

random.randint(0,9)
random.seed (1)

random.randint(0,9)
#You can go back and look at where your random generator was seeded
#Recreate what would otherwise be random
#Know what your seed is or control it, tie it to time of day, participant number, etc.\
#Use tab, random. then hit TAB, it can autocomplete the available commands
#Random.normalvariate, want to simulate data, generally they are normally distributed

#Functions
#Ways to reuse code to increase efficiency
#Functions can take arguments (inputs) and can return values (outputs)
def nameprintfunc(name):
    print('the name is' + name)
    return name
#Function ends with a colon and everything within the function should be indented
#to print like this, it does nothing
#But if you put in terminal, "nameprintfunc", it errors because we haven't given it an argument

print('Steve')
nameprintfunc('Steve')

myName = nameprintfunc('Steve')

def adderFunc(val):
    x = val + val
    print(x)

adderFunc(2)

#Not in variables, due to scope
#That value of x is unreadable outside of that function

x = adderFunc(2)

def adderFunc(val):
    x = val + val
    print(x)
    return x
#X shows up as Nonetype because it only exists within that scope to kick it out of the scope have to use return

def adderFunc(val = 4):
    x = val + val
    print (x)
    return x

adderFunc()

def adderFunc(val1, val2 = 4):
    x = val1 + val2
    return x

#Two arguments, one is required first one, val2 is overridden is user puts two numbers

adderFunc(2,5) #both specified
adderFunc(2) #only one specified

def adderFunc(val1, val2 = 4):
    x = val1 + val2
    y = (val1 + val2) *2
    return x, y

a, b = adderFunc(10, 5)

#Tuple unchangable, lists changable
c = adderFunc(10,5)
c[1] = 0 #cannot change

def adderFunc(val1, val2 = 4):
    """Adds two numbers together
    
    
    """
    x = val1 + val2
    y = (val1 + val2) *2
    return x, y

help(adderFunc)
# can write in own help function

#Classes
#like functions that have data, built flexibility within code, ex. subject information, condition information
#Object-oriented programming
#Create a class, has attributes (data), methods (operations)
#Ex. Class = car, methods = drive, brake, attributes = speed, colour
    #instances = Toby's car, Maggie's car.
    #Each has own attributes
    
class car: #definition of a class
    def __init__(self, color='white'): #initialize attributes of every instance of the class
        self.speed = 0 #self allows you to access variable from anywhere else in class
        self.color = color #color is defined by (optional) input
    
    def drive(self): #a method for the object (car)
        self.speed = self.speed + 1
    
    def breaking(self):
        self.speed = self.speed - 1
#can only call breaking and drive on cars
vw = car()
vw.speed
#vw is the object, the period calls the specified attribute of that thing

vw.drive

for i in range(1,100):
    vw.drive()
print(str(vw.speed))
        
#You can import classes from other files
#from filename import class
# %% cell 2
1+1
#Making new cells
#%% Cell 3


