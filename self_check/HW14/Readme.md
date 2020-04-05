# HW14

## 14_1
(Difficulty: ★★☆☆☆) Write a command-line program named dehtml.py to remove tags from an HTML file and write the file into a plain text file.

Background: HTML, for Hypertext Markup Language, is the way web pages are formatted.  It contains tags in the form of of angle bracketed tags. 
The purpose of dehtml.py is to take out these angle-bracketed tags (i.e., formatting) and leave just the original text.

You can test your code with any web page that is saved as an HTML file and name it with the extension of ".html" (e.g., myweb.html). 

Your program should open the file specified on the command line.  It should check to make sure the file name is named with ".html" extension.  If it can be opened, it should write the output into a file whose name is the same as the HTML file except the ".html" suffix is replaced with a ".txt" suffix.  For example,
$ python3 dehtml.py myweb
Error: File name should have .html suffix
$ python3 dehtml.py myweb.html
Wrote file myweb.txt
$ 
If successful, it creates a file named myweb.txt without the HTML tags.

Hint: use **regular expressions** to specify the tags so they can be split.
You may replace each tag with a blank space.


## 14_bonus
(Difficulty: ★★★★☆)  Write a Tkinter version of the postfix calculator for dates (from the previous assignment).

The interface should look be divided into a left pane and a right pane.  The left pane contains buttons for the verbs: 'today', 'tomorrow', 'yesterday', 'add', 'sub', 'swap'.
It should also contain an Entry widget for text entry and a 'push' button.

The right pane should be a ListBox to show the content of the stack.  For simplicity, the stack grows "downward" so that the bottom of the stack is on the top side of the ListBox, and new items get pushed to below the last item.

In the Entry field, you may enter any valid Python expressions that can be pushed. You can also push buttons to enter instead.  Using the code from the previous assignment, you should be able to enter 
```
date(year, month, day)
days(d)
weeks(w)
months(m)
```
Hint: you may use the eval() function to convert from the text in the Entry into the corresponding Python data structure.  To be safe, you would want to allow access to only your date, days, weeks, and month classes but block out other symbols.  Note that the user could type in arbitrary code, but if an exception occurs during eval(), or if eval() does not return a valid type, then you may indicate error in the "error message here" (as a Label) shown in the example above.

The ListBox should display the same content as shown in the list returned by datecalc() function.  Unlike the word finder example, where the entire content is deleted before new content is added on every refresh, here you only need to remove the bottom entry for a pop, or append the new entry to the end for a push.

Hint: It may be easier if the ListBox only serves the display purpose instead of also working as the stack data structure.

