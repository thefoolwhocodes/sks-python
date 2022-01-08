'''
Following program demonstrates that statement following to return statement is never executed.
'''

def my_function():
    print "This is first statement"
    print "This is second statement"
    return;
    print "This statement will never execute"

var = my_function();
print var
print type(var) 
