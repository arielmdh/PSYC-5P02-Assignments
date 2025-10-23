#Question 6
from psychopy import visual, core, event, data
win = visual.Window([800, 600], fullscr=False, monitor="testMonitor", units="deg")

fixation_cross = visual.TextStim(win, text='+', height=0.5)
fixation_cross.draw()
win.flip()
core.wait(0.5)

message = visual.TextStim(win, text = 'Go!', color='green')
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
