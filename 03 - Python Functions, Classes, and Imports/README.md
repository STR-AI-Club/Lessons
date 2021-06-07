# Python - Functions, Classes and Imports

**Contents**
- [Python - Functions, Classes and Imports](#python---functions-classes-and-imports)
- [Functions](#functions)
- [Classes](#classes)
- [Imports](#imports)

Functions (and classes to an extent) are essential to python. They can simplify repetitive tasks for us, and make re-usable code.

# Functions

The idea of functions in programming is not much different than functions in math. **Note that in most programming languages functions are referred to as methods**.

For example, in math you may have something like:

$f(x) = 2x$.

This function takes in a number, $x$, and returns an output, $2x$.

The same function in python would look like:
```py
def f(x):
    return 2 * x
```

We can now call this function as many times as want:
```py
def f(x):
    return 2 * x

a = f(100)
print(a)
>>> 200

b = f(-0.3)
print(b)
>>> -0.6
```

The x inside the brackets are what we call *parameters*, which is the input for the function. The function then does something with the parameters, and returns an output with the `return` keyword. *Functions can also take in multiple parameters:*
```py
def add(a, b):
    return a + b
```

This function takes in two variables, `a` and `b`, and returns their sum.

Functions also don't have to return anything:
```py
def multiply(a, b, c):
    print("The product of " + str(a) + ", " + str(b) ", " + str(c) + "is:")
    print(a*b*c)

multiply(2, 3, 5)
>>> The product of 2, 3, 5 is:
>>> 30
```

Functions can take no parameters:
```py
def say_hi():
    print("i said hi")

say_hi()
>>> i said hi
```

Finally, python has some built in functions. You may have noticed that `print` is a function. (All type casters are functions as well!) Here are some examples:
```py
# input() takes input from the user
# (you can type input into the terminal, represented by <<<)
a = input()
print(a)
<<< i really enjoy trees
>>> i really enjoy trees
```

```py
# min() does what you think it does
print(min(100, -100))
>>> -100

print(min([5, 3, 1, 4, 2]))
>>> 1
```

```py
# so does max()
print(max(100, -100))
>>> 100

print(max([5, 3, 1, 4, 2]))
>>> 5
```

```py
# abs() returns absolute value
print(abs(-99999))
>>> 99999

print(abs(6789))
>>> 6789
```

```py
# sum() returns the sum of an iterable (list, etc.)
print(sum([4, 2, 0, 1, 1]))
>>> 8
```

```py
# len() returns the length of a list
print(len([1, 2, 3, 4]))
>>> 4
```

# Classes

Classes are the core of something we call "Object Oriented Programming" (OOP). Although we will not be using classes much during the club, it is good to know how they work in case an occurrence comes up (which it will).

Think of a class like an object. We can have a class for a person, a plant, or anything else. Every class has to have an ``__init__()`` method, which is what we call a *constructor*.
```py
# class for a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Every method in a class must take `self` as a first parameter. The `self` keyword refers to the class itself. All variables that belong to the class will follow the convention of `self.variable_name`. (If this is hard to understand, just remember that `self` is needed for all class methods.) To access a class variable, we use `object.variable`.

We can now create multiple people with the `Person` class:
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# one object (it's a person but just pretend)
bobby = Person("Bobby", 12)
ally = Person("Ally", 13)
print(ally.age)
>>> 13

# (bobby gets older)
bobby.age = 34
print(bobby.age)
>>> 34
```

Notice how when we create a class, we use the parameters in the `__init__()` method. We don't need to provide anything in the place of `self`.

It is good practice to only initiate class variables in the constructor (`__init__()`).

We can also have other methods in the class. These are called class methods.
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(self.name + " says hi!")

bobby = Person("Bobby", 12)
bobby.greet()
>>> Bobby says hi!
```

Here's a slightly more complicated example of a class. Give it a try on a test file!
```py
class Counter:
    def __init__(self, count):
        self.count = count

    def add(self, value):
        self.count += value

    def subtract(self, value):
        self.count -= value

    def get_count(self):
        print("The count is: " + str(self.count))
```

# Imports

There are some things that we want to do when programming, but it may be too much work to write it yourself. Libraries are basically a collection of functions and classes that we can import into our program to do specific tasks for us.
```py
# the 'random' library has a collection of functions that
# allow us to generate random things (like numbers)

# we first import the library
import random

# we can now call functions that are part of the library
# random.randint returns a random integer in [a, b]
random_num = random.randint(1, 3)
print(random_num)
>>> 1
```

Sometimes we may not want to import an entire library. Rather, we may only need a few functions. To do this we can use the `from` keyword.
```py
# import the 'randint' function from the 'random' library
from random import randint

print(randint(1, 3))
>>> 2
```

Furthermore, some python libraries may have quite long names, so we can import them with an alias. For this we use the `as` keyword.
```py
import random as rd

print(rd.randint(1, 3))
>>> 2
```

```py
# this is the same as above
# import 'randint' with alias 'ri'
from random import randint as ri

print(ri(1, 3))
>>> 3
```
