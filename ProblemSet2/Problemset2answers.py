# -*- coding: utf-8 -*-
"""
PSYC 5P02 Problem Set 2
"""
#Question 1
#Works I think
#a) 100 normally distributed values mean of 0.7 and SD of 2 by importing numpy and creating random distribution, using .normal function to define a normal distribution
import numpy as np
randomdist = np.random.normal(loc=0.7, scale=2, size=100) #defining a mean and sd for the distribution
#b) create function to calc mean and SD, remove over 2.5 SDs of the mean
#First have to define a function

def remove_outliers(data,threshold=2.5):#define function, specify SD threshold
    data_array = np.array(data) #turn data into an array
    total_outliers = 0 
    outliers_found = True #using true false to set when loop stops instead of a break, when I tried with break I couldn't figure it out. 
    while outliers_found: #using while loop instead of for loop so it continues trimming until there are no more outliers i.e. outliers found = false
        outliers_found = False
        mean = np.mean(data_array) #calculating mean
        std = np.std(data_array) #calculating standard deviation
        lower_bound = mean - (threshold * std) #defining the lower bound, 2.5 sd lower than mean
        upper_bound = mean + (threshold * std) #defining upper bound, 2.5 higher than mean
        is_outlier = (data_array < lower_bound) | (data_array > upper_bound) #defining that an outlier is either 2.5 lower or higher than the mean
        if np.any(is_outlier): #if there is an outlier, remove it! Found in numpy library, helpful!
            num_removed = np.sum(is_outlier) 
            total_outliers+= num_removed #adding up the outliers that are removed, in lec 3
            data_array = data_array[~is_outlier] #using boolean mask (?) to remove outliers
            outliers_found = True 
            
    final_mean = np.mean(data_array) #added calucation for final mean and standard deviation, I think
    final_std = np.std(data_array)
            
    return data_array.tolist(), total_outliers, final_mean, final_std #returning all the needed info 

print("original distribution:", randomdist) #just looking at dist first

cleaned_data, removed_count, final_mean, final_std = remove_outliers(randomdist,threshold=2.5) #applying it to my random distribition

print("/nCleaned data:", cleaned_data) #return new data set
print("Total outliers removed:", removed_count) # how many it took out

print("Final mean:", final_mean) #print final mean
print("Final standard deviation:", final_std) #print final std


   
#Question 2
#Works
#a) Make list
namelist = ["Adam", "Jane", "John", "Mary", "Charles", "Agnes", "Ernie","Dorothy", "James", "Betty"] #I looked up "old names" for this
import random
gradelist = [random.randint(76, 100) for _ in range(10)] #using random number generator instead of typing in number list (what I did the first time)

for i in range(len(namelist)):
    name = namelist[i]
    grade = gradelist[i]
    
    if grade >=90: #classic if statement like in lec 3/4
        letter_grade = 'A+'
    elif grade >=85:
        letter_grade ='A'
    elif grade >=80:
        letter_grade = 'A-'  
    else:
        letter_grade = 'B+'
    print(f"{name} recieved a perentage of {grade}, which is a(n) {letter_grade}.")

#Question 3
#Inefficent :(
def gradeLookup():
    student_name = input ("Enter Student Name:")
    if student_name == "Adam": #needs to be variable instead of set 
        print(f"Adam, 85, A")
        
    elif student_name == "Jane":
        print("Jane, 86, A")
    elif student_name == "John":
        print("John, 86, A")
    elif student_name == "Mary":
         print("Mary, 82, A-")
    elif student_name == "Charles":
         print("Charles, 99, A+")
    elif student_name == "Agnes":
       print("Agnes, 78, B+")
    elif student_name == "Ernie":
        print("Ernie, 86, A")
    elif student_name == "Dorothy":
        print("Dorothy, 84, A-")
    elif student_name == "James":
       print("James, 99, A+")
    elif student_name == "Betty":
       print("Betty, 91, A+")
    else:
        print(f"Student not found in gradelist")

gradeLookup()

       
#Question 4 
#This one went well actually (I think)
#making a class   
class PersonalityProfile: #defining a class called "personality profile", just like the cars
    def __init__ (self, participant_number, openness, conscientiousness, agreeableness, extraversion, neuroticism): #defining each attribute i.e. personality trait
        self.participant_number = participant_number
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.agreeableness = agreeableness
        self.extraversion = extraversion
        self.neuroticism = neuroticism
    
    def is_introvert(self): #defining the function that determines introversion
        return self.extraversion < 3
    
    def low_openness(self): #continue to define the rest of the traits
        return self.openness < 3
    
    def low_conscientiousness(self):
        return self.conscientiousness < 3
        
    def is_disagreeable(self):
        return self.agreeableness < 3
    
    def is_neurotic(self):
        return self.neuroticism < 3

    def summary(self): #defining the bonus function of summary
        personality = {
            "Openness": self.openness,
            "Conscientiousness": self.conscientiousness,
            "Agreeableness": self.agreeableness,
            "Extraversion": self.extraversion,
            "Neuroticism": self.neuroticism
            }
        strongest_trait_score = max(personality, key=personality.get) #I had to look up which function could pull out the largest item in a list, it is the max() function, need to specify what my parameters are for largest, this is where I define my key, that i am looking for the largest value within my personality traits. 
        return f"Strongest trait is {strongest_trait_score}" #return a little phrase too, why not
        
  Person1 = PersonalityProfile(1, openness = 1, conscientiousness = 2, agreeableness = 3, extraversion = 2, neuroticism = 2) #set up my person's profile
  Person1.is_introvert()
  Person1.is_disagreeable()
  Person1.summary()
#and they work!



