
# 1. Write a Python program to print all natural numbers from 1 to n.
n = int(input('Enter a number: '))
for i in range(1, n+1):
    print(i)

# 2. Write a Python program to print all natural numbers in reverse (from n to 1)
n = int(input('Enter a number: '))
print("Solution 1")
for i in reversed(range(1, n+1)):
    print(i)
print("Solution 2")
for i in range(n, 0, -1):
    print(i)

# 3. Write a Python program to print all alphabets from a to z.
for i in range(ord('a'), ord('z')+1):
    print(chr(i))

for i in range(97, 97+26):
    print(chr(i))

# 4. Write a Python program to print all even numbers between 1 to 100.
for num in range(1, 100):
    if not num%2:
        print("Number %1d is even" % (num))

for num in range(2,100,2):
    print("Number %1d is even" % (num))

# 5. Write a Python program to print all odd number between 1 to 100.
for num in range(1, 100):
    if num%2:
        print("Number %1d is odd" % (num))

for num in range(1, 100, 2):
    print("Number %1d is odd" % (num))

# 6. Write a Python program to find sum of all natural numbers between 1 to n.
natural_sum = 0
for num in range(1,100):
    natural_sum += num;
print(natural_sum)
# 4950

# 7. Write a Python program to find sum of all even numbers between 1 to n.
even_sum = 0
for num in range(2,100,2):
    even_sum += num
print(even_sum)
# 2450

# 8. Write a Python program to find sum of all odd numbers between 1 to n.
odd_sum = 0
for num in range(1,100,2):
    odd_sum += num
print(odd_sum)
# 2500

# 9. Write a Python program to print multiplication table of any number.
num = 2
for i in range(1,11):
    print(num * i)

n = int(input('Enter a number: '))
for i in range(n, n*10+1, n):
    print(i)

# 10. Write a Python program to count number of digits in a number.
# First way (Integer input)
number = int(input('Enter a number: '))
count = 0
temp_number = number
while temp_number > 0:
    temp_number = int(temp_number / 10)
    count += 1
print('Total number of digits are: %d' % count)

# Second way (String input)
number = input('Enter a number: ')
count = 0
for i in number:
    count += 1
print('Total number of digits are: %d' % count)

# 11. Write a Python program to find first and last digit of a number (String input)
number = input('Enter a number: ')
print("First digit: %s , Last digit: %s" % (number[0], number[-1]))

# 12. Write a Python program to find sum of first and last digit of a number (String input)
number = input('Enter a number: ')
sum_number = int(number[0]) + int(number[-1])
print("Sum of first digit and last digit: %d" % sum_number)

# 13. Write a Python program to swap first and last digits of a number.
number = input('Enter a number: ')
new_number = number[-1] + number[1:-1] + number[0]
print("Swapped: %s" % new_number)

# 14. Write a Python program to calculate sum of digits of a number
# First way (Integer input)
number = int(input('Enter a number: '))
temp_holder = number
number_sum = 0
while temp_holder > 0:
    number_sum += temp_holder % 10
    temp_holder = int(temp_holder / 10)
print(number_sum)

# Second way (String input)
number = input('Enter a number: ')
number_sum = 0
for i in number:
    number_sum += int(i)
print(number_sum)

# 15. Write a Python program to calculate product of digits of a number.
number = int(input('Enter a number: '))
temp_holder = number
number_prod = 1
while temp_holder > 0:
    number_prod *= temp_holder % 10
    temp_holder = int(temp_holder / 10)
print(number_prod)

# Second way (String input)
number = input('Enter a number: ')
number_prod = 1
for i in number:
    number_prod *= int(i)
print(number_prod)

# 16. Write a Python program to enter a number and print its reverse.
number = int(input('Enter a number: '))
temp_holder = number
reversed_number = 0
while temp_holder > 0:
    ind_digit = temp_holder % 10
    reversed_number = reversed_number * 10 + ind_digit
    temp_holder = int(temp_holder / 10)
print(reversed_number)

# Second way (String input)
number = input('Enter a number: ')
print(int(number[::-1]))

# 17. Write a Python program to check whether a number is palindrome or not.
number = int(input('Enter a number: '))
temp_holder = number
reversed_number = 0
while temp_holder > 0:
    ind_digit = temp_holder % 10
    reversed_number = reversed_number * 10 + ind_digit
    temp_holder = int(temp_holder / 10)
if number == reversed_number:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

# Second way (String input)
number = input('Enter a number: ')
if number == number[::-1]:
    print('Number is palindrome')

# 18. Write a Python program to find frequency of each digit in a given integer.
number = int(input('Enter a number: '))
frequency_dict = {}
# Or following can be used to create dictionary variable
# frequency_dict = dict()
temp_holder = number
while temp_holder > 0:
    ind_digit = temp_holder % 10
    temp_holder = int(temp_holder / 10)
    if ind_digit in frequency_dict:
        frequency_dict[ind_digit] += 1
    else:
        frequency_dict[ind_digit] = 1
print(frequency_dict)

#19. Write a Python program to find a power of 2 of each number using for loop.
number = input('Enter a number: ')
new_number = str()
for i in number:
    new_number += str(int(i) ** 2)
print(new_number)

# 20. Write a Python program to print all ASCII character with their values.
digit = 0
while digit <= 255:
    print("%d = %c" %(digit, chr(digit)))
    digit += 1