# HW6

## 6_1
Write a Python program named dateconv.py to prompt the user for date in US format of mm/dd/yyyy (e.g., '02/15/2019' and outputs it in the full format of 'February 15, 2019'.  You may assume the dates are given as decimal literals separated by '/', but you should also check if the dates are in range.  If the dates are out of range, then you should inform the user what is wrong. 

For instance
```
$ python3 dateconv.py
enter date in mm/dd/yyyy: 02/15/2019
February 15, 2019
enter date in mm/dd/yyyy: 02/29/2019
Invalidate day 29 for February: not a leap year
enter date in mm/dd/yyyy: 01/01/2001
January 1, 2001
enter date in mm/dd/yyyy: 13/10/2038
Invalid month 13: should be between 01 and 12
enter date in mm/dd/yyyy: 10/32/2019
Invalid day for October: should be between 01..31
enter date in mm/dd/yyyy: 04/31/2019
Invalid day for April: should be between 01..30
enter date in mm/dd/yyyy: quit
bye
$ _
```

Hint: Build up your program one piece at a time.  First, simply use a loop to prompt for input and check for 'quit'.  If not quit then first use a print statement to check if the input is as you expect.  Once confirmed, you can use str's split() method to split a string by its separator ('/' in this case).  Then, you can check the array of strings, assuming you can convert them to int, and check if each one is within range.  Month can be checked easily.  Day depends on the month, and for the month of February, day also depends on whether the year is a leap year (28 or 29 days).  If any field is invalid, then report the error and loop again.  If all fields are correct then  display the full month string.
You may store the names of the months all in a list indexed by the month number or in a dictionary keyed by the month.  You may use the leap year function from a previous lecture.

## 6_2
[somewhat challenging]  Write a Python program named long_multiply(a, b) to return a string that shows the steps in a long multiplication.  (note: a is called the multiplier, and b is the multiplicand) For example
```
>>> print(long_multiply(12, 34))
  12
x)34
----
  48
 36 
----
 408
```
Hint:  You should construct the return value of the function by concatenating different strings together.  It is probably easier if you just append the strings into a list and join them by '\n'.join(listOfStrings).
a)	Before you join the strings, you need to determine the width to format each line.  This is the maximum number of characters needed to represent the multiplier, multiplicand + 2 (because 'x)' takes two positions), and the product.
b)	Create the following strings and append each one into a list:
i)	string for the multiplier with the width (right aligned), 
ii)	'x)' concatenated the multiplicand formatted with width-2 (also right-aligned),
iii)	string of '-' repeated for width times
iv)	loop over the partial products of multiplier * each digit of the multiplicand, but each time shifted one position to the left.
v)	anotherr string of '-' repeated for width times
vi)	finally, the product as a string, formatted to the same width, right aligned.
c)	finally, return '\n'.join( list of strings created in above steps )
Note: you may assume a and b are both nonnegative integers.  Your code should work with integers of any number of digits.


