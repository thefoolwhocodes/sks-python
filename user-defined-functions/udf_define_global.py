'''
Following program demonstrates that global_var_1 will only come into existence when function my_function is called.
If we comment the call to function, we will get error as 'global_var_1' is not defined
'''
def my_function():
    global global_var_1
    global_var_1 = 10

#my_function()
print (global_var_1)
