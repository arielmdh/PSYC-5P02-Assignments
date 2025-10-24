from psychopy import visual, core, event, data, gui
import numpy as np
import random
import os

#experiment name and dialogue box
expName = 'visual_search' #name experiment
expInfo = {'participant': '', 'trials_per_condition': 5} #defining what I want in a dialogue box
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) #Found more info about this in "experiment setting" in Psychopy.org

#Add on #7 Saving file
filename = 'data/%s_%s_%s' % (expInfo['participant'], expName, data.getDateStr())
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
#Used the article "psychopy.data" on Psychopy.org to learn about the experiment handler as a way to save files
#Defining experiment parameters
# Define set sizes
set_sizes = [8, 12, 14] #Add on #3, defining three different set size options
# Define response keys
resp_keys = ['right', 'left'] #Add on #1, defining the arrow keys as the response I'm looking for
# Define stimulus rotations
rotations = [0, 90, 180, 270] #Add on #5, adding differing rotations, although I can't figure out how to apply to only distractors
# Timeout for trial
trial_timeout = 1.0 #Add on #9, seems super fast!

# Set up window, just like class exercise
win = visual.Window(
    size=[900, 900], fullscr=False, screen=0,
    monitor='testMonitor', color=['black'], colorSpace='rgb',
    blendMode='avg', units='height')

#Add on #8, adding beginning instructions
def show_instructions():
    instruction_text = visual.TextStim(win=win, name='instruction_text',#Used some markdown style notation to make this multiple paragraphs so you can actually see all the instructions at once
                                       text='Welcome!\n\n'
                                            'In this experiement, you will determine if the target letter "T" is present.\n\n'
                                            'If the letter "T" is present, press the right arrow key.\n'
                                            'If the letter "T" is NOT present, press the left arrow key.\n\n'
                                            'Try to respond as quickly and accurately as possible.\n'
                                            'Press any key to begin the practice trials.',
                                       pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                       color='white', colorSpace='rgb')
    instruction_text.draw()
    win.flip()
    event.waitKeys() #Used psychopy.event website for help with waitKeys

#Set up practice
def run_practice(): #define a function for a practice run
    practice_text = visual.TextStim(win=win, name='practice_text',
                                    text='Practice Trials. Press any key to continue.',
                                    pos=(0, 0), height=0.05)
    practice_text.draw()
    win.flip()
    event.waitKeys()
    
    # 3 practice trials
    for i in range(3):
        present = random.choice([True, False])
        set_size = 8 #didn't randomize set size for this
        run_trial(present, set_size, is_practice=True)

#Experimental run!

def run_trial(target_present, set_size, is_practice=False):


    #Randomize positions
    positions = [] #I initally just had a series of positions like (1,0) but then all the letters would be on top of eachother, then I tried a grid and couldn't figure that out and ended up doing this which I definitely think is more complicated than all the other ways to do it but nothing else worked for me
    radius = 0.4 #Anyway, this is a really confusing way to do these, found through numpy constants and stack overflow forums
    for i in range(set_size):
        angle = (2 * np.pi / set_size) * i
        x_pos = radius * np.cos(angle)
        y_pos = radius * np.sin(angle)
        positions.append((x_pos, y_pos))
    random.shuffle(positions)

    # Generating the stim
    stimuli = [] #create list for stimuli
    if target_present: #if the target is present, present at random position
        # Create target 'T'
        target_pos = random.choice(positions)
        target = visual.TextStim(win, text='T', pos=target_pos, height=0.08, ori=random.choice(rotations))
        stimuli.append(target)
        
        # Create distractors 'L'
        distractor_positions = [pos for pos in positions if pos != target_pos] #create new list for distractor positions, excludes elements equal to the target position
        for pos in distractor_positions: #discovered the pos for pos in through the psychopy online forum, someone asking what this phase means
            distractor = visual.TextStim(win, text='L', pos=pos, height=0.08, ori=random.choice(rotations))
            stimuli.append(distractor)
    else:
        # No target, only distractors, if no target, do all distractors, Addressing add on #4
        for pos in positions:
            distractor = visual.TextStim(win, text='L', pos=pos, height=0.08, ori=random.choice(rotations))
            stimuli.append(distractor)
    
    #Present stimuli!
    for stim in stimuli:
        stim.draw()
    win.flip()
    #waiting for keyboard response Add on #1
    resp_clock = core.Clock()
    keys = event.waitKeys(keyList=resp_keys + ['escape'], maxWait=trial_timeout, timeStamped=resp_clock)
    
    #How response should be processing
    if not keys: #if they dont select any key, timeout, add on #9
        response_info = {'response': 'timeout', 'rt': np.nan, 'accuracy': False}
    else:
        key, rt = keys[0] #adding escape key in case they want to quit, add on #2
        if key == 'escape':
            core.quit()
        
        # Determine correct answer and accuracy
        if target_present and key == 'right':
            accuracy = True
            corr_ans = 'right'
        elif not target_present and key == 'left':
            accuracy = True
            corr_ans = 'left'
        else:
            accuracy = False
            corr_ans = 'right' if target_present else 'left'
        
        response_info = {'response': key, 'rt': rt, 'accuracy': accuracy, 'correct_ans': corr_ans}
    
    # Provide feedback, add on #10
    if not is_practice:
        feedback_text = ''
        if response_info['response'] == 'timeout':
            feedback_text = 'Too slow!'
        elif response_info['accuracy']:
            feedback_text = 'Yippee!'
        else:
            feedback_text = 'Noooo'
        
        feedback_stim = visual.TextStim(win, text=feedback_text, height=0.07, color='purple')
        feedback_stim.draw()
        win.flip()
        core.wait(0.5)
    
    return response_info

#Experiment cycle
def main_experiment(): #Order of presentation, instructions, then show practice trials
    show_instructions()
    run_practice()
    
    # Loop through each set size
    for set_size in set_sizes: 
        # Define condition list for the loop
        condition_list = [{'set_size': set_size, 'target_present': i % 2 == 0} 
                          for i in range(expInfo['trials_per_condition'] * 2)]
        random.shuffle(condition_list) #randomize condition
        
        for condition in condition_list:
            response_data = run_trial(condition['target_present'], condition['set_size'])
            
            # Save everything, add on #7, more experiment handler type stuff, learning how to save all this stuff as my file name, super cool
            thisExp.addData('set_size', condition['set_size'])
            thisExp.addData('target_present', condition['target_present'])
            thisExp.addData('response', response_data['response'])
            thisExp.addData('RT', response_data['rt'])
            thisExp.addData('accuracy', response_data['accuracy'])
            thisExp.nextEntry()

    thisExp.saveAsWideText(fileName=filename + '.csv', appendFile=False)
    thisExp.close()

    end_message = visual.TextStim(win, text="Thank you for participating!", height=0.05) #Final message!
    end_message.draw()
    win.flip()
    core.wait(2.0)
    win.close()
    core.quit()
    
resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}") #Print reaction time
# Run the experiment
if __name__ == "__main__":
    main_experiment()
