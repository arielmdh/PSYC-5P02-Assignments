from psychopy import visual, core #need to import first
win = visual.Window([400,400]) #denoting a window, what size
message = visual.TextStim(win, text = '') #define what message is, its visual, in the window, text is "hello", can also define font, colour, size, pos etc.
message2 = visual.TextStim(win, text = 'world', pos = (-0.5, -0.5))#object is an instance of a class

#message.autoDraw = True #keep drawing until telling it to turn off 

timer = core.Clock() #create clock, timer is instance of clock
mouse = event.Mouse(visable=True)
x = 0.0
y = 0.0

startTime = timer.getTime()

while timer.getTime() - startTime < 20.0: #create while loop, is the current time (timer.getTime) minus the startTime is less than 2 seconds, keep looping through code. Updated position of message every loop
    #x = mouse.getPos()[0] #calling mouse get postion, [0], first position, indexing
    #y = mouse.getPos()[1]
    pos = mouse.getPos()
    #x += 0.01
    #y += 0.01
    message.pos = (pos[0],pos[1])
    message.draw()
    win.flip()
    
win.flip() #putting on the window from back buffer
core.wait(2.0)

message.autoDraw = False
message2.autoDraw = True
win.flip()
core.wait(2.0)