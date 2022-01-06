#1. Write a Python program to print all natural numbers from 1 to n.
n = int(input('Enter a number: '))
for i in range(1, n+1):
    print(i)

#2. Write a Python program to print all natural numbers in reverse (from n to 1)
n = int(input('Enter a number: '))
print("Solution 1")
for i in reversed(range(1, n+1)):
    print(i)
print("Solution 2")
for i in range(n, 0, -1):
    print(i)
