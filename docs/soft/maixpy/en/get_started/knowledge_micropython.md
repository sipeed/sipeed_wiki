---
title: MicroPython background knowledge
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MicroPython background knowledge
---


Since **MaixPy** is developed and built on top of **MicroPython**,
The final interface provided to users is **Micropython**, so we need to be familiar with the basic knowledge and syntax of `MicroPython` at the beginning of development using MaixPy


## About MicroPython:

MicroPython is a streamlined and efficient implementation of the programming language Python3. The syntax is consistent with Python3, but only a small part of the Python standard library is implemented. It is optimized and can be used in resource-constrained environments such as MCU and WIFI SOC. So we To use MicroPython, you need to understand its syntax.

If you have previous programming experience in **C/C++/Java** (or any other language), it is recommended
[*(Liao Xuefeng's Python Tutorial).*](https://www.liaoxuefeng.com/wiki/1016959663602400)

If you do not have any programming experience before, recommend
[*(Learn Python in a Stupid Way).*](https://wizardforcel.gitbooks.io/lpthw/content/)

## REPL and serial port

First, disconnect the connection between the development board and MaixPy IDE, otherwise the serial port will conflict!

Open a terminal window in MaixPy IDE

print('The quick brown fox','jumps over','the lazy dog')

Output:

```
The quick brown fox jumps over the lazy dog
```

print() will print each string in turn, and will output a space when it encounters a comma ",". Therefore, the output string is spelled like this:

> The quick brown fox jumps over the lazy dog

print() can also print integers or calculate results:

```python
print(300)
300
print(100 + 200)
300
```

Therefore, we can print the result of calculating 100 + 200 more beautifully:

```python
print('100 + 200 =', 100 + 200)
100 + 200 = 300
```

Note that for 100 + 200, the Python interpreter automatically calculates the result 300, but '100 + 200 ='is a string instead of a mathematical formula, and Python treats it as a string.

## MicroPython basic syntax
### Variable

In Python, the equal sign `=` is an assignment statement, which can assign any data type to a variable. The same variable can be assigned repeatedly, and it can be a variable of different types, for example:

```python
a = 123 # a is an integer
print(a)
a ='ABC' # a becomes a string
print(a)
```

This kind of language with variable types is called **dynamic language**, and its counterpart is **static language**.
A static language must specify the variable type when defining a variable. If the type does not match when assigning a value, an error will be reported. For example, Java is a static language, and the assignment statement is as follows (// means comment):

```java
int a = 123; // a is an integer variable
a = "ABC";// Error: Cannot assign a string to an integer variable
```

Compared with static languages, dynamic languages ​​are more flexible for this reason.

### List

One of the built-in data types of Python is **list**: **list**.<br/>
**list** is an ordered collection, elements can be added and deleted at any time.
For example, to list the names of all classmates in the class, you can use a **list** to indicate:

```python
classmates = ['Michael','Bob','Tracy']
classmates
['Michael','Bob','Tracy']
```

The variable classmates is a `list`.<br/>
Use the `len()` function to get the number of list elements:

```python
len(classmates)
3
```

Use the index to access the elements at each position in the list, the index starts from 0:

```python
classmates[0]
'Michael'
classmates[1]
'Bob'
classmates[2]
'Tracy'
classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

When the index exceeds the range, Python will report an IndexError error, so make sure that the index does not exceed the range, remember that the index of the last element is len(classmates)-1.

If you want to get the last element, in addition to calculating the index position, you can also use -1 as an index to get the last element directly:

```python
classmates[-1]
'Tracy'
```

By analogy, you can get the second to last and third to last:

```python
classmates[-2]
'Bob'
classmates[-3]
'Michael'
classmates[-4]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  IndexError: list index out of range
```

Of course, the fourth from last crossed the line.

The list is a **variable** **ordered list**, so you can append elements to the list to the end:

```python
classmates.append('Adam')
classmates
['Michael','Bob','Tracy','Adam']
```

You can also insert the element into a specified position, such as the position with index number 1:

```python
classmates.insert(1,'Jack')
classmates
['Michael','Jack','Bob','Tracy','Adam']
```

To delete the element at the end of the list, use the pop() method:

```python
classmates.pop()
'Adam'
classmates
['Michael','Jack','Bob','Tracy']
```

To replace an element with another element, you can directly assign it to the corresponding index position:

```python
classmates[1] ='Sarah'
classmates
['Michael','Sarah','Tracy']
```

The data types of the elements in the list can also be different, for example:

```python
L = ['Apple', 123, True]
```

If there is no element in a list, it is an empty list with a length of 0:

```python
L = []
len(L)
0
```

### Tuple

Another kind of ordered list is called tuple: **tuple**.<br/>
Tuple is very similar to list, but once the `tuple` is initialized, it cannot be modified. For example, it also lists the names of classmates:

```python
classmates = ('Michael','Bob','Tracy')
```

Now, the **tuple** of classmates cannot be changed, and it does not have methods such as append(), insert(). The other methods of obtaining elements are the same as list, you can use classmates[0], classmates[ normally -1), but cannot be assigned to another element.

What is the point of an immutable tuple? Because tuples are immutable, the code is safer.
If possible, try to use tuple instead of list.

The trap of tuple: When you define a tuple, the elements of the tuple must be determined at the time of definition, such as:

```python
t = (1, 2)
t
(1, 2)
```

However, to define a
A tuple with only 1 element, if you define it like this:

```python
t = (1)
t
1
```

But at this time, the definition is not tuple, t is an integer variable, and the value of variable t is 1! <br/>
This is because parentheses () can represent tuples and parentheses in mathematical formulas, which creates ambiguity.Therefore, Python stipulates that in this case, the calculation is based on parentheses, and the calculation result is naturally 1.

Therefore, the definition of **tuple** with only 1 element must add a comma `,`, to disambiguate:

```python
t = (1,)
t
(1,)
```

When Python displays a tuple with only 1 element, it will also add a comma `,` to prevent you from misunderstanding it as a bracket in the sense of mathematical calculations.

### Conditional judgment

The complete form of the if statement is:

```
if <condition judgment 1>:
    <Execute 1>
elif <condition judgment 2>:
    <Execute 2>
elif <condition judgment 3>:
    <Execute 3>
else:
    <Execute 4>
```

such as:

```python
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```

### Loop

There are two types of Python loops, one is the `for...in` loop, which iterates over each element in a list or tuple in turn, see an example:

```python
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
```

Executing this code will print each element of names in turn:

```python
Michael
Bob
Tracy
```

So the `for x in ...` loop is to substitute each element into the variable x, and then execute the statement of the indented block.

If you want to calculate the sum of integers from 1 to 100, it is a bit difficult to write from 1 to 100. Fortunately, Python provides a range() function that can generate a sequence of integers, which can be converted to a list by the list() function.<br/>
For example, the sequence generated by range(5) is an integer less than 5 starting from 0:

```python
list(range(5))
[0, 1, 2, 3, 4]
```

range(101) can generate a sequence of 0-100 integers, calculated as follows:

```python
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
```

The second type of loop is the **while loop**. For example, if we want to calculate the sum of all odd numbers within 100, we can use the while loop:

```python
sum = 0
n = 99
while n> 0:
    sum = sum + n
    n = n-2
print(sum)
```

-----

### Data type conversion

Python's built-in common functions also include data type conversion functions, such as the int() function to convert other data types to integers:
```python
>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
from machine import GPIO
```
### Functions

In Python, to define a function, use the `def` statement, write the function name, parentheses, the parameters in the parentheses and the colon `:` in turn, and then write the function body in the indented block, and the return value of the function is returned The statement returns.

Let's write a function to calculate x2:

```python
def power(x):
    return x * x
```

For the power(x) function, the parameter x is a positional parameter.

When we call the power function, we must pass in one and only one parameter x:

```python
power(5)
25
power(15)
225
```

Now, what if we want to calculate x3? We can define another power3 function, but what if we want to calculate x4, x5...? We cannot define an infinite number of functions.

You may think of it, you can modify power(x) to power(x, n) to calculate xn, just do it:

```python
def power(x, n):
    s = 1
    while n> 0:
        n = n
         - 1
        s = s
         * x
    return s
```

For this modified power(x, n) function, any n-th power can be calculated:

```python
power(5, 2)
25
power(5, 3)
125
```

The modified power(x, n) function has two parameters: x and n. These two parameters are positional parameters. When the function is called, the two values ​​passed in are assigned to the parameters x and n in order of position.

### Slice

It is a very common operation to take some elements of a `list` or `tuple`. For example, a list is as follows:

```python
L = ['Michael','Sarah','Tracy','Bob','Jack']
```

Take the first 3 elements and complete the slice with one line of code:

```python
L[0:3]
['Michael','Sarah','Tracy']
```

L[0:3] means that it starts from index 0 and ends at index 3, but does not include index 3. That is, indexes 0, 1, 2, are exactly 3 elements.

If the first index is 0, it can also be omitted:

```python
L[:3]
['Michael','Sarah','Tracy']
```

You can also start at index 1, and take out 2 elements:

```python
L[1:3]
['Sarah','Tracy']
```

`tuple` is also a kind of list, the only difference is that `tuple` is immutable. Therefore, `tuple` can also be sliced, but the result of the operation is still `tuple`:

```python
(0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
```

`String`'xxx' can also be regarded as a kind of `list`, each element is a character. Therefore, string can also be sliced, but the result of the operation is still a string:

```python
'ABCDEFG'[:3]
'ABC'
```

### Object

Python is **object-oriented** programming, such as an LED light

```python
from pyb import LED

red_led = LED(1)
red_led.on()
```

LED is a **class**, red_led is an **object**, you can operate this object, such as turning on, turning off, and viewing the value.

### Module

### What is a module?

As the code increases, the code in a file will become longer and more difficult to understand.

In order to write maintainable code, we group many functions into different files. In Python, a `.py` file is called a **Module**.

What are the benefits of modules?

Easy to reuse code! If I wrote a module and you also wrote a module, we have two modules. We organize these modules so that everyone can write a lot less code!

#### How to use modules?

```python
import time

time.sleep_ms(500)
```

`import time` is to import the `time` module. The module can be imported through the `import` statement.

### More

Please search for more MicroPython basic syntax tutorials.
