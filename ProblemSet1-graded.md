>[!IMPORTANT]
>Be sure to provide as many details as possible. Also, try to have all files for each assignment in separate folders. 

**Question 1:**
a) ```ls -rt```
b) ```ls -lrt```
c) Using the command ```ls``` allows the user to see what files are currently in your directory, adding ```-lrt``` to the command denotes viewing the files in long form, reverse, time order where you can view the files currently in your directory in reverse time order with the date and time lasted edited shown.

>[!NOTE]
>I wanted you to copy the actual description from the manual, but I will accept this.

:memo: **3/3**
 
**Question 2:**
a) ```cd``` b) ```cd ~/``` c) ```cd../```
> _a_ should be `cd /users/adh/` or something similar.

:memo: **2/3**


**Question 3:**
Step 1: ```mkdir Data```
Step 2: ```touch subj01.txt```
Step 3: 
```cp subj01.txt subj02.txt```
```cp subj01.txt subj03.txt```
```cp subj01.txt subj04.txt```
```cp subj01.txt subj05.txt```
```cp subj01.txt subj11.txt```
Step 4: ```mv subj*.txt Data```
Step 5: ```rm subj0*.txt```

:memo: **5/5**

**Question 4:**
The ```tee``` command allows a user to read input and write output while also copying the output to another file. I am aiming to look at the files in my current directory in longform and simultaneously copy the output to another file. Using the following code:
```ls -l | tee -a output.ls```
I can double check that the output is in the new file with the following code:
```vi output.ls```
There I can see that my output has been saved to a new file.

:memo: **3/3**


**Question 5:**
In the second screen, the command history is only of the current session whereas the command history in the main screeen is of all time.
>>In the first one it should include the past history

:memo: **3/3**

**Question 6:**
![This is a screenshot of my git](/PSYC-5P02-Assignments/Screenshotgit.png)

:memo: **3/3**

**Question 7:**
![This is a screenshot of my shell](/PSYC-5P02-Assignments/screenshotshell.png)

:memo: **3/3**


**Question 8:**
Instead of using the ```head``` command to take the first lines, however many you specify, you would use the ```tail``` command to take the last lines, however many you specify. Using a chevron ```>``` I will make the final file. 

:memo: **3/3**

:memo: **Total: 25/26**
