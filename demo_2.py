
# Functions
# help - get the documentation of specified module, class, function, variables etc
# help(print)
# help(range)
# help(map)

# dir - returns list of the attributes and methods of any object
# dir(int)

# ord - Converts a character into its Unicode code value
# ord('s')

# chr - returns the character that represents the specified unicode
# chr(115)

# len - calulate len of in iterable object
# len('1234')

# range(start, stop, step) - Returns an object of type <class 'range'> that can be used to get
# sequence of numbers, starting from 0 by default
# and increments by 1 by default and stops at specified number (Exclusive)

# Find object's type
var = int()
type(var)
# <class 'int'>

var = 10
type(var)
# <class 'int'>

varFloat = 10.1
type(varFloat)
# <class 'float'>


# Identity of an object
# Every object that is created is given a number that uniquely identifies it.
# It is guaranteed that no two objects will have the same identifier during any period in which their lifetimes overlap.
# Once an object’s reference count drops to zero and it is garbage collected, then its identifying number becomes available
# and may be used again.
# help(id)

# In the following code we can see that id of the object int is same in both the runs.
id(1)
# 10915168
id(1)
# 10915168

# In the following example we can see that when the variable a is re-assigned the value 10, id becomes same.
a = 10
id(a)
# 10915456
a = 300
id(a)
# 140525377609200
a = 10
id(a)
# 10915456


# Complex type
a = 3 + 4j
type(a)
# <class 'complex'>

print(a.real)
# 3.0
print(a.imag)
# 4.0

realVar = 2
imaginaryVar = 5
complexVar = complex(realVar, imaginaryVar)
print(complexVar)
# (2+5j)


# Operators
# Arithmetic operations
# +, -, *, /, **, //, %
# Addition
10 + 5
# 15

# Subtraction
10 - 5
# 5

# Multiplication
2 * 2
# 4

# Division
a = 5 /2
print(a)
# 2.5
type(a)
# <class 'float'>

# Floor division
a = 3//2
print(a)
# 1
type(a)
# <class 'int'>

# Modulus
10 % 3
# 1

# Exponentiation
2 ** 3
# 8

# Evaluation order https://docs.python.org/3/reference/expressions.html#evaluation-order
res = 10 ** 2 + 3 * 2
print(res)
# 106

res = 10 ** ( 2 + 3 ) * 2
print(res)
# 200000

# Conversion
# Binary representation of an integer
# help(bin)
res = bin(3)
print(res)
# 0b11

# Binary to Decimal
res = int( '1101', 2 )
print(res)
# 13

# Binary to Octal
res = int('1101', 8)
print(res)
# 577

# Binary to Hexa Decimal
res = int('1101', 16)
print(res)
# 4353


# Bitwise operators for binary numbers
# &, |, ^, ~, <<, >>


# Comparison operators
# ==, !=, >, <. >=, <=
10 == 10
# True
10 != 10
# False
10 > 10
# False
10 < 10
# False
10 >= 10
# True
10 <= 10
# True


# Identity operators
# is, is not
# is operator evaluates to true if the variables on either side
# of the operator point to the same object.

# In following example var1 is var2 will return True if 300 is not
# garbage collected
var1 = 300
print(id(var1))
var2 = 300
print(id(var2))
print(var1 == var2)
print(var1 is var2)
#140207124544432
#140207124544432
#True
#True

# In following example var3 and var2 both are pointing to same
# object
var3 = var2
print(id(var3))
print(id(var2))
print(var3 is var2)
# 140176422051504
# 140176422051504
# True

# In following example var3 and var2 both are pointing to same
# object
name = 'Shashi'
another_name = 'Shashi'
print(name is another_name)
# True
print(name is not another_name)
# False

# Membership operators
# in, not in
print('as' in 'shashi')
# True
print('as' not in 'shashi')
# False

# int
print(dir(int))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
a = 10
b = 20
print(a.__add__(b))


# str
print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

name = 'Shashi'
lastname = "Santosh"
class_name = ''' Python '''
print(type(name))
print(type(lastname))
print(type(class_name))

filename = 'C:\name\test\file.txt'
print(filename)
filename = r'C:\name\test\file.txt'
print(filename)

filename = 'C:\\name\\test\\file.txt'
print(filename)

print(name + lastname)
print(name + ' ' + lastname)
print(name * 2)

# Comparison operators are overloaded
# ==, !=, <, >, <=, >=
print('shashi' > 'Shashi')
# True
# Reason is ord('s') that is 115 is greater than ord('S') 83
print(ord('s'))
# 115
print(chr(115))
# s

# Indexing Positive and Negative indexing
name = 'shashi'
print(name[0])
# s
print(name[0])
# s
print(name[-6])
# s
print(name[5])
# i
print(name[-1])
# i

statement = 'This is Python second class'
# print last element
print(statement[len(statement)-1])
# s

# print second last element
print(statement[len(statement)-1])
# s

print(statement[0:4:1])
# This

print(statement[0:4:2])
# Ti

print(statement[0:4:3])
# Ts

print(statement[0:4:4])
# T

print(statement[8:15:1])
# 'Python '

# Default step is 1
print(statement[8:14])

# Default start is 0
print(statement[:14])
# This is Python

# Default start is 0 and end is len of object
print(statement[:])
# This is Python second class

print(statement[::2])
# Ti sPto eodcas

# Reverse order
print(statement[::-1])
# ssalc dnoces nohtyP si sihT

print(statement[2:6:-1])
# ''

print(statement[2::-1])
# ihT

print(statement[-1:-5:-1])
# ssal