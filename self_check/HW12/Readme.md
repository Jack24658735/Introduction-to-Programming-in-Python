# HW12

## 12_1
(Difficulty: ★★☆☆☆) Define a generator function CharRange, which generates a range of characters with inclusive bounds.  It takes two parameters for the starting and ending characters.  It yields one character at a time whose unicode number is one closer to the ending.  For example,
```
$ python3 -i charrange.py
>>> cr = CharRange('A', 'E')
>>> list(cr)
['A', 'B', 'C', 'D', 'E']
>>> dr = CharRange('E', 'A')
>>> list(dr)
['E', 'D', 'C', 'B', 'A']
>>> 
```

Hint: the generator looks like
```
def CharRange(start, end):
    ...
```
It helps to convert between the character and the code using the ord() and chr() functions.  To support stepping up or down, you need to check if the start is larger or smaller than the end.  You may use range() to get one value at a time, but range() works for integers only; also, range's bound is exclusive, not inclusive, so you will need to make an adjustment for the bound's value.  A generator uses yield instead of return to pass values back.  After you finish yielding values, you don't have to do anything special, and your function will implicitly return None to mark the end of generation.


## 12_2
(Difficulty: ★★★☆☆) Define an iterable class named DaysInYear for iterating the days in a year.  It takes the year as the argument to the constructor.  Instead of implementing the \_\_iter\_\_ method to return the iterator object, it implements the \_\_getitem\_\_ method to return the ith value.  The index to \_\_getitem\_\_ indicates the ith day of the year, where i = 0 means January 1, i = 1 means January 2, etc.
```
$ python3 -i daysinyear.py
>>> y = DaysInYear(2019)
>>> y[5]
'2019.01.04'
>>> y[364]
'2019.12.31'
>>> y[31]
'2019.02.01'
>>> y[365]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "daysinyear.py", line 15, in __getitem__
    raise StopIteration
StopIteration
```

By defining the \_\_getitem\_\_ method, it makes the class iterable and you don't need to define the \_\_iter\_\_ method to return an iterator object -- the caller is responsible for tracking the iteration state.  You do need to raise a StopIteration exception when the index is beyond the last day.  
This allows you to convert it to a list, use in a for loop, etc.

## 12_bonus
(Difficulty: ★★★★☆) Define a class named CountingList.  It works like a list except it also keeps track of the number of times each element is accessed.  It should also be iterable but its iterator outputs elements in decreasing order of access count.  An access is defined by a call to either \_\_getitem__(self, i) or \_\_setitem\_\_(self, i, val) where i may be an int or a slice.
```
>>> d = CountingList(('A', 'B', 'C', 'D', 'E'))
>>> d[0], d[2], d[2], d[4]   # these call __getitem__
('A', 'C', 'C', 'E')         
>>> [d[-1], d[-2], d[4]]
['E', 'D', 'E']              
>>> for i in d:
...     print(i)
...
E
C
D
A
B
```

As you can probably figure out, you should define CountingList by subclassing from the built-in list class, like
```
class CountingList(list):
    def __init__(self, d = ()):
        super().__init__(d)
        # additional code here
    def __getitem__(self, i):
        # i is the index or slice.
        # (1) use the same i to increment the access count,
        #     your code here...
        # (2) return what the base class does, as below
        return super().__getitem__(i)
    def __iter__(self):
        # This returns an iterator that outputs elements in 
        # order of decreasing access count. 
```
need to implement the following methods:
a.	The constructor:\
It should first call the superclass's \_\_init\_\_ to initialize the list data structure, and then define additional data structures to keep an access count of the elements.  A good one to use is another list structure, which can be indexed using the same index as that for accessing the CountingList's content.  It contains the access count for the corresponding element in the CountingList and should be initialized to zero.\
b.	The \_\_getitem\_\_(self, i) method:\
It needs to intercept the accesses to each element by incrementing the corresponding count.  Note that the type of  i parameter can be either int or slice.  In any case, this method needs to return the value, which can can be done by calling its base class's \_\_getitem\_\_ using the same i.\
c.	Strictly speaking, you also need to intercept the \_\_setitem\_\_(self, i, val) method also.  But you should make sure your \_\_getitem\_\_ works properly before you try the \_\_setitem\_\_.  The idea is the same, since either one counts as one access.\
d.	The \_\_iter\_\_(self) method:\
It needs to return an iterator object but in order of decreasing access count.  To do so, one way is to make a list whose elements are (access count, value) and sort in decreasing order, i.e., reverse=True.  Then, you can return an iterator that iterates over the sorted value (but without the access count).

