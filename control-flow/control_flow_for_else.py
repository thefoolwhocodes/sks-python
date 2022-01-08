"""
For Else examples
"""

# Program demonstrates that when break condition executes, it scopes up to else.
# In another words, in below program, else will not execute, if break executes.
number = 8
for i in range(1,number):
    if i == 6:
        print("Going to break at i: %d" % i)
        break
else:
    print("Inside else")
# Going to break at i: 6

# Find whether the number is prime or not
number = int(input("Enter the number to be checked for prime"))
for i in range(2, int(number/2) + 1):
    if not number % i:
        print("Number is not prime")
        break
else:
    print("Number is prime")

# Find out prime numbers between 1 and 100
for i in range(2, 100):
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            break
    else:
        print('Number %d is prime' % i)
