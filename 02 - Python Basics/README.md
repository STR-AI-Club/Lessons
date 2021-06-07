# Python Basics

**Contents**
- [Python Basics](#python-basics)
- [Syntax](#syntax)
  - [Declaration](#declaration)
  - [Comments](#comments)
- [Data Types](#data-types)
  - [Numbers](#numbers)
  - [Strings](#strings)
  - [Booleans](#booleans)
  - [Lists](#lists)
  - [Dictionaries](#dictionaries)
  - [Type Casting](#type-casting)
- [If & Else](#if--else)
- [Loops](#loops)
  - [`for` loop](#for-loop)
  - [`while` loop](#while-loop)

In python, one very basic tool we can use to see the value of variables is the `print` function. To print something to the terminal, the syntax goes as follows:
```py
print(element)
```

In this lesson, we will be using `>>>` to represent what will be printed on the console. *For example:*
```py
print("Hello, World!")
>>> Hello, World!
```

# Syntax

Syntax is another word for rule. When writing code in any programming language, there are a set of rules you must follow for your computer to understand.

## Declaration

Variables are the core of most programming languages. In Python, variables can simply be declared with an equal sign (=). *Some examples of variables:*
```py
random_number = 10
piValue = 3.14
john_cena = "John Cena"
_last_name = "hmm what i put here"
```

Variable names are allowed to have any alphanumeric character, as well as the `_` character. However, variable names are not allowed to start with numbers.

Note that python variables are *case sensitive*, so in other words, capitalization matters.
```py
# these three variables all are different
cheeses = 1
Cheeses = 2
chEEsEs = 3
```

There are also some reserved keywords that you may not name your variables after. These words will be seen by Python as special words, and it will not treat it as a variable. We will talk more about keywords later in this lesson.

*Some invalid variable names:*
```py
2apples = "two apples" # (preceding number)
pizza-count = 100      # (illegal character, -)
fav num = 89           # (space separated)
open = 90              # (reserved keyword)
```

## Comments

Comments are a way to annotate your code, write down thoughts, or explain what is going on in different sections to make it easier for others to understand.

In python, a comment is marked by a `#`. If you are commenting multiple lines of code, you can surround it with `'''`. Comments can go on a new line or at the end of a line with other code. *Some examples of comments:*
```py
do_i_like_apples = 1 # mmm delicious

# the comment below is not true
'''
do_i_like_to_code = 0
'''
```

# Data Types

Python has a variety of *data types* that can each store and do different things. In this lesson we will be covering the most essential data types for what we will be doing.

## Numbers

A number in Python can be any integer or decimal number. In Python, we refer to integers as *int*s and decimals as *float*s (as in floating point integers).

Numbers can be declared as you'd expect:
```py
one = 1         # int
neg_two = -2    # int
e = 2.71        # float
epsilon = 1e-07 # scientific notation (still a float)
```

We can also perform basic arithmetic with ints and floats. *For example:*
```py
x = 12
y = 38

# addition
a = x + y
print(a)
>>> 50

# subtraction
b = x - y
print(b)
>>> -26

# multiplication
c = x * y
print(c)
>>> 456

# division
d = x / y
print(d)
>>> 0.3157894737

# floor division
e = y // x
print(e)
>>> 3

# modulus
f = y % x
print(f)
>>> 2
```

A simpler way to do operations on numbers is using special operators. Typing the following code may be tedious at times:
```py
a = 4
a = a + 8
print(a)
>>> 12
```

So we can use the `+=` operator:
```py
a = 4
a += 8
# this is the same as a = a + 8
print(a)
>>> 12
```

All basic arithmetic operators can also be used in this way.

Operator | Equivalent
:---: | :---:
`a += b` | `a = a + b`
`a -= b` | `a = a - b`
`a *= b` | `a = a * b`
`a /= b` | `a = a / b`
`a //= b` | `a = a // b`

## Strings

A string in Python is a combination of any characters. Think of it as a word, sentence, or phrase. In python, strings are surrounded by the `"` character or `'` character. *Some examples of strings:*
```py
banana = "banana"
my_name = "Kanye East"
true_statement = 'AI Club makes you elite'

# you can also combine strings
print(banana + my_name)
>>> bananaKanye East

# the ',' character can do the same but with a whitespace in between
print(banana, my_name)
>>> banana Kanye East
```

Strings can also be multiple lines long. These are called *multi-line strings*. These are surrounded by `"""` or `'''`. You may notice that these are the exact same as multi-line comments. The difference is that this time we are assigning them to a variable. *Some examples of multi-line strings:*
```py
jumble = """
Lorem ipsum
dolor sit amet
"""
```

## Booleans

In programming, a boolean is anything that we can determine as true or false. In python, we use the keywords `True` and `False` (capitalization is important). *Examples of booleans:*
```py
ate_lunch = True
still_hungry = False

print(ate_lunch)
>>> True
```

Expressions are also booleans. There are a few operators which compare two variables and return a boolean value.

Operator | Meaning
:---: | :---:
`==` | equal to
`!=` | not equal to
`>` | greater than
`>=` | greater than or equal to
`<` | less than
`<=` | less than or equal to

*Examples:*
```py
print(1 == 2)
>>> False

print(10 > 9.9)
>>> True

print("hi" != "hi")
>>> False
```

## Lists

Lists can be used to store multiple items inside a single variable. *For example:*
```py
fruits = ["banana", "apple", "strawberry", "grape"]
```

Lists can be indexed to access specific values inside. The first item in a list is index `0`, and the other items would be `1, 2, 3,...`. To access an item in a list by index, we use square brackets. *For example:*
```py
primes = [2, 3, 5, 7, 11, 13]
first_prime = primes[0]
third_prime = primes[2]

print(first_prime)
>>> 2

print(second_prime)
>>> 5
```

## Dictionaries

Dictionaries can be used to store multiple values in key, item pairs. Think of them as lists except you can index them with specific values, called *keys*, to retrieve their corresponding values, called *items*.
```py
ages = {
    "Bob": 78,
    "Ellen": 57,
    "Koral": 25,
    "Bryan": 1000
}
```

To index items in a dictionary, we can get them by their keys.
```py
ages = {
    "Bob": 78,
    "Ellen": 57,
    "Koral": 25,
    "Bryan": 1000
}

bob_age = ages["Bob"]
ellen_age = ages["Ellen"]

print(bob_age)
>>> 78

print(ellen_age)
>>> 57
```

## Type Casting

We can change the type of a variable by using functions such as *int()* and *float()*. The terminology for this is *type casting*. We can also check the type of a variable by using the *type()* function. *For example:*
```py
x = 1
y = 1.5
z = '2'

# we can check the variable's type the following way
print(type(x), type(y), type(z))
>>> <class 'int'> <class 'float'> <class 'str'>

# remember that int() always rounds the number down
a = int(y)
print(y)
>>> 1

# float() adds a decimal place upon conversion.
b = float(x)
print(b)
>>> 1.0

# round() rounds the number to the closest integer
c = round(y)
print(c)
>>> 2

# str() converts to a string
d = str(y)
print(d)
>>> 1.5 #this is technically a string in the terminal

#list() converts to a list
e = list(z)
print(e)
>>> ['2']
```

Type casting will not work if a variable can't be converted to another type. Usually, it is quite simple to see why.
```py
num = "four"
num_int = int(num)
# this would raise a value error because
# you can't convert a word to a number
```

# If & Else

The `if` and `else` keywords are used to check logical statements (aka booleans).
```py
a = 5
b = 4
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
>>> a is equal to b
```

Another keyword, `elif`, can also be used to check logical statements. Basically, if a previous statement was not true, we can check another statement to see if this one is true.
```py
n = 98
if n > 100:
    print("n bigger than 100")
elif n > 50:
    print("n bigger than 50")
else:
    print("n is so small")
>>> n bigger than 50
```

The syntax of `if...else` statements are very important. Notice the semicolon (`:`) at the end of each statement, and the indent under each condition. The following code would not run:
```py
if 80 > 1:
print("yes")
```

# Loops

There are two types of loops in python.

## `for` loop

The `for` loop can be used to iterate over an iterable, such as a list, string, or range of numbers.
```py
# loop through list
for num in [1, 3, 5]:
    print(num)
>>> 1
>>> 3
>>> 5

# loop through string
for character in "AI":
    print(character)
>>> A
>>> I

# loop through range
# (the range function start at 0 and ends at n-1)
total = 0
for i in range(5):
    total += i
print(total)
>>> 10

total2 = 0
for i in range(3, 10): # iterate over the range [3, 9)
    total += i
print(total):
>>> 42
```

## `while` loop

The while loop executes whatever is in its contents as long as a condition is true.
```py
i = 0
while i < 3:
    print(i)
    i += 1
>>> 0
>>> 1
>>> 2
```

Be careful, because while loops can run on forever!
```py
# try running the following code snippet on a test file
# (press ctrl+c to stop it)
i = 15
while i >= 2:
    print("still true...")
```
