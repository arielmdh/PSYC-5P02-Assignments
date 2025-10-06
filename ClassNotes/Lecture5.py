#Lecture 5
from psychopy import visual, core #import psychophy library items visual and core
win = visual.Window([400,400]) #Creating window to draw onto , assign name to window and size, can set unit, i.e. 'pix' for pixels
message = visual.TextStim(win, text='hello') #draw a stim to back buffer, assign label (message), specify type of stim (visual), assign to window (win)
message.autoDraw = True #automatically draw every frame, refresh rate, most cases want autodraw
win.flip() #flip stimulus to the screen, doesn't appear until flip 
core.wait(2.0) #wait command to delay next event, everything stops until wait is over
message.text = 'world' #call message, modify text property to world
win.flip() #flip stimulus again
core.wait(2.0) #wait again
#CLASS EXERCISE
 info {} #a dictionary
#present dialog to collect info
  #Writing files
    #fileID = open(filename, 'w') w - write, x - open, a - append
    #fileID.write('format', vars)

info['participant'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()
        
    fileName = expInfo['observer'] + expInfo['dataStr']
    dataFile = open(fileName+'.csv','w')
    dataFile.write('targetSide, oriIncrement, correcct/n')

from psychopy import visual, event, core, data
import random
win = visual.Window([1024, 768], fullscr=False, units='pix')

respClock=core.Clock()



#initialize some stimuli
fixation = visual.Circle(win, size = 5, #in this case we set units to pixs so it will be 5 pixels tall
    lineColor = 'white', fillColor = 'LightGrey')
    
probe = visual.GratingStim(win, size = 80, # 'size' is 3xSD for gauss,
    pos = [300, 0],#we'll change this later
    tex = None, mask = 'gauss',
    color = 'green')
cue = visual.ShapeStim(win,
    vertices = [[-30, -20], [-30,20], [30,0]],
    lineColor = 'red', fillColor = 'salmon')
    
info = {} #a dictionary
info['fixTime'] = 0.5
info['cueTime'] = 0.2
info['probeTime'] = 0.2

side = [1,2]
orient = [1,2]


#run one trial
#run multiple trials

for trial in range(5):
    
    random.shuffle(side)
    random.shuffle(orient)

    fixation.draw ()
    win.flip()
    core.wait(info['fixTime'])
    
    if orient[0] == 1:
        cue.ori = 0
    else:
        cue.ori = 180
        
    cue.draw()
    win.flip()
    core.wait(info['cueTime'])
    
    if side[0] == 1:
        cue.ori = 0
    else:
        probe.pos = [30,0]


    fixation.draw()
    probe.draw()
    win.flip()
    #core.wait(info['probeTime']) no longer waiting
    respClock.reset()
    win.flip() #clear screen
    
    #look for keyboard response
    keys = event.waitKeys(keylist = ['left', 'right', 'escape']) #waiting for key response
    resp = keys[0]
    rt = respClock.getTime() #calculate reaction time
    
    #calculate accuracy
    
    if (resp == 'left' and side[0] == 2) or (resp == 'right' and side[0] ==1):
        corr = 1
    else:
        corr = 0
        
    #Track responses
    
    
   
    
    dataFile.write('%i,%.3f,%\n' %(targetSide, thisIncrement, thisResp))
    
dateFile.close()

#Imagestim
#Imagestim(win[,image,mask,units,pos,...])
#Image = path to image

#Audio
#Audioclip
#audio.audioclip 

#mouseinput
#psychopy.event (import event)

#Each one is a class, each has different attributes (for mouse, attributes:press, position)
