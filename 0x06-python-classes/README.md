# Classes and Objects

# Learning Objectives

* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method``
* What is the special `__init__` method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

# Tasks

## My first square

Write an empty class `Square` that defines a square:

* You are not allowed to import any module

**Solution:** [0-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/0-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./0-main.py
<class '0-square.Square'>
{}
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# 
```

## Square with size

Write a class `Square` that defines a square by: (based on `0-square.py`)

* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module

**Solution:** [1-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/1-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```

## Size validation

Write a class `Square` that defines a square by: (based on `1-square.py`)

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module

**Solution:** [2-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/2-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```

## Area of a square

Write a class `Square` that defines a square by: (based on `2-square.py`)

* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

**Solution:** [3-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/3-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```

## Access and update private attribute

Write a class `Square` that defines a square by: (based on `3-square.py`)

* Private instance attribute: `size`:
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        * if `size` is less than 0, raise a ValueError exception with the message `size must be >= 0`
* Instantiation with optional `size`: `def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module

**Solution:** [4-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/4-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```

## Printing a square

Write a class `Square` that defines a square by: (based on `4-square.py`)

* Private instance attribute: `size`:
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Instantiation with optional `size`: `def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line
* You are not allowed to import any module

**Solution:** [5-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/5-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```

## Coordinates of a square

Write a class `Square` that defines a square by: (based on `5-square.py`)

* Private instance attribute: `size`:
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Private instance attribute: `position`:
    * property `def position(self):` to retrieve it
    * property setter `def position(self, value):` to set it:
        * `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message position `must be a tuple of 2 positive integers`
* Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line
    * `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
* You are not allowed to import any module

**Solution:** [6-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/6-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```

## Compare 2 squares

Write a class `Square` that defines a square by: (based on `4-square.py`)

* Private instance attribute: `size`:
	*property `def size(self)`: to retrieve it
	*property setter `def size(self, value):` to set it:
		*`size` must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`
		*if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* Instantiation with `size: def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current square area
* `Square` instance can answer to comparators: `==, !=, >, >=, < and <=` based on the square area
* You are not allowed to import any module

**Solution:** [102-square.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/102-square.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes# ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
root@985e10084b49:~/holbertonschool-higher_level_programming/0x06-python-classes#
```
