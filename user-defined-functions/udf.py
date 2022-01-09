"""
Following program demonstrates the simple usage of user defined function.
"""


def my_function_return_none():
    """
    Following program does not return anything.
    Return type is None
    """
    print("Inside user defined function my_function")


my_function_return_none() # It calls the function
print(my_function_return_none()) # Call the function and print its return value using print
# None

var = my_function_return_none() # Call the function and capture its return value in an identifier
print(var) # Print the value of var captured in last statement
# None
print(type(var)) # Print type of the var
# <class 'NoneType'>
