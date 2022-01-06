# Two syntax of if else.

'''
First syntax.
'''
var = None
print("Syntax 1 example 1")
if var:
    print("True")
else:
    print("False")
# False

print("Syntax 1 example 2")
if var is None:
    print("False")
else:
    print("True")
# False

'''
Second syntax.
Note:
This if syntax can only be used with single line statements
return This if CONDITION else return that
'''
print("Syntax 2 example 1")
print(True if var else False)
# False

print("Syntax 2 example 2")
print(False if var is None else True)
# False

# if else if
numbers = list(range(0,10))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_len = len(numbers)
print(numbers_len)
# 10

if numbers_len > 10:
    print("Length of numbers is greater than 10")
elif numbers_len == 10:
    print("Length of numbers is exactly 10")
else:
    print("Length of numbers is less than 10")
# Length of numbers is exactly 10

# if else nested
# Question: If length of numbers is greater than 10
# print whether first number is odd or even
numbers = list(range(0,11))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_len = len(numbers)
print(numbers_len)
# 11
if numbers_len > 10:
    print("Length of numbers is greater than 10")
    if numbers[0]%2 is 0:
        print("Number is even:" + str(numbers[0]))
    else:
        print("Number id odd:" + str(numbers[0]))
else:
    print("Length of numbers is less than or equal to 10")
# Length of numbers is greater than 10
# Number is even