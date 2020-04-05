# HW11

## 11_1
(Difficulty: ★★☆☆☆) Extend the Polynomial class from last week.  To recall, it models a polynomial for a single variable x with integer coefficients and powers.   That is,
f(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + a<sub>3</sub>x<sup>3</sup> + a<sub>4</sub>x<sup>4</sup> +  ...

The constructor takes variable-length arguments for the coefficients for polynomials to the 0, 1, 2, … degrees.

The supported operations include

●	adding or subtracting two polynomial functions to make another polynomial function by overloading the + and - operators. (i.e., define __add__ and __sub__ special methods)

●	evaluating a polynomial function for a given value of x

●	scaling a polynomial by implementing the __imul__ special method

```
>>> f = Polynomial(3, 2, 0, 5, 4)
>>> g = Polynomial(7, 4, 1)
>>> f + g
Polynomial(10, 6, 1, 5, 4)
>>> g - f
Polynomial(4, 2, 1, -5, -4)
>>> f *= 2
Polynomial(6, 4, 0, 10, 8)
>>> f(1)
28
>>>
```

## 11_2
(Difficulty: ★★★☆☆) Define a NewTemp class by subclassing from the Temperature class from last week so that it can support 

a.	operator overloading for + and -.  The unit of the operation defaults to the unit of the left-hand-side.

b.	changing units, including 'C' (Celsius), 'F' (Fahrenheit)

```
Note: define __add__(self, RHS) and __sub__(self, RHS) methods to overload the + and - operators. You must check the RHS (= "right hand side") parameter's type to make sure it is an instance of Temperature (base class is okay -- doesn't have to be NewTemp), or it could be a number (int or float).  If it is a Temperature, convert it to the same unit as self's unit before adding or subtracting.  If it is a number (int or float), simply assume it is of the same unit.
```

```
>>> t = NewTemp(20, 'C')
>>> t + 3
NewTemp(23, 'C')
>>> u = NewTemp(30, 'C')
>>> t + u
NewTemp(50, 'C')
>>> t - u
NewTemp(-20, 'C')
>>> t.unit
'C'
>>> t.unit = 'F'
>>> t
NewTemp(68.0, 'F')
>>> t + u
NewTemp(122.0, 'F')
```


## 11_3
(Difficulty: ★★★★☆) Write a NewList class by inheriting from the built-in list class to support the following operations:
a.	list multiplication (also known as cross-product) by overloading the @ operator (define the \_\_matmul\_\_(self, RHS) special method)
```
>>> NewList([6,7,8]) @ NewList(['a', 'b'])
NewList([(6, 'a'), (6, 'b'), (7, 'a'), (7, 'b'), (8, 'a'), (8, 'b')])
```

b.	scalar multiplication, to be distinguished from list repetition.  e.g., 
```
>>> NewList([6, 7, 8]) * 2 
NewList([6, 7, 8, 6, 7, 8]) 
as in a regular list, but
>>> 2 * NewList([6, 7, 8]) 
 NewList([12, 14, 16])
>>> 3 * NewList(['a', 'b', 'c'])
NewList(['aaa', 'bbb', 'ccc'])

Hint:  define the __rmul__(self, scalar) special method, where scalar is a number.
```

c.	alternative base index (e.g., starting from index 1 instead of index 0).  However, negative index remains the same.
```
>>> L = NewList(['a', 'b', 'c', 'd', 'e'])
>>> L[1]
'a'
>>> L[5]
'e'
```

d.	inclusive limit instead of exclusive (e.g., L[2:5] refers to L[2],..., up to and including L[5], whereas a regular list is up to but not including L[5]).  This should work for downward (e.g., negative) stepping and slicing.
```
>>> L[2:3]
NewList(['b', 'c'])
>>> L[4:2:-1]
NewList(['d', 'c', 'b'])
>>> L[-1]
'e'
```

Hint: to implement c and d, you will need to overload all operators that may use indexing or slicing. This means 
```
__getitem__(self, itemref) -- called by L[i], L[i:j] or L[i:j:k],
__setitem__(self, itemref, val) -- called to do L[i] = val, L[i:j] = val, L[i:j:k]=val
__delitem__(self, itemref) -- called to do del L[i], del L[i:j], or del L[i:j:k]
```
