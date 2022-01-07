"""
While Else examples
Program demonstrates that when break condition executes, it scopes up to else.
"""

# Program to find if a given number is prime or not.
# A number is prime that cannot be divided by any other number except 1 and itself.
number = int(input("Enter a number to be checked for prime:"))
count = 2
while count < number/2 + 1:
    if number % count == 0:
        print("Number is not prime")
        break
    count += 1
else:
    print("Number is prime")
