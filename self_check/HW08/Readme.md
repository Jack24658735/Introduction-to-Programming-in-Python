# HW8

## 8_1
(Difficulty: ★☆☆☆☆) Write a function which named Volcal() that can take three parameters to calculate the volume of cuboid. Three parameters includes length, width and height. Please set their default value as (10,10,10),and the function will print their length,width and height and return coboid’s value. 

## 8_2
(Difficulty: ★★☆☆☆) Write a function that can take a variable number of parameters to decide who is older. The parameter list consists of many people’s names and their ages. the function need to print who is oldest and return oldest person’s age.If the parameter is empty,you need to return -1.
[Note] You don’t consider that 2 people have the same age. 

## 8_3
(Difficulty: ★★★☆☆) Write a function that can take a variable number of parameters to make a postfix calculator.  The parameter list consists of either the operands or the operators.  An operand is a number (int or float) and is pushed on the stack.  An operator is a string that indicates the action to take.  A binary arithmetic operator pops the top two elements from the stack and pushes back the result. 

| argument     | action     |
| :-----------:  | :-----------: |
| int or float literal     | push int or float literal onto stack     |
	
'add'	A = pop(); B = pop(); push(A+B) 
'sub'	A= pop(); B = pop(), push(A-B)
'mul'	A=pop(); B = pop(); push(A*B)
'swap'	A=pop(); B=pop(); push(A); push(B)
```
>>> postcalc(1, 2, 3, 4)
[1, 2, 3, 4]
>>> postcalc(1, 2, 3, 4, 'add')
[1, 2, 7]
>>> postcalc(1, 2, 'add')
[3]
>>> postcalc(1, 2, 3, 'add', 'sub')
[4]
>>> postcalc(2, 3, 'add', 4, 'mul', 5, 'swap', 'sub')
[15]
```

In addition, it should be able to take an optional stack in the form of a list of numbers.
```
>>> postcalc(1, stack=[2, 3, 4])
[2, 3, 4, 1]
>>> postcalc(3, 4, 'add', stack=[1, 2])
[1, 2, 7]
>>> postcalc('add', stack=[1, 2])
[3]
>>> postcalc('add', 'sub', stack=[1, 2, 3])
[4]
>>> postcalc('add', 4, 'mul', 5, 'swap', 'sub', stack=[2, 3])
[15]
```

Before solving this problem, decide on how should the formal parameters of this function be declared?  Should you use variable-length arguments? arguments with default value?  
