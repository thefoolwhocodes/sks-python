
'''
Demonstration of Basic Syntax and rules for Positional and Keyword parameters
'''
print("----------------------Example set 1----------------------")
def my_function1(var1,var2):
    print(var1,var2)

print("Example1: Demonstration of Positional parameters/arguments")
my_function1(10,20) 

print("Example2: Demonstration of Keyword parameters/arguments")
my_function1(var1=10, var2=20)
my_function1(var2=20, var1=10) 

print("Example3: Demonstration of Positional followed by Keyword parameters/arguments")
my_function1(10, var2=20)

print("Example4: Error: Positional argument follows Keyword argument")
#my_function1(var1=10,20)

print("Example5: Error: got multiple values for argument 'var1'")
#my_function1(10,var1=20)


'''
Demonstration of passing variable number of positional arguments to function
Note: Type of args is tuple 
'''
print("----------------------Example set 2----------------------")
def my_function2(*args):
    '''
    Function accepts single variable of variable length positional arguments type
    and prints the value of type of it.
    '''
    print("Typef of *args",type(args))
    for var in args:
        print("Values inside args:", var)
        print(type(var))

my_function2() #This call will cause no error
my_function2(1,2,3,4,("a","b","c","d"),[9,19,12,34])


def my_function3(argv,*args):
    '''
    Function accepts two arguments
    argv - positional argument
    *args - variable length positional argument
    '''
    if argv=="add":
        sum=0
        for var in args:
            sum+=var
        return sum
    elif argv=="mul":
        mul=1
        for var in args:
            mul*=var
        return mul
    else:
        return None

print(my_function3("add",1,2,3,4,5))
print(my_function3("mul",1,2,3,4,5))
print(my_function3("sub",1,2,3,4,5))
print(my_function3("add")) # This line will cause not error

'''
Demonstration of default arguments
'''
print("----------------------Example set 3----------------------")
def my_function4(var1=10,var2=20):
    print("Variable1:", var1 ," Variable2:", var2)

#Positional parameters
my_function4()
my_function4(30)
my_function4(30,40)

#Keyword parameters
my_function4(var1=30,var2=40)
my_function4(var2=40,var1=30)
#SyntaxError: positional argument follows keyword argument
#my_function4(var1=30,10)

#SyntaxError: non-default argument follows default argument
#def my_function5(var1,var2=10,var3):
#    print(var1,var2,var3)


'''
Demonstration of keyworded, variable-length argument list
Note: Type of args is dic
'''
print("----------------------Example set 4----------------------")
def my_function6(**kwargs):
    print("Type of kwargs:", type(kwargs))
    print(kwargs)

my_function6()
my_function6(var1=10,var2=20)


def my_function7(a, b , *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)

my_function7(1, 2, 3, 4, 5, 6, 7, 8, d = 10, e= 20, c = 30)
