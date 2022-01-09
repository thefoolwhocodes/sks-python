import sympy

'''
var2 = 10
def function(var1):
    global var3
    var3 = 20
    global var2
    var2=50
    print var3
    print var2
    print "Passed value is:", var1
    return 1

function(10)
print var2
print var3
'''

'''
def function(var1,var2):
    print var1,var2

function(10,var2=30)
#function(var1=10,20)
'''

'''
def function(var1=10,var2=20):
    print var1,var2

function()
function(1)
function(2,3)
function(var2=100,var1=50)
'''

'''
def function(var1,var2=10,var2):
    print var1
'''

'''
def function(*items):
    print type(items)
    print items

function(1,2,3)
function([1,2,3])
'''

'''
def function(**kwargs):
    print type(kwargs)
    print kwargs

function()    
function(one=1,two=2,three=3)
'''

'''
def function(a,b,*c,**d):
    print a
    print b
    print c
    print d 

#function(1,2,3,4,5,6,7,8,a=10,b=20,c=30)
function(1,2,3,4,5,6,7,8,d=10,e=20,c=30)
'''


'''
def add(a,b):
    return a+b
add = lambda a,b: a+b
print add(10,20)

def conditionalAdd(a,b):
    if a > b:
        return a+b
    else:
        return a-b
condiotionalAdd = lambda a,b: a+b if a > b else a-b
print condiotionalAdd(7,10)
print condiotionalAdd(17,10)
'''

def isPrime(var):
    for a in var
        count=1
        while a%2==0
            return True
        


print map(lambda a: True if isprime(a) else False , range(1,10))



