
Revise /home/santosh/Python/Day6/udf_arguments.py and continue with the remaining at this file.


# lambda - user defined function, which is anonymous
# accepting multiple values/parameters but return single object

def check_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

print(list(map(check_prime, range(2, 10))))
print(list(filter(check_prime, range(2, 10))))

# Step 1 - Fetch each and every value in iterable
# Step 2 - Apply the function
# Step 3 - Return Original value for which function is True


"""
def cube(x):
    return x ** 3

print(list(map(lambda x: x**3, range(1, 10))))

def add(a, b):
    return a + b

add = lambda a, b: a + b # thats a syntax of above user defined function
add(10, 20)

def add(a, b):
    if a > b:
        return a + b
    else:
        return a - b

add = lambda a, b: a + b if a > b else a - b # thats a syntax of above user defined function


def checkarguments(a, b , *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)

checkarguments(1, 2, 3, 4, 5, 6, 7, 8, d = 10, e= 20, c = 30)


"""



