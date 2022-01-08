'''
Following program demonstrates the simple usage of user defined function. 
'''

def my_function():
    '''
    Following program does not return anything.
    Return type is None
    '''
    print "Inside user defined function my_function"
    print "Inside user defined function, second statement"


my_function() # It calls the function
print my_function() # Call the function and print its return value using print

var = my_function() # Call the function and capture its return value in an identifier
print var # Print the value of var captured in last statement
print type(var) # Print type of the var
