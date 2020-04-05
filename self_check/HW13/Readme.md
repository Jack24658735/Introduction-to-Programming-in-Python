# HW13

## 13_1
1.	(Difficulty: ★★☆☆☆) Write a "rock, paper, scissors" game using the random module.

$ python3 rps.py
rock, paper, scissors? rock
I am also rock - tied!
rock, paper, scissors? paper
I am rock - I lose!
rock, paper, scissors? scissors
I am rock - you lose!
rock, paper, scissors? rabbit
rabbit is invalid - try again? quit
bye
$ 


## 13_2
(Difficulty: ★★★☆☆) Define a Matrix class to represent numbers as a two-dimensional array.

The constructor for the matrix is a list of lists of numbers.  A 3x3 matrix
1	2	3
4	5	6
7	8	9
would be constructed as
M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

Define the following methods
```
class Matrix:
    def __init__(self, data):
        # data is the list of lists of value

    def row(self, r):
        # return the r-th row in the form of a list
        # r is from 0.. number of rows
        # in the exmaple above, M.row(1) would return
        # [4, 5, 6]

    def column(self, c):
        # retun a the c-th column in the form of a list.
        # in the example above, M.column(2) would return 
        # [3, 6, 9]

    @property
    def nrows(self):
        # return the number of rows

    @property
    def ncolumns(self):
        # return the number of columns

    def __getitem__(self, ij):
        # return the matrix element at ij, where ij is a tuple
        # for the (row, column).  For example above,
        # 

    def __setitem__(self, ij, val):
        # assign the value to the matrix as ij, where ij is 
        # a tuple for (row, column)


    def transpose(self):
        # return a new Matrix whose content is same as this 
        # Matrix except the row and column positions are 
        # switched.  In the example above, 
        # M.transpose() would return
        # Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        # Note: use zip() to do the transpose

    def randomize(self):
        # return another matrix whose content is the same as
        # this matrix except their positions are randomized.

    def __matmul__(self, other):
        # return the matrix product for the two matrices A B
        # p[i,j] = sum(A[i,k] * A[k,j]) for 0 <= k <= A.nrows
        # where A.nrows must be == B.ncolumns
```
Note: use itertools.longest_zip in at least one of the methods.

## 13_bonus

(Difficulty: ★★★★☆)  Write a function that can take a variable number of parameters to make a postfix calculator for dates.  This is similar to the postcalc example from HW8, except you work on dates instead of numbers.

The parameter list consists of either the operands or the operators.  An operand is either a date string or a date-delta string and is pushed on the stack.  An operator is a string that indicates the action to take.  A binary arithmetic operator pops the top two elements from the stack and pushes back the result. 

|argument|	|action|
| :-----------:  | :-----------: |
int	push int onto stack
date(year, month, day)	push date onto stack
days(d)	push days delta onto the stack
weeks(w)	push weeks delta onto the stack
months(m)	push months delta onto the stack
'today'
'tomorrow'
'yesterday'	push today's date, tomorrow's date, or yesterday's date onto the stack
'add'	A = pop(); B = pop(); push(A+B) 
'sub'	A= pop(); B = pop(), push(A-B)
'swap'	A=pop(); B=pop(); push(A); push(B)
Write a stack-style date-time calculator function called datecalc.  Here is an example

```
$ python3 datecalc.py
>>> datecalc('today', 'tomorrow', 'yesterday', daydelta(4))
[date(2019, 12, 3), date(2019, 12, 4), date(2019, 12, 2), days(4)]
>>> datecalc('today', 'tomorrow', 'yesterday', days(4), 'add')
[date(2019, 12, 3), date(2019, 12, 4), date(2019, 12, 06)]
>>> datecalc('today', months(2), 'add')
[date(2020, 02, 03)]
>>> datecalc('today', date(2019, 12, 10), date(2019, 12, 20), 'sub', 'add')
[date(2019, 12, 13)]
>>> datecalc('today', weeks(2), 'add', months(3), 'swap', 'sub')
[date(2019, 10, 27)]
```
Hint: 

Obviously, you should take advantage of the datetime module to do as much of the work as possible.  You will need to define your own classes

days
weeks
months

The datetime.timedelta class can be the base class for your own days class and weeks class.   The days class would simply define a constructor that passes the days parameter to the base class; the weeks class is similar except it is simply in units of 7 days.  The overloaded operators can be inherited directly from the timedelta class.  You also need to define your own __repr__ special method for these two classes so their values can be displayed accordingly.

Your months class would be your own class.  The reason is that the number of days depends on the actual date.  So, you can't simply say 2 months is 60 days. Instead, when you do date + months or date - months, you operate on the month (and maybe year) field and return a newly constructed date object.
```
Your months class needs to define the special methods 
__add__(self, RHS)  # if RHS is date, return new date; 
                    # if RHS is months, return sum months
__sub__(self, RHS)  # RHS can only be months; 
                    # => return date constructor call with
                    #    updated month value
                    # all other types => type error
__radd__(self, LHS) # simply return self + LHS
                    # and LHS can only be date.
__rsub__(self, LHS) # LHS can only be months; 
                    # => return date constructor call with
                    #    updated month value
```

Once these classes are all working, then put your code into the loop structure as in the postcalc.  You also need to update the string comparison so that the strings such as yesterday, today, and tomorrow get mapped to the respective date object.

