# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:34:03 2025

@author: Asus
"""
#PSYC 5P02 Midterm
#Ariel Dennison-Hardy


#Question 1
import random 
import statistics #importing needed libraries, trying to use statistics even though I used numpy for previous assignments, I think statistics will be easier in this case. 
randomrtlist = [random.randint(450, 700) for _ in range(10)] #creating a random list of reaction times between 450-700 ms, using my notes from lecture 5
mean = statistics.mean(randomrtlist) #calculating the mean using the statistics package, also using my lecture 5 notes for instructions for the statisitcs packages
sd = statistics.stdev(randomrtlist) #calculating the sd for the reactions times using the statistics package


min(randomrtlist) #printing the min value using min() function, had to double check that both min and max were a thing, as we've only used one before
max(randomrtlist) #printing the max value using max() function, which we used in problem set 2
print (mean) #printing mean and sd
print (sd)

#Question 2
# I think there is probably a shorter way to go about this, but this is what makes the most sense to me so I'm going with it. 
import numpy as np #using numpy again
def trimmed_rts(data): #defining a function, using my work for problem set 2 for this entire question
    data_array = np.array(data) #Turn data into an array, again, not sure if this is needed but it makes sense to me
    total_outliers = 0 
    outliers_found = True #using true false to set when loop stops
    while outliers_found: 
        outliers_found = False
        mean = np.mean(data_array) #calculating mean
        std = np.std(data_array) #calculating standard deviation
        lower_bound = 600 #defining the lower bound, no higher bound for this question
        is_outlier = (data_array < lower_bound) #defining that an outlier is either 2.5 lower or higher than the mean
        if np.any(is_outlier): 
            num_removed = np.sum(is_outlier) 
            total_outliers+= num_removed #counting how many values trimmed
            data_array = data_array[~is_outlier]
            outliers_found = True 
            
            
    return data_array.tolist(), mean, total_outliers #returning all the needed info 

trimmed_rts, mean, total_outliers = trimmed_rts(randomrtlist) #applying it to my random distribition
print("Trimmed reaction times:", trimmed_rts) #return new data set

print("Final reaction time mean:", mean) #print final mean
print("Total reaction times trimmed:", total_outliers)
#Took me forever to figure out why the total trimmed and mean were not working, turns out you have to have them in the same order that you put when you apply it to your list. Or at least when I switched them, it started working. Yippee

#Question 3
def summarize_rts(rts_list): #create a function just like the last question
    data_array = np.array(rts_list)
    mean = np.mean(data_array) #calculating mean
    std = np.std(data_array) #calculating standard deviation
    #print("# of Trials:", size)
    print("Reaction time mean:", mean) #print final mean
    print("Reaction time standard deviation:", std) #print final std
summarize_rts(randomrtlist) #using my new function on my OG list
summarize_rts(trimmed_rts) #using my new function on trimmed list

print("Trimmed data is faster than untrimmed data by:", 645.2 - 596.3, "ms" )
#Terrible for hard coding this in but it works 

#Question 4
#I spent the most time on this question, possibily because I decided to name my lists with a bunch of 's's everywhere that I kept forgetting everytime I typed it. I should use Tab
subject_rts = [] #empty list ready for some data
subject1_rts = [random.randint(450, 700) for _ in range(10)] #I almost hard coded values in but decided to use random instead, growth!
subject_rts.append({"subject_id": 1, "rts": subject1_rts}) #using the append function, to adjust the list. I looked up this function to make sure I was using it right. Found article on Psychopy.org  

subject2_rts = [random.randint(450, 700) for _ in range(10)]
subject_rts.append({"subject_id": 2, "rts": subject2_rts})

summarize_rts(subject1_rts) #using function on subject 1 reaction time
summarize_rts(subject2_rts)

print (subject_rts) #just checking

subjects_rts_means = [] #Doing the same thing again but with the means
subject1_rts_mean = statistics.mean(subject1_rts)
subjects_rts_means.append(subject1_rts_mean)

subject2_rts_mean = statistics.mean(randomrtlist)
subjects_rts_means.append(subject2_rts_mean)

print (subjects_rts_means) #just checking again

overall_mean = statistics.mean(subjects_rts_means)
print (overall_mean) #print overall mean of two subjects
       
#Question 5
#I could not figure this out, then ran out of time. But I was definietly going somewhere with it. 

class Participant:
    def __init__ (self, pid, rts)
        self.pid = pid
        self.rts = rts
        
    def mean_rt(self): 
      return mean_rt = statistics.mean(rts)
  
    def add_rt(self):
        
    def num_trial(self): 
        return 
    
#Question 6
# separate file upload