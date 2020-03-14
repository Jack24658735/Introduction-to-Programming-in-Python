# HW4

## 4_1
Write a program that prompts the user to input two strings and reports the two strings' lengths, by reporting the shorter string first. But if they are of the same length then keep them in the original order.  

Example: 
```
$ python3 compstr.py
Enter a string: Great
Enter another string: job
Shorter string: job (length 3)
Longer string: Great (length 5)
$ python3 compstr.py
Enter a string: Mary
Enter another string: lamb
First string: Mary (length 4)
Second string: lamb (length 4)
$
```
Note that in case the strings are of different lengths, the program says Shorter and Longer, but in case the strings are of equal length, the program says First and Second.

## 4_2
Write a Python program named catn.py by modifying the template code to implement the unix utility command cat with -n option, which adds the line number in front of every line of a file.
a.	First version: support the command with optional -n flag and one file.  Note that the line number is formatted 
```
$ python3 catn.py mary.txt
Mary had a little lamb
little lamb, little lamb
Mary had a little lamb
its fleece was white as snow
$ python3 catn.py -n mary.txt
     1  Mary had a little lamb
     2  little lamb, little lamb
     3  Mary had a little lamb
     4  its fleece was white as snow
$ 
```
b.	Second version: handles one or more files with optional -n flag.  In case of multiple files, the line number restarts from 1.


