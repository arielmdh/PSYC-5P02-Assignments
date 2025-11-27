%Lecture 9 notes
%percentage sign to write notes
A = [1 2 3 4 5]
B = [1 2 3 4 5]

%if you put semicolon ;, it will not print the command
%if you put 1+1 in command window, if you do not create a variable, it will
%create a variable called ans

%if you write file name into command window, it will run file top - bottom 
%who = what variables
%whos= more information about variables
d = [1;2;3;4;5]

%row by column structure

m = [1 2; 3 4; 5 6;]

w = [1 2; NaN 4; 5 NaN]

% indexing done with round brackets

A(3)

m(3)

m(3,1)

m([1 3], 1)
%telling to take the first column and look at variables at 1 and 3

trials = [1 3]
m(trials,1)

m(:,2)
%colon specifies everything in that vector
%colon by itself means everything, colon between two values is a range,
%(2:end,2) means from 2 to the end of the range

a = [1 3 5 7 9]

% a'
 
a = [1 2]
b = [3 4]
c = [a b] %concatenate variables

c(5) = 5 %extends matrix
c(10) = 6 % fills in everything in between with zeros

c(6:9)=[] %take the values from 6 to 9 and delete them 

%pre-allocate your matrix
%fill with zeros or ones
a = zeros (5,5);
b = ones (5,5);
c = NaN (5,5);

whos
why

rot90(a)
%rot takes arrange and shifts it 90 degrees

a.*[1 2]
%multiplication and division automatically does matrix
%multiplication/division, have to put period to do individuals

%Saving variables
save('myFirstMat')

clear

load myFirstMat.mat

% Help function
help save

% most functions built in --> mean, std, etc. 
%does column wise mean
mean(a)
%does row wise mean
mean(a')
mean(a,"all") %entire matrix

%How to deal with pseudo random number that matlab assigns
%can reset the random number generator with rng ('shuffle')
%Can also seed random number

a = rng()
%returns structure

a.State
