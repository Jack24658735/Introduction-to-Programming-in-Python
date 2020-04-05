# HW10

## 10_1
(Difficulty: ★★☆☆☆) Define a class for a polynomial for a single variable x with integer coefficients and powers.   That is,
f(x) = a0 + a1 x + a2 x2 + a3 x3 + a4 x4 +  ...
Your Polynomial constructor would take variable-length arguments for the coefficients from the 0th order and up.  For instance, 
              f(x) = 3 + 5 x + 4 x2 + 7 x3 + x4 
is represented by 
```
>>> f = Polynomial(3, 5, 4, 7, 1)
It should support a method named evaluate(xvalue):
>>> f.evaluate(3)
324
```

because 3 + 5 * 3 + 4 * 32 + 7 * 33 + 34
                  = 3 + 15 + 36 + 189 + 81 
           = 324
Your Polynomial class may look like this:
```
class Polynomial:
    def __init__(self, *coeff):
        # your code here to remember to coefficients
        # 
    def evaluate(self, xvalue):
        # return the sum of coefficienti * xvalue i 

Extra information: 
If you define a special method named __call__, then the object instance can be called just like a function.  To do this, you can simply do
    __call__ = evaluate  
    # indent it at the same level as the def for the methods
this way, you define __call__ to be another name for the evaluate method, but because it is a special symbol, Python lets you say
>>> f(3)
324 
which is a more concise way than saying f.evaluate(3).
```



## 10_2
(Difficulty: ★★★☆☆) Define a class for Temperature.  The requirements are

a.	The constructor should take two arguments (degree, unit): 

b.	degree is an int or float. The constructor needs to check if degree is an int or float; if not, raise a TypeError.
  
c.	unit defaults to 'C' for Celsius, but it can be 'F' for Fahrenheit. The constructor needs to check if the unit is an allowed character; if not, raise a ValueError.  Actually, lower case 'c' and 'f'   are also accepted, but they should be converted to the upper case.

d.	The __repr__() method should return a string that, when printed, is a constructor call that yields the same value as the object.

e.	Define an instance method named get_temp().  It should return a tuple (degree, unit).   It takes one optional argument for the unit, which should be either 'C' (default) or 'F', in the same way as the constructor.

f.	Define a property named degree.  You should define two methods

### i.	get_degree(), which returns the value of the _degree attribute
### ii.	set_degree(), which assigns the parameter value to the _degree attribute
### iii.	use degree = property(...) to make degree a property

g.	Define a class method named set_format() that takes a formatting string to be used by the subsequent __repr__() calls to format the degree.

```
>>> c = Temperature(10)
>>> d = Temperature(68, 'F')
>>> c
'10.0 C'
>>> d
'68.0 F'
>>> c.get_temp()
(10, 'C')
>>> c.get_temp('F')
(50.0, 'F')
>>> d.get_temp()
(68, 'F')
>>> d.get_temp('C')
(20.0, 'C')
>>> c.degree
10
>>> c.degree = 50
>>> c
(50, 'C')
>>> c.get_temp('F')
(122.0, 'C')
>>> c
'50.0 C'
>>> c.set_format('%d')  # this is a class method call
>>> c
'50 C'
>>> c.set_format('%.3f')
>>> c
'50.000 C'
>>> d
'68.000 F'
```

## 10_bonus
(Difficulty: ★★★★☆)  Write a Python program that models the mother-side relationship in a family. 

```
class Person:
    def __init__(self, name):
        # your code here
    def __repr__(self):
        # your code here

    @property
    def name(self):
        # your code here. read-only property

    @property
    def children(self):
        # your code here. read-only property

    def add_children(self, *children):
        # your code here.
        # construct each child, linked with mother and sisters

    @property
    def mother(self):
        # your code here. read-only property

    @property
    def sisters(self):
        # your code here. read-only property
        # mother's daughters minus self

    @property
    def aunts(self):
        # your code here: return list of aunts. read-only
        # mother's sisters

    @property
    def grandchildren(self):
        # your code here: list of ALL grandchildren. read-only
        # trick is how to combine lists from daughters'
        # daughters.

    @property
    def family_tree(self):
        # make a dictionary for the family tree
        # from self to descendants but not to ancestors
        # hint: recursion
        # read-only property.
```
```
>>> p = Person('Wilma')  # constructor call
>>> p.children              # no children initially
[]
>>> p.add_children('Mary', 'Ann', 'Jill', 'Jane')
>>> p.children            # husband & wife have same children
[Person('Mary'), Person('Ann'), Person('Jill'), Person('Jane')]
>>> mary, ann, jill, jane = p.children
>>> mary
Person('Mary')
>>> mary.mother
Person('Wilma')
>>> mary.sisters
[Person('Ann'), Person('Jill'), Person('Jane')]
>>> mary.children
[]
>>> mary.add_children('Lynn', 'Cindy')
>>> lynn, cindy = mary.children
>>> lynn.aunts
[Person('Ann'), Person('Jill'), Person('Jane')]
>>> lynn.grandmother
[Person('Wilma')]
>>> jill.add_children('Kate')
>>> p.family_tree
{'Wilma': {'Mary': {'Lynn': {}, 'Cindy': {}}, 'Ann': {}, 'Jill': {'Kate'}, 'Jane': {}}
>>> p.grandchildren
[Person('Lynn'), Person('Cindy'), Person('Kate')]
>>> 
```




