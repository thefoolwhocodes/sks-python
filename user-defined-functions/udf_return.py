"""
Following program demonstrates that statement following to return statement is never executed.
"""


def my_function():
    print("This is first statement")
    return;
    print("This statement will never execute")


var = my_function();
print(var)
# None
print(type(var))
# <class 'NoneType'>
