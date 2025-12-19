#EXPERIMENT 2: Images
#Ideally, one would take their own photos for something like this to improve consistency in images, I was just interested in setting up an experiment like this to see how it would work
#I used what stock images I could find to illustrate some grooming behaviours, I couldn't find many that worked so again ideally you would have many more
#But this is at least a potential set up for using images and collecting rts and accuracy in identifying behaviours
#Similar with phrases, this experiment presents an image, collects rts and accuracy, and saves the file. 
from psychopy import visual, core, data, gui
from psychopy.hardware import keyboard
import random, os

#Initial set up basically the same as experiment 1
info = {'Participant ID': '', 'Session': '001'}
if not gui.DlgFromDict(dictionary=info, title='Grooming Image Study 2025').OK:
    core.quit()

#Saving file, changing name to grooming image study
filename = f"data/{info['Participant ID']}_{data.getDateStr()}"
thisExp = data.ExperimentHandler(name='GroomingImageStudy', extraInfo=info, dataFileName=filename)

#initializing window, made this one full screen, keyboard response, and image set up
win = visual.Window(fullscr=True, color="black", units="height")
kb = keyboard.Keyboard()
img_stim = visual.ImageStim(win, size=(0.6, 0.4)) #played around a little with aspect ratio but this is standard landscape size

#Defining stims (11 Images, 9 grooming, 2 control)
# 'right' = grooming, 'left' = not grooming
trials_list = [
    {'img': 'img_bribe.png', 'type': 'grooming', 'corr': 'right'}, #images are set up based on them being in directory, so might not work if images are not in directory
    {'img': 'img_enteringspace.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_giftgiving.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_luring.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_playgroundisolation.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_rubback.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_secret.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_threaten.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_tickling.png', 'type': 'grooming', 'corr': 'right'},
    {'img': 'img_control1.png', 'type': 'control', 'corr': 'left'},
    {'img': 'img_control2.png', 'type': 'control', 'corr': 'left'},
]
random.shuffle(trials_list) #randomize appearance order

#display instructions
instr_msg = (
    "Welcome!\n\n"
    "In this experiment, you will see an image featuring an adult and child interacting, you must determine if that behaviour is grooming or not.\n\n"
    "Press RIGHT ARROW for grooming behaviours.\n"
    "Press LEFT ARROW for non-grooming behaviours.\n"
    "Press ESCAPE key at any time to end the experiment early.\n"
    "Please answer as quickly and accurately as possible.\n\n"
    "Ready? Press any key to start."
)
visual.TextStim(win, text=instr_msg, color='blue', height=0.05).draw() #this one is blue for fun
win.flip()
kb.waitKeys()

#organizing info to output with titles
print(f"\n{'Image':<15} | {'RT (s)':<8} | {'Correct'}")

for trial in trials_list: #using for loop again for displaying images
    #prepare and show image, simnilar to how text set up, help from coder-show images on psychopy.org
    img_stim.image = trial['img']
    img_stim.draw()
    win.flip()
    

    #reset with key response for accurate rts and accepted key responses
    kb.clock.reset() 
    keys = kb.waitKeys(keyList=['left', 'right', 'escape'])
    
    
    #escape key for exit
    resp = keys[0]
    if resp.name == 'escape':
        break
        
    
    is_correct = 1 if resp.name == trial['corr'] else 0

 # Print results to console immediately
    print(f"{trial['img']:<15} | {resp.rt:.3f}    | {bool(is_correct)}") #using previously identified correct answer to print accuracy to output
    
    #saving trial data to file
    thisExp.addData('image_file', trial['img'])
    thisExp.addData('type', trial['type'])
    thisExp.addData('response', resp.name)
    thisExp.addData('rt', resp.rt)
    thisExp.addData('accuracy', is_correct)
    

#final save of file 
thisExp.saveAsWideText(filename + ".csv") #set up final filename
print(f"\nSaved to: {filename}.csv") #print that experiment finished and what the name is
win.close()
core.quit() #done!