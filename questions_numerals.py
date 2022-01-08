# 10. Write a Python program to count number of digits in a number.


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