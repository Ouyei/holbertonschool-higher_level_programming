# Exceptions

# Learning Objectives

* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception* 

# Tasks

## Safe list printing

Write a function that prints `x` elements of a list.

* Prototype: `def safe_print_list(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* `x` represents the number of elements to print
* `x` can be bigger than the length of `my_list`
* Returns the real number of elements printed
* You have to use `try: / except:`
* You are not allowed to import any module
* You are not allowed to use `len()`

**Solution:** [0-safe_print_list.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/0-safe_print_list.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#
```

## Safe printing of an integers list

Write a function that prints an integer with `"{:d}".format()`.

* Prototype: `def safe_print_integer(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
* Otherwise, returns `False`
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to import any module
* You are not allowed to use `type()`

**Solution:** [1-safe_print_integer.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/1-safe_print_integer.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./1-main.py
89
-89
School is not an integer
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#
 
```

## Print and count integers

Write a function that prints the first `x` elements of a list and only integers.

* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* `x` represents the number of elements to access in `my_list`
* `x` can be bigger than the length of `my_list` - if it’s the case, an exception will occur
* Returns the real number of integers printed
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print an integer
* You are not allowed to import any module
* You are not allowed to use `len()`

**Solution:** [2-safe_print_list_integers.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/2-safe_print_list_integers.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/root/holbertonschool-higher_level_programming/0x05-python-exceptions/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[elements]), end="")
IndexError: list index out of range
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#

```

## Integers division with debug

Write a function that divides 2 integers and prints the result.

* Prototype: `def safe_print_division(a, b):`
* You can assume that `a` and `b` are integers
* The result of the division should print on the `finally:` section preceded by `Inside result:`
* Returns the value of the division, otherwise: None
* You have to use `try: / except: / finally:`
* You have to use `"{}".format()` to print the result
* You are not allowed to import any module

**Solution:** [3-safe_print_division.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/3-safe_print_division.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#
```

## Divide a list

Write a function that divides element by element 2 lists.

* Prototype: `def list_division(my_list_1, my_list_2, list_length):`
* `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
* `list_length` can be bigger than the length of both lists
* Returns a new list (length = `list_length`) with all divisions
* If 2 elements can’t be divided, the division result should be equal to `0`
* If an element is not an integer or float:
    * print: `wrong type`
* If the division can’t be done (`/0`):
    * print: `division by 0`
* If `my_list_1` or `my_list_2` is too short
    * print: `out of range`
* You have to use `try: / except: / finally:`
* You are not allowed to import any module

**Solution:** [4-list_division.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/4-list_division.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#
 
```

## Raise exception

Write a function that raises a type exception.

* Prototype: `def raise_exception():`
* You are not allowed to import any module

**Solution:** [5-raise_exception.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/5-raise_exception.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./5-main.py
Exception raised
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#

```

## Raise a message

Write a function that raises a name exception with a message.

* Prototype: `def raise_exception_msg(message=""):`
* You are not allowed to import any module

**Solution:** [6-raise_exception_msg.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/6-raise_exception_msg.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./6-main.py
C is fun
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#
```

## Safe integer print with error message

Write a function that prints an integer.

* Prototype: `def safe_print_integer_err(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
* Otherwise, returns `False` and prints in `stderr` the error precede by `Exception:`
* You have to use `try: / except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to use `type()`

**Solution:** [100-safe_print_integer_err.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/100-safe_print_integer_err.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./100-main.py 2> /dev/null
89
-89
School is not an integer
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions#

```

# Safe function

Write a function that executes a function safely.

* Prototype: `def safe_function(fct, *args):`
* You can assume `fct` will be always a pointer to a function
* Returns the result of the function,
* Otherwise, returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`
* You have to use `try: / except:`

**Solution:** [101-safe_function.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/101-safe_function.py)

```
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# cat 101-main.py
#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
root@985e10084b49:~/holbertonschool-higher_level_programming/0x05-python-exceptions# ./101-main.py 2> /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None

```

# ByteCode -> Python #4

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

**Solution:** [102-magic_calculation.py](https://github.com/Ouyei/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/102-magic_calculation.py)

```
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
