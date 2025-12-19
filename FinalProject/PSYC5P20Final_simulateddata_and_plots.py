#With the experiments designed, I'm moving on to simulating the data
#Simulated data for grooming phrases experiment (EXPERIMENT 1)
import numpy as np #using numpy and pandas for simulate data
import pandas as pd

#Decided to simulate 50 participants that each went through each trial
n_participants = 50
n_grooming = 15 #setting up conditions, had 15 grooming phrases and 5 control phrases
n_control = 5
sd_rt = 0.080  # setting up a normal standard deviations, chose 80ms variability

#Based on my previous research, it generally found that participants tend to find grooming behaviours easier to identify, so assumption is they would be faster in grooming condition compared to control
#For accuracy, participants tend to be pretty accurate at identifying grooming behaviours, but feel unsure about control behaviours, so assumption for higher accuracy in grooming condition compared to control
# Condition targets
RT_grooming = 0.450  # 450ms, slightly faster in grooming condition
RT_control  = 0.600  # 600ms, slower for control
accuracy_grooming = 0.80  # based on previous research, setting mean accuracy for identifying grooming at around 80%
accuracy_control  = 0.60  #based on previous research, setting mean accuracy for identifying control behaviours slightly worse around 60%

data = [] #set up variable to put data into

#actually generating data using a for loop
for participant_id in range(1, n_participants + 1): #setting up ids to increase with each participant
    part_str = f'part-{participant_id:02d}'
    
    #grooming trials created using random generator(faster rt, higher accuracy)
    rts_g = np.random.normal(RT_grooming, sd_rt, n_grooming).clip(0.200) # clipped at a mininum reaction time, nobody reading faster than that
    acc_g = np.random.binomial(1, accuracy_grooming, n_grooming)
    for r, a in zip(rts_g, acc_g):#zip function for aggregating element from accuracy and reaction time
        data.append({'Participant': part_str, 'TrialType': 'Grooming', 'RT': r, 'Accuracy': a}) #append data for adding titles
        
    #control trials (slower rts, lower accuracy)
    rts_c = np.random.normal(RT_control, sd_rt, n_control).clip(0.200) #again clipping at low end of reaction time
    acc_c = np.random.binomial(1, accuracy_control, n_control)
    for r, a in zip(rts_c, acc_c):
        data.append({'Participant': part_str, 'TrialType': 'Control', 'RT': r, 'Accuracy': a})

df = pd.DataFrame(data) #make dataframe

#Dataframe of simulated data has now been created, we're not moving on to plotting a graph
#I've decided to plot the means for each condition, using help from seaborn barplot on seaborn.pydata.org and YouTude "Seaborn bar plot tutorial" Kimberly fessel for refresher on how to make them
import matplotlib.pyplot as plt
import seaborn as sns

#calculating means for plots, using groupby function, store results in new dataframe
part_means = df.groupby(['Participant', 'TrialType']).agg({'RT': 'mean', 'Accuracy': 'mean'}).reset_index()

#setting up plots with sizes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6)) #Set up for two plots next to eachother

#plot 1:reaction time
sns.barplot(data=part_means, x='TrialType', y='RT', ax=ax1, palette='mako', capsize=.1) #set up plot axis and chose palette from seaborn
ax1.axhline(RT_grooming, color='blue', alpha=0.5) #setting up colours and lines for comparisons
ax1.axhline(RT_control, color='red', alpha=0.5)
ax1.set_title('Mean Reaction Time by Condition') #setting titles
ax1.set_ylabel('RT (seconds)')


#plot 2: accuracy
sns.barplot(data=part_means, x='TrialType', y='Accuracy', ax=ax2, palette='rocket', capsize=.1) #chose different seaborn palette, setting up data to use, and x and y axis
ax2.axhline(accuracy_grooming, color='blue', alpha=0.5) #colors, comparisons
ax2.axhline(accuracy_control, color='red', alpha=0.5)
ax2.set_title('Mean Accuracy by Condition') #setting titles
ax2.set_ylabel('Proportion Correct')
ax2.set_ylim(0, 1) #limit

plt.tight_layout()
plt.show()

#Simulating data and plotting graphs for phrase experiment complete
#Now moving on to simulating data for images experiment (EXPERIMENT 2) and plotting graph of means for that

#I set this up essentially the same as the first experiment
n_participants_img = 50
n_grooming_img = 9
n_control_img = 2
total_trials_img = n_grooming_img + n_control_img

mean_rt_img = 0.800   #Based on assumptions from previous data, reaction times might be the same between conditions
sd_rt_img = 0.150     # Standard deviation of 150ms
acc_groom_img = 0.60  #based on assumptions that the images will be difficult to identify, assuming 60% accuracy
acc_ctrl_img = 0.50   #based on assumption that identifying control conditions will be around chance

data = []

#generating data using for loop
for part_id_img in range(1, n_participants_img + 1):
    part_str_img = f'part-{part_id_img:02d}'
    
    #adding in grooming trials
    rts_g_img = np.random.normal(mean_rt_img, sd_rt_img, n_grooming_img).clip(0.200) # Clipped at 200ms
    acc_g_img = np.random.binomial(1, acc_groom_img, n_grooming_img)
    for r, a in zip(rts_g_img, acc_g_img):
        data.append({'Subject': part_str_img, 'TrialType': 'Grooming', 'RT': r, 'Accuracy': a})
        
    #adding control trials
    rts_c_img = np.random.normal(mean_rt_img, sd_rt_img, n_control_img).clip(0.200)
    acc_c_img = np.random.binomial(1, acc_ctrl_img, n_control_img)
    for r, a in zip(rts_c_img, acc_c_img):
        data.append({'Subject': part_str_img, 'TrialType': 'Control', 'RT': r, 'Accuracy': a})

df_img = pd.DataFrame(data)

#Now moving on to plots for this simulated data

#calculating means using groupby, aggregating data
part_means_img = df.groupby(['Subject', 'TrialType']).agg({'RT': 'mean', 'Accuracy': 'mean'}).reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

#plot 1: Reaction Time by Condition
sns.barplot(data=part_means_img, x='TrialType', y='RT', ax=ax1, palette='coolwarm', capsize=.1)
ax1.axhline(mean_rt_img, color='red')
ax1.set_title('Mean Reaction Time by Condition')
ax1.set_ylabel('RT (seconds)')
ax1.set_ylim(0, 1.2)

# plot 2: Accuracy by Condition
sns.barplot(data=part_means_img, x='TrialType', y='Accuracy', ax=ax2, palette='viridis', capsize=.1)
ax2.axhline(acc_groom_img, color='blue', alpha=0.5)
ax2.axhline(acc_ctrl_img, color='green', alpha=0.5)
ax2.set_title('Mean Accuracy by Condition')
ax2.set_ylabel('Proportion Correct')
ax2.set_ylim(0, 1)

plt.tight_layout()
plt.show()

#print out of means
print(df.groupby('TrialType')[['RT', 'Accuracy']].mean())