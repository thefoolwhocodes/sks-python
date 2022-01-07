"""
While Else examples
"""

# Program to find if a given number is prime or not.
# A number is prime that cannot be divided by any other number except 1 and itself.
# Program demonstrates that when break condition executes, it scopes up to else.
number = int(input("Enter a number to be checked for prime:"))
count = 2
while count < number/2 + 1:
    if number % count == 0:
        print("Number is not prime")
        break
    count += 1
else:
    print("Number is prime")


# Program demonstrates that when break condition executes, it scopes up to else.
# In other words, in below program, else will not execute, if break executes.
count = 0
while count < 10:
    print("Inside while: %d" % count)
    count += 1
    if count == 5:
        break
else:
    print("Inside else: %d" % count)

# Else will be executed when the condition of while becomes false.
count = 0
while count < 5:
    print("Inside while: %d" % count)
    count += 1
else:
    print("Inside else: %d" % count)
