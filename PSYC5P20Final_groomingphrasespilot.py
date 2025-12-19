#Pilot study to determine how long phrases are
#Goal for phrases to be around same length
#There does not seem to be any phrases that are consistently longer to read
from psychopy import visual, core, event, data
win = visual.Window([800, 600], fullscr=False, monitor="testMonitor", units="deg")

fixation_cross = visual.TextStim(win, text='+', height=0.5)
fixation_cross.draw()
win.flip()
core.wait(0.5)

#Victim selection
print (f"Victim Selection:")
message = visual.TextStim(win, text = 'An adult likes the child because the child is trusting', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

message = visual.TextStim(win, text = 'An adult likes the child because the child has low confidence', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")


message = visual.TextStim(win, text = 'An adult likes the child because the child is pretty', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

#Gaining access and isolation
print (f"Gaining access and isolation:")
message = visual.TextStim(win, text = 'An adult takes a child to an isolated room', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

message = visual.TextStim(win, text = 'An adult gains the trust of family to spend time with a child', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")


message = visual.TextStim(win, text = 'An adult plans an overnight trip with the child', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

#Trust development
print (f"Trust development:")
message = visual.TextStim(win, text = 'An adult says they have a special relationship with the child', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

message = visual.TextStim(win, text = 'An adult gives the child presents', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")


message = visual.TextStim(win, text = 'An adult plays games with the child', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

#Desensitization
print (f"Desensitization:")
message = visual.TextStim(win, text = 'An adult asks a child about their sexual experiences', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

message = visual.TextStim(win, text = 'An adult tells the child inappropriate jokes', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")


message = visual.TextStim(win, text = 'An adult rubs the child’s back', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

#Post-Abuse maintenance
print (f"Post abuse maintenance:")
message = visual.TextStim(win, text = 'An adult encourages secrets with a child', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

message = visual.TextStim(win, text = 'An adult tells the child they can’t be friends anymore', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")


message = visual.TextStim(win, text = 'An adult rewards secrecy with a child', height=0.4)
message.draw()
win.flip()
event.waitKeys()

resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}")

# --- End Experiment ---
win.close()
core.quit()
