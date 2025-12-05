
%Creating the remove outliers function, used the example from class,
%powerpoint, explanations of how the rmoutliers function works on Matlab
%help center
function [cleaned_data, removed_values, iterations] = removeOutliers(data_in, removed_values_in, iteration_count) %output variables = input variables
% REMOVEOUTLIERS Recursively removes outliers based on +/- 2 standard deviations.
    current_data = data_in(:); 
    iteration_count = iteration_count + 1; %for each loop around add one to the iteration count

    %Calculate current mean and standard deviation
    current_mean = mean(current_data);
    sd = std(current_data);
    
    %Define the outlier thresholds (mean +/- 2*SD)
    lower_bound = current_mean - 2 * sd;
    upper_bound = current_mean + 2 * sd;
    
    %Identify values within bounds
    inliers_mask = (current_data >= lower_bound) & (current_data <= upper_bound); %using a boolean mask to identify value within bounds
    
    %Identify outliers
    outliers_mask = ~inliers_mask; %inverse for outliers, only reason for doing it like this is that it seems easier to figure out how to extract good values
    
    %Extract the data that falls within the bounds
    next_data = current_data(inliers_mask);
    
    %Save the outliers found in this round
    current_outliers = current_data(outliers_mask);
    removed_values_in = [removed_values_in; current_outliers];
    
    %Check to see if the size hasn't changed, if so, we are done
    if length(next_data) == length(current_data)
        %no more outliers removed therefore all within bounds
        cleaned_data = current_data;
        removed_values = removed_values_in;
        iterations = iteration_count;
        return; % Exit the function
    else
        %Call the function again with the cleaned data
        [cleaned_data, removed_values, iterations] = removeOutliersRecursive(next_data, removed_values_in, iteration_count);
    end

end



