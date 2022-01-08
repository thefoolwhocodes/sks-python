'''
Following program demonstrates that
    Example1:Variables that are only referenced inside a function, are implicitly global.
    Example2:Even if we try to reassign value to a global variable, from inside the function, its existence is only scoped to the function, that is the global 
        varaible's value is not changed.
    Example3:If we want to overwrite global variable, we need to explicitly use global keyword from inside the function.
'''

print("Example1")
my_var1=1
def my_function1():
    print(my_var1)
my_function1()


print("Example2")
my_var2=1

def my_function2():
    my_var2=2
    print(my_var2)

print(my_var2)
my_function2()
print(my_var2)


print("Example3")
my_var3=1
print("Id:",id(my_var3))

def my_function3():
    global my_var3
    my_var3=2
    print(my_var3)

print(my_var3)
my_function3()
print(my_var3)
print("Id:",id(my_var3))

