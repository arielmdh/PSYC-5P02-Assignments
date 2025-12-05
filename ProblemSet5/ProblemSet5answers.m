%Problem set 5 Dennison-Hardy
%Question 1
%Using logical indexing 
RT = [520 498 601 1200 450 475 3000 510 490]; %Given
RT_clean=RT>1500 %create vector that removes rts using simple indexing
filteredRT = RT(RT_clean); %apply it to the rts

mean(filteredRT) %calc mean
median(filteredRT) %calc median
% Calculate the number of filtered values
numFiltered = numel(filteredRT); %numel displays total number of elements in array, source: Mathworks

% Display the results
disp('Mean of filtered values:'); 
disp(mean(filteredRT));
disp('Median of filtered values:');
disp(median(filteredRT));
disp('Num of RTs removed')
disp(numFiltered)


%Question 2
%Create matrix
stim_intensity = randi([1, 100], 10, 1); %stimulus intensity, values between 1 and 100, 10 trials, in column. using randi from MatLab help center for creating uniformly distributed random integers
condit = randi([1,2], 10 ,1); %condition , values between 1 and 2, using randi again
resp = randi([1,2], 10, 1); %response, same as condition

data = [stim_intensity,condit,resp]; %Put it all together in a matrix

disp(data); %display data, looks ok

%extract high load data
highloadcolumn = data(:,2) == 2; %where condition is equal (==) to 2, using (:,2) to index correct location in matrix
highloadData = data(highloadcolumn, :); %create new matrix for the high load data
disp(highloadData) %display again, looks right

%Means
meanHighLoad = mean(highloadData(:, 1)); % Mean of stimulus intensity for high load
meanLowLoad = mean(data(data(:,2) == 1, 1)); % Mean of stimulus intensity for low load


disp(meanHighLoad)
disp(meanLowLoad)

%Question 3
%if statement
criterion = 50; %Given

num_trials = 10; %define number of trials

%Loop through trials, using a for loop to define accuracy
for i = 1:num_trials
    stimulus = stim_intensity(i); %defining what variables to look at
    response = resp(i);

    if stimulus < criterion %refresher on if statements, youtube video "For Loop with If statement in MatLab" and "Nested Loops" from Educate Yourself
        correct_response = 1;

    else 
        correct_response = 2;
      
    end

    if response == correct_response
        outcome = 'Correct!';
    else
        outcome = 'Incorrect!';
    end 

    fprintf('Trial %d: %s\n', i, outcome); %source: how to write data to text file, "fprintf", mathworks, matlab help center
end


%Question 4
%Create variable
num_values = 100;
mean_rt = 0.700
sd_rt = 0.100
min_noise = 0 
max_noise = 400

reg_rts = mean_rt + sd_rt * randn(num_values, 1); %define rts without noise added, normally distributed around .700 ms, randn allows for random normally distributed numbers
%formula on matlabhelpcenter "random numbers from normal distribution with
%specific mean"

noise = min_noise + (max_noise - min_noise) * rand(num_values, 1); %calc noise the same way

rts = reg_rts + noise; %combine them

%Create function
%In separate file

% Initializing a variable to store removed values
removedRTs = [];
% Initialize counter for how many removed
iterations = 0;

% Start the cleaning process by using the function applied to our data
[cleaned_RTs, removedRTs, iterations] = removeOutliersRecursive(rts, removedRTs, iterations);

% Print the final results
fprintf('Original total samples: %d\n', length(rts)); %was super painstaking to figure out how to use the fprintf, not sure it's totally worth it
fprintf('Final cleaned mean: %.4f ms\n', mean(cleaned_RTs));
fprintf('Total iterations performed: %d\n', iterations);
fprintf('Total number of outliers removed: %d\n', length(removedRTs));

%Question 5
%this is where I loaded my file from, probably would need to be changed to just
%load("experiment_data.mat)
load("C:\Users\Asus\Downloads\experiment_data.mat")
fprintf('Participant ID: %s\n', data.participant) %print the participant number

num_trials = numel(data.trials); %using numel (again? I think I used it before)
fprintf('Number of trials: %d\n', num_trials);

rts_data = data.trials.rt; %identifying where in structure
data.mean_RT = mean(rts_data); %calc mean, and add new field

fprintf('Mean RT: %.2f ms\n', data.mean_RT);
 
%Not sure how to compute accuracy without knowing which response is correct
%and which isn't, additionally not knowing if you want a yes/no accuracy or
%overall? The easiest route is to calculate accuracy assuming that a 'yes'
%response is accurate and then calculating the overall accuracy based on
%that. Sorry if that's not what you're looking for. 

% Access the responses made by participant in structure
responses_made = data.trials.response;

% Determine which responses were accurate ("yes")
% The 'strcmp' function compares strings and returns a logical array (1s and 0s)
accurate_mask = strcmp(responses_made, 'yes');

% Sum the array to count the number of accurate responses
num_accurate = sum(accurate_mask);

% Calculate the overall accuracy as a percentage, using num trials from
% before
data.accuracy = (num_accurate / num_trials) * 100;

disp('Overall accuracy:')
disp(data.accuracy) %wanted to use fprintf again but couldnt figure out the correct %d/n thing to make it look right


%Creating new subject
% Define the number of trials for the new subject
num_new_trials = 10;

%creating 10 random rts between 400 and 800 ms, based on the rts from the
%first participant
% rand(10, 1) generates 10 random numbers between 0 and 1
new_RTs = 400 + rand(num_new_trials, 1) * 400; 

% Use the 'deal' function to assign values to fields of a new structure
% [Output1, Output2] = deal(Input1, Input2);
[new_subject.participantID, new_subject.RTs] = deal('P002', new_RTs);


