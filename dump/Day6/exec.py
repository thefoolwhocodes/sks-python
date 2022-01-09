Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, start=0, /)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function
This is second statement in function
This is first statement in function
This is second statement in function
None
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function
This is second statement in function
This is first statement in function
This is second statement in function
None
This is first statement in function
This is second statement in function
None
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function
This is second statement in function
This is first statement in function
This is second statement in function
String
This is first statement in function
This is second statement in function
String
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function 10
This is second statement in function
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 6, in <module>
    function() # it call the function
TypeError: function() missing 1 required positional argument: 'var1'
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 7, in <module>
    function() # it call the function
TypeError: function() missing 1 required positional argument: 'var1'
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function 10
This is second statement in function
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 8, in <module>
    print(var1)
NameError: name 'var1' is not defined
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
40
This is first statement in function 10
This is second statement in function
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
Inside function:  50
This is first statement in function 10
This is second statement in function
Outside function:  40
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
Inside function:  50
This is first statement in function 10
This is second statement in function
Outside function:  50
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 6, in <module>
    function(10, 20) # positional parameters/arguments
TypeError: function() missing 1 required positional argument: 'var3'
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function 10
This is second statement in function 20
This is first statement in function 20
This is second statement in function 10
This is first statement in function 10
This is second statement in function 20
This is first statement in function 20
This is second statement in function 10
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function 10
This is second statement in function 20
This is first statement in function 20
This is second statement in function 10
This is first statement in function 10
This is second statement in function 20
This is first statement in function 20
This is second statement in function 10
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 11, in <module>
    function(10, var1=20) # runtime error
TypeError: function() got multiple values for argument 'var1'
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
This is first statement in function 20
This is second statement in function 10
This is first statement in function 1
This is second statement in function 10
This is first statement in function 10
This is second statement in function 20
This is first statement in function 60
This is second statement in function 50
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
()
(1,)
(1, 2)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
()
(1,)
(1, 2)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
()
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 8, in <module>
    function(a = 1)
TypeError: function() got an unexpected keyword argument 'a'
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
{'one': 10}
{'one': 10, 'two': 2}
{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
Traceback (most recent call last):
  File "/Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py", line 8, in <module>
    checkarguments(1, 2, 3, 4, 5, 6, 7, 8, a = 10, b= 20, c = 30)
TypeError: checkarguments() got multiple values for argument 'a'
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
1
2
(3, 4, 5, 6, 7, 8)
{'d': 10, 'e': 20, 'c': 30}
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
[1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
[1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
[True, True, True, False, True, False, True, False, False]
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
[True, True, False, True, False, True, False, False]
>>> 
 RESTART: /Users/jatinmiglani/Dropbox/8th Dec 19 Pimple - Python/Day 6/first.py 
[True, True, False, True, False, True, False, False]
[2, 3, 5, 7]
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str
    
    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.

>>> 'jatin'.capitalize()
'Jatin'
>>> 'Yatin'.capitalize()
'Yatin'
>>> help(str.center)
Help on method_descriptor:

center(...)
    S.center(width[, fillchar]) -> str
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> account = '8323456789876543'
>>> account[-4:].center(16, 'X')
'XXXXXX6543XXXXXX'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 

