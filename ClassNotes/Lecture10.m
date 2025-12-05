%Lecture 10
%review
%percentage sign to make notes

%be careful with math, matlab tendency to do matrix math
%Must specify non matrix math

%if you put semicolon ;, it will not print the command
m(3,1)

m([1 3], 1)
%telling to take the first column and look at variables at 1 and 3



% Lesson 9 - in class exercises
%% 9.1 - making if statements
% Let's start by shuffling the rng
rng('shuffle');

a = rand();
myVar = 1==1;

if a < 0.3  %if the value a is less than .33 (if it returns true)
    b = a.^2;  %square
elseif a >= 0.33 & a <= .66    
    another = true;
    b = 0;
else % if everything returned false
    b = a.^.5; %squareroot
end; %the end of my first if statment 

%% 9.2 - Switch/case

k = randi(6); % make a variable

switch k %start of switch
    case {1,2}
        VWMCapacity = 'low';
    case {3,4}
        VWMCapacity = 'med';
    otherwise
        VWMCapacity = 'high';  
    
end % end of switch

%% 9.3 - For Loops


var = 11:21 % create a vector

for i = 1:length(var) %loop through elements of that vector
    
    i
    var(i)
    a = var(i)^2
    
end % loop

%% 9.4 comparing indexing to loops

tic % start clock
a = zeros(1,10); % pre-allocating a variable
toc %end clock

b = [];
tic
for i = 1:10
    b(i) = i^2; %adding elements to b
end
toc

tic
for i = 1:10
    a(i) = i^2; %inserting elements into pre-allocated a
end
toc

%% 9.5 Embedding while loops

numLoops = 0;
a = 0;        %give it a start value
numLoops2 = 0;
numLoops3 = 0;
while a < .9    %make it meat some condition
    numLoops = numLoops + 1;
    a = rand();  %reset value of a
    if a < .5
        numLoops2 = numLoops2 + 1;
        if a < .1
            continue;
            numLoops3 = numLoops3 + 1;
        end %who do these belong to?
    end
    if a == .7    %here's an if statement that will break out of the loop
        break;
    end % who do these belong to??
end

%% 9. 6 -  indexing

x = round(10 + randn(100,1));  %random normal numbers centered on 10

(x==10)
x(x==10)
find(x==10)

%any and all

any(x==10)

all(x==10)

%% 9.7 - Functions

function myfcn(arg1,arg2,arg3)
if nargin < 3
    arg3 = some_value; %some default value
end;
if nargin < 2
    arg2 = some_other_value; %default value to make function more flexible
end;
end;

function outputArray = subtractOne (inputArray)
outputArray = inputArray - 1; % Subtract one from each element of the input array
end;

subjectNum = input ('Please enter the subject number:')

%% 9.8 - text

myText = ('This is some text') %class is character, size is 1x17, so it can be indexed
myText(10) %indexing

double(myText) %gives the unique number combination for each letter or combination of characters


%comparing strings:
'apples' == 'oranges'
strcmp('apples', 'oranges') %double quotes compares entire string, single quotes compares each character

%can ignore case with strcmpi

%string find:

strfind('where in the world is carmen sandiego', 'carmen sandiego')

name = input('What is your name?', 's')%s is the special character

fprintf %write text to file

%writing to file
fid = fopen('myFile.txt', 'wt');
rr = [1.1:5.1];





%string replace:

strrep('a a a a ', ' ', [])


% writing to a file:

fid = fopen('myFile.txt', 'wt');
rr = 1.1:5.1;

fprintf(fid,'%3.2f\t',rr);
fprintf(fid,'\n');
fprintf(fid,'%3.2f\t',rr + 2);

fclose(fid);

%% 9.9 - eval


numArrays = 10; 
A = cell(numArrays,1);
for n = 1:numArrays 
	A{n} = magic(n); 
    Eval(['A', int2str(n), ' = magic(n)']);
End

A{5}


Eval(['A', int2str(n), ' = magic(n)']);

%% structures and cells

cell1 = {'apples', 'oranges'}
cell1{1}(1)

cell2 = {[1 2 3 4 5], [1 2 3 4 5 6]} %elements do not have to be equal
cell2{1}(5) %first cell, fifth element

cell2{3} = "does this work?"

a = cell2{1} %returns type of class, not 1x1 variable

cell2mat

data2.subject = "SME"
data.rt = [0.9 1.2]
data(2).subject
data:.subject %shows all subjects

data.subject(1).block(2).trial(50).RT = 0.7650 %nested within eachother
%kind of like a class or database of information

%Define trials
function [nTrials stimType] = defineTrials(subject, condition)
%%

if (subject == 999) | (condition == 0)
    nTrials = 10;
    stimType = 0;
    return;   %end the function early. Not a great piece of code here...
               ...because could have used an else-if statement instead
end                   
nTrials = 100;
stimType(1:nTrials./2) = 1;
stimType(nTrials./2 + 1:max(nTrials))=2;
uselessVariable = 100 * 100; %this variable is local to that function, it does not exist after the function ends
end 

[trials, stim] = defineTrials(999, 0)

%

