'''
Program demonstrates how to take user inputs
'''

var = int(input("Please enter the number to be checked for even/odd"))
print(type(var))
if var % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")