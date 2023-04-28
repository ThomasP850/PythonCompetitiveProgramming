
# **Where is My /water?**
Your boss, a.k.a. Lazy Larry, is always trying to find the simplest way to get every task done. For the past
week, he has been complaining about how much effort it takes to move between file folders on his
computer. So, he’s made it your job to write him a utility program that will determine the least number
of mouse clicks he should need to get from his current directory to another directory of interest.

You realize that in the simplest case, a graphical representation of the directory structure would be a
simple tree like that pictured above. Given two directory paths, e.g. C:/this/is/where/you/start/ and
C:/where/is/my/water/, the problem could be solved by finding the longest partial path shared by the
files (in this case C:/) and then counting the number of back clicks to that point from the starting folder
(5) and forward clicks down to the destination (4) to get the total number required (9).

But, Lazy Larry, being who he is, has complicated the problem by putting shortcuts within some
directories that, if used, might make getting to the destination directory possible in fewer clicks. For
example, if there is a shortcut [C:/this/is/] in the start folder, then it is shorter to take one click into the
start folder, follow the shortcut (saving one click), and then proceeding as above for a total of 8 clicks.

## **Details of the input**
Folder names will be complete paths starting from the root of the C:/ drive. That is,

&emsp; *C:/s1/s2/…/sx/*

where each of s1, s2, ..., sx is the name of a subfolder. A subfolder name is a simple alphanumeric string
(i.e., no special characters) followed by a slash (*/*). The final of these names, *sx/*, may be replaced by the
name of a shortcut to another folder. A shortcut will appear as a complete path enclosed in square
brackets. That is, [*C:/s1/s2/…/sx/*]. Shortcuts may not contain other shortcuts.

### **Input to the program will be as follows:**

 - The first line is a single integer, *n*, which specifies the number of folder paths that follow.
 - Each of the next *n* lines will contain a single string, *p*, which specifies a path to a folder or shortcut.
 - The next line is a single integer, *m*, which specifies the number of test cases that will follow.
 - Each of the next *m* lines will contain a single string, *d*, which specifies a starting folder.

There will be no input for the destination folder of each case. It is defined to be *C:/where/is/my/water/*.

### **Details of the output**
For each test case, output should begin with the line “Case i:” where i is the corresponding case number.
That should be followed by a single space and the minimum number of clicks for that case.

#### **Sample input**
```
11  
C:/  
C:/where/  
C:/where /is/  
C:/where/is/my/  
C:/where/is/my/water/  
C:/this/  
C:/this/is/  
C:/this/is/where/  
C:/this/is/where/you/  
C:/this/is/where/you/start/  
C:/this/is/where/you/start/[C:/this/is/]  
2  
C:/this/  
C:/where/is/my/water/  
```
#### **Sample output**
```
Case 1: 5  
Case 2: 0
```