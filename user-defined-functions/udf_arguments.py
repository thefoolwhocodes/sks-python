"""
Demonstration of Basic Syntax and rules for Positional and Keyword parameters
Demonstration of Variable length Positional arguments to function
Demonstration of default arguments
Demonstration of Keyworded (not a typo), variable-length argument list **kwargs
Demonstration of Following errors
    SyntaxError: positional argument follows keyword argument
    SyntaxError: non-default argument follows default argument
"""


# Demonstration of Basic Syntax and rules for Positional and Keyword parameters
def my_function1(var1, var2):
    print(var1, var2)


print("Example1: Demonstration of Positional parameters/arguments")
my_function1(10, 20)

print("Example2: Demonstration of Keyword parameters/arguments")
my_function1(var1=10, var2=20)
my_function1(var2=20, var1=10)

print("Example3: Demonstration of Positional followed by Keyword parameters/arguments")
my_function1(10, var2=20)

print("Example4: Error: Positional argument follows Keyword argument")
# my_function1(var1=10,20)

print("Example5: Error: got multiple values for argument 'var1'")
# my_function1(10,var1=20)


# Demonstration of Variable length Positional arguments to function
# Note: The type of variable length positional argument (args in current example) is always tuple
def my_function2(*args):
    """
    Function accepts single variable of variable length positional arguments type
    and prints the value of type of it.
    """
    print("Type of *args", type(args))
    for var in args:
        print("Values inside args:", var)
        print(type(var))


# This call will cause no error
my_function2()
# Type of *args <class 'tuple'>

# In this example tuple is passed as arguments
my_function2(1, 2, ("a", "b"), [9, 19])
# Type of *args <class 'tuple'>
# Values inside args: 1
# <class 'int'>
# Values inside args: 2
# <class 'int'>
# Values inside args: ('a', 'b')
# <class 'tuple'>
# Values inside args: [9, 19]
# <class 'list'>


def my_function3(argv, *args):
    """
    Function accepts two arguments
    argv - positional argument
    *args - variable length positional argument
    """
    if argv == "add":
        sum = 0
        for var in args:
            sum += var
        return sum
    elif argv == "mul":
        mul = 1
        for var in args:
            mul *= var
        return mul
    else:
        return None


print(my_function3("add", 1, 2, 3, 4, 5))
print(my_function3("mul", 1, 2, 3, 4, 5))
print(my_function3("sub", 1, 2, 3, 4, 5))
# Following line will not cause error
print(my_function3("add"))

# Demonstration of default arguments using two variables
def my_function4(var1=10, var2=20):
    print("Variable1:", var1, " Variable2:", var2)


# Positional parameters
my_function4()
# Variable1: 10  Variable2: 20
my_function4(30)
# Variable1: 30  Variable2: 20
my_function4(30, 40)
# Variable1: 30  Variable2: 40

# Keyword parameters
my_function4(var1=30, var2=40)
my_function4(var2=40, var1=30)
# SyntaxError: positional argument follows keyword argument
# my_function4(var1=30, 10)

# SyntaxError: non-default argument follows default argument
# def my_function5(var1,var2=10,var3):
#    print(var1,var2,var3)


# Demonstration of Keyworded (not a typo), variable-length argument list **kwargs
# Note: Type of args kwargs is dic
def my_function6(**kwargs):
    print("Type of kwargs:", type(kwargs))
    print(kwargs)


my_function6()
# Type of kwargs: <class 'dict'>
# {}
my_function6(var1=10, var2=20)
# Type of kwargs: <class 'dict'>
# {'var2': 20, 'var1': 10}


def my_function7(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


my_function7(1, 2, 3, 4, 5, 6, 7, 8, d=10, e=20, c=30)
