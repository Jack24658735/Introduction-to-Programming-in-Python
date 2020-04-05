# HW9

## 9_1
(Difficulty: ★★☆☆☆) Write a function that computes Pascal's triangle. 
```
Col:  0  1  2  3  4  5... 
Row0: 1
Row1: 1  1
Row2: 1  2  1
Row3: 1  3  3  1
Row4: 1  4  6  4  1
Row5: 1  5 10 10  5  1
```

The function should have the following call signature:
def pascal(row, column):
The function can be defined recursively as follows:
```
pascal(row, col) = {	1	if col = 0 or col = row
	??	if 0 < col < row
 ```
Fill in the ?? above and write this as a recursive function.  You may also check the range of the parameter values.  If out of range then it should raise a ValueError exception.

Then, write a function print_Pascal_triangle(n) to print out the triangle as above.  The parameter n indicates the number of rows.


## 9_2
(Difficulty: ★★★☆☆) Generalize the recursive finding function rec_find() from the recursion slides #22 so that you can pass either a value to be compared for equality, or you can pass a plug-in function that defines the matching criterion.  You can check if  val parameter is a plug-in function by calling the built-in function
callable(val)
which returns True if val is a function object or a lambda expression, or returns False if it is a value (assumed to be int).
For instance, you would called the revised rec_find as follows:
```
>>> L = [1, -2, [3, 4], 5]
>>> rec_find(L, 3)
(2, 0)
>>> rec_find(L, lambda x: x == 3)  # alternative way
(2, 0)
>>> rec_find(L, lambda x: x < 0)  # finds -2 at L[1]
(1,)
```

You need to generate test cases both in terms of different L and val (as int values, lambda expressions, and the expected answers in a list (or tuple).  Use a loop to invoke rec_find with these test values and use assert to check if the answer is as expected.

## 9_3
3.	(Difficulty: ★★★★☆) Rewrite the number_outline() function from the recursion slides #28 so that instead of concatenating the section numbers together by '.', it lets the user specify a plug-in function that defines the format, or use the default formatting.  For example,
```
L=['Intro',
      ['Motivation', 'Contributions'],
   'Related Work',
      ['By Author', 'By Subject'],
   'Technical Approach',
      ['Overview',
         ['Block Diagram', 'Schematic'],
       'Algorithm',
         ['Static', 'Dynamic'] ],
   'Conclusions']
```

Assume you have different formatting functions defined, 
```
>>> number_outline(L, my_outline_format_function)
I. Introduction
  A. Motivation
  B. Contributions
II. Related Work
  A. By Author
  B. By Subject
III. Technical Approach
  A. Overview
    1. Block Diagram
    2. Schematic
  B. Algorithm
    1. Static
    2. Dynamic
IV. Conclusions
```

And you can plug in another function for a different format:
```
>>> number_outline(L, my_thesis_format_function)
Chapter 1. Introduction
  Section 1.1 Motivation
  Section 1.2 Contributions
Chapter 2. Related Work
  Section 2.1 By Author
  Section 2.2 By Subject
Chapter 3. Technical Approach
  Section 3.1 Overview
    3.1.1 Block Diagram
    3.1.2 Schematic
  Section 3.2 Algorithm
    3.2.1 Static
    3.2.2 Dynamic
Chapter 4. Conclusions
```

Hints:
a.	How should the parameter list for the function be revised to accommodate the plug-in function?  Should it have a default value?
b.	How does your revised number_outline() function decide whether to use default formatting or to call the plug-in function for formatting?
c.	What parameter(s) should be passed to the plug-in function?  Hint: it is best if the plug-in function just returns the formatted string instead of calling print directly.
d.	What adjustments are needed when number_outline() makes a recursive call?


