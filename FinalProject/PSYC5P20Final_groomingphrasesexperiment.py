#EXPERIMENT 1: Phrases
#The first experiment takes the pre-tested phrases and presents them
from psychopy import visual, core, data, gui
from psychopy.hardware import keyboard
import random, os

#Set up for data saving and allow input of participant info
#Create a dialog box for participant info
info = {'Participant ID': '', 'Session': '001'}
if not gui.DlgFromDict(dictionary=info, title='Grooming Phrase Study 2025').OK:
    core.quit() #set up same as previous experiment assignment

#File saving, help from psychopy.data - functions for storing/saving/analysing data, using experiment handler
filename = f"data/{info['Participant ID']}_{data.getDateStr()}" #set up saved name with inputed info
thisExp = data.ExperimentHandler(name='GroomingPhraseStudy', extraInfo=info, dataFileName=filename)

#Set up experiment window, size, colour, etc.
win = visual.Window([1000, 1000], fullscr=False, color="black", monitor="testMonitor", units="deg")

kb = keyboard.Keyboard() #set up to take keyboard response
stim_text = visual.TextStim(win, text="", color="pink", height=0.5) #set up stim text properties, pink for fun

#Phrases (15 Grooming, 5 Control)
#'right' = grooming 'left' = not groominig
trials_list = [ #set up list of phrases (make randomization easy)
    {'phrase': 'An adult likes a child because the child is trusting.', 'corr': 'right', 'grooming': 'yes'}, #enter the phrase, the correct answer and the condition
    {'phrase': 'An adult likes a child because the child has low confidence.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult likes a child because the child is pretty.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult takes a child to an isolated room.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult gains the trust of family to spend time with a child.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult plans an overnight trip with a child.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult says they have a special relationship with a child.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult gives a child presents.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult plays games with a child.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult asks a child about their sexual experiences.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult tells a child inappropriate jokes.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult rubs a child’s back.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult encourages secrets with a child.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult tells a child they can’t be friends anymore.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult rewards secrecy with a child.', 'corr': 'right', 'grooming': 'yes'},
    {'phrase': 'An adult helps a child if they have hurt themselves.', 'corr': 'left', 'grooming': 'no'},
    {'phrase': 'An adult takes a child to the busy playground.', 'corr': 'left', 'grooming': 'no'},
    {'phrase': 'An adult enjoys working with children.', 'corr': 'left', 'grooming': 'no'},
    {'phrase': 'An adult scolds a child for swearing.', 'corr': 'left', 'grooming': 'no'},
    {'phrase': 'An adult attends a childs birthday party.', 'corr': 'left', 'grooming': 'no'}
]
random.shuffle(trials_list)  # Randomized phrases

#Display the instructions
instr_msg = (
    "Welcome!\n\n"
    "In this experiment, you will read a phrase describing a behaviour and determine if that behaviour is grooming or not.\n\n"
    "Press RIGHT ARROW for grooming behaviours.\n"
    "Press LEFT ARROW for non-grooming behaviours.\n"
    "Press ESCAPE key at any time to end the experiment early.\n"
    "Please answer as quickly and accurately as possible.\n\n"
    "Ready? Press any key to start."
)
visual.TextStim(win, text=instr_msg, color='pink', height=0.5).draw()
win.flip()
kb.waitKeys() #wait until key is pressed

#Actual trial loop
print(f"\n{'Phrase':<30} | {'RT (s)':<8} | {'Correct'}") #for displaying information in the output


for trial in trials_list:
    stim_text.text = trial['phrase']
    stim_text.draw()
    win.flip()
    
    # Precise Timing Reset
    kb.clock.reset() 
    keys = kb.waitKeys(keyList=['left', 'right', 'escape'])
    
    # Handle Escape and Processing
    resp = keys[0]
    if resp.name == 'escape':
        break
        
    is_correct = 1 if resp.name == trial['corr'] else 0
    
    # Console Output (Live Print)
    print(f"{trial['phrase'][:28]:<30} | {resp.rt:.3f}    | {bool(is_correct)}")
    
    # Store Data to ExperimentHandler
    thisExp.addData('phrase', trial['phrase'])
    thisExp.addData('grooming', trial['grooming'])
    thisExp.addData('response_key', resp.name)
    thisExp.addData('rt', resp.rt)
    thisExp.addData('accuracy', is_correct)
    thisExp.nextEntry()  # Move to the next row in the data file
    
    # Brief Inter-trial Blank Screen
    win.flip()
    core.wait(0.5)

# 6. Save and Shutdown
# New 2025 naming conventions apply automatically via dataFileName
thisExp.saveAsWideText(filename + ".csv") 
print(f"\nExperiment complete. Data saved to: {filename}.csv")
win.close()
core.quit()