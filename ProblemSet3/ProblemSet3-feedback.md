# PSYC 5P02- Introduction to Programming for Psychology
## Fall 2025

### Problem Set #3

### Rubric:
* Accuracy & Efficiency: 50%
* Explanation and documentation: 50%

--- 
###  Feedback:

* Great use of (nested) functions! 
* Would like a few more comments about new solutions, like how the ExperimentHandler works, and how the code defining the locations along a circle works. 
* * The `waitKeys()` method you used works fine, although it pauses the experiment, so if you had other things you wanted to do while waiting for a response you would want to use the `getKeys()` method and put it in a loop.
* You could combine your logicals when checking for correct responses, such as `if (target_present and key == 'right') or (not target_present and key == 'left'):`
* not sure if you need the variable `corr_ans`. I think I guess you're trying to save what the correct answer was, and not the response they made, but that could also be easily obtained by saving the response and the condition? 
* The code writes two files. It's not entirely clear to me why, but that's the kind of thing that should make you wonder if you've organized your code properly 
* Set sizes aren't randomized, but are blocked. Could be situations where you don't want to have this. Is there a way to make it truly random?
* This code here:
> `resp_clock = core.Clock()
keys = event.waitKeys(timeStamped=resp_clock)
rt = resp_clock.getTime()
print (f"RT: {rt:.3f}") #Print reaction time`

This is called before you run the experiment, so the window opens and then needs a response (but it isn't clear that's the case). The RT printed to the terminal is just the RT from that one keyboard response. THEN the experiment actually starts.

* It's not clear to me what this code is doing:
 > `if __name__ == "__main__":
    main_experiment()`

Needs to be better documented!
* I also would have liked to have seen the experiment/trial handler better explained so it's clear to me you understand how it works. * **Overall:** Generally speaking very good. Managed to accomplish most of what I asked. Were able to use functions usefully. Good use of global variables. A few small things that could lead to bugs/gremlins but works good. There are a few things I would like better documented (e.g., how. you are using the Experiment Handler to write data), since we didn't cover it in class. 
* 

**Accuracy & Efficiency:** 22/25
**Explanation and documentation:** 23/25
**Total:** 45/50
