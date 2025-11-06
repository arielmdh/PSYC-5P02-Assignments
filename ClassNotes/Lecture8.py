# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 14:41:51 2025

@author: Asus
"""
#Exercise: create a multidimensional list of x + y coordinate pairs (as tuples)

coords = [1,1], [1,2], [1,3]
type(coords[0])

nbaTeams= {
    'Los Angeles':'Lakers',
    'Toronto':'Raptors',
    'Chicago':'Bulls'
    }

#dictionaroes are indexed by keys, which cane be immutable type
#Keys have to be unique

#Instead of curly brackets use dict()
#First item key, second item value

nbaTeams["Toronto"]
#OR
nbaTeams.get("Toronto")

#to create array, you have to call array method
import numpy as np
arr = np.array ([1,2,3,4,5])
#round brackets start functions, square brackets defining array

mdArr = np.array ([[1,2,3],[4,5,6],[7,8,9]])
print(mdArr)

#Make three dimensional array

3darr = np.array ([[[0,0,0],[0,0,0]],[[1,1,1],[1,1,1]]])

mdArr[0]
#takes first slice out of array

mdArr[0,1]
#take from first row, second column

for x in mdArr:
    print(x)
    for y in x:
        print(y)
#for the values of y that move across the second dimension (x)
#arr.reshape (4,3): reshapes an existing 1 x 12 array into 4 x 3 array

#can index specific values using Boolean mask
newArr = [5,6,2,4,7,8,2,1,0]
newArr = np.array(newArr)
#want to find values greater than 2
import numpy as ma
mask = newArr > 2

newArr[mask]
cleanData = newArr[mask]
cleanData = newArr[newArr>2]

newArr2=[0,1,2,3,4,5,6,7,8]
newArr2= np.array(newArr2)

x = newArr[newArr2>4]
cleanData = rt[(cond == 1) and (block > 4)]

#np.nonzero(a) returns all the nonzero elements
#np.where(condition, [x,y], /) returns elements from x or y depending on condit

data = np.loadtxt(fname='inflammation-01.csv', delimiter=',`)

data = inflammation01csv
print(data.shape)
print(type(data))

data[10,35]
print(data[0:4,0:10])

data[0,:]
data[0,5:-1]

data[0:1,0:1]

meanval = np.mean(data, 0) #calculates row
print(meanval)

meanval = np.mean(data, 1) #calculates columns
print(meanval)

meanval = np.mean(data[0],0) #just one row

#calculate rows or columns
np.mean(data[0,:])

np.mean(data[:,0])

#Numpy random
from numpy import random
random.randint(100)

randData = random.randint(5,10,size=[10,50])

random.rand() #0 - 1
random.choice(data[0:]) #random from array

conds = [0,1,2]
print
random.shuffle(conds) #shuffles list

#Random Distribution(binominal, random, etc)
#Normally distributed from certain SD
#Good for simulating data

#PANDAS
#can handle numbers, strings, etc., all together
#two data structures: Series and DataFrame

import pandas as pd
volumes = pd.Series(['4 cups', '1 cup','2 large', '1 can'])

pd.Series(data=['4 cups','1 cup','2 large', '1 can']) #same thing

s = pd.Series(data=[1,'2',3,4,'5',6,7,8,'99','100'])
x = s.astype('int')

x.mean()

data = pd.Series([1,2,pd.NA,4,5])
data.dropna(inplace=True)

data.fillna('Null', inplace = True)

data = pd.Series([1,2,3,4,5])
data.apply(np.sqrt)
data.apply(lambda x: x+1) 
#applying to set of data, add noise, transform data, analysis data, especially for simulating data

#DataFrame
data = pd.read_csv('RTdata')

data['subjs'][5]
data = pd.read_csv('RTdata', index_col='subjs')
#can index by anything

#Exercise: get rts for race:cauasian sex:female, then combination of both

data.iloc[2,5]
data.loc[:]['K'] #index by column K

data.iloc[:,5] #calls column K as well, two different methods for same outcome

data.groupby('sex').mean()
output.loc['m']['RTs']

output = data.groupby(['sex','race']).mean()
print(output)

data.loc[:,'sex']
import numpy
help(np.mean)
data.mean()

titanic["Name"].str.lower()
titanic["Name"].str.split(",") #split by comma
titanic["Surname"] = titanic["Name"].str.split(',').str.get(0)