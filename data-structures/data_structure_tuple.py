# tuple
# Immutable collection, value cannot be changed.
# Allows duplicate values.
# Items can be indexed.
# Items are ordered, means items have a definite order and that
# order will not change.

employee1 = ('Shashi', 35, 1)
employee2 = ('Rahul', 25, 1)
print(type(employee1))
# <class 'tuple'>
print(employee1[0])
# Shashi
print(employee1[-1])
# 1
print(employee1 + employee2)
# ('Shashi', 35, 1, 'Rahul', 25, 1)
print(employee1 * 2)
# ('Shashi', 35, 1, 'Shashi', 35, 1)
print(employee1 > employee2)
# True

print('Shashi' in employee1)
# True
print(5 in employee1)
# False

# tuple of tuples
employee = (employee1, employee2)
print(employee)
# (('Shashi', 35, 1), ('Rahul', 25, 1))
print(employee[0])
# ('Shashi', 35, 1)
print(employee[0][0])
# Shashi

# Following line of code will give object assignment error
# employee[0][0] = 'shashi'
# 'tuple' object does not support item assignment

# tuple of lists
employee = (['San', 38],['Kant', 2])
print(employee)
# (['San', 38], ['Kant', 2])
print(employee[0])
# ['San', 38]
print(employee[0][0])
# San

# In Tuple of lists, tuple cannot be modified
# Following line of code will cause assignment error
# employee[0] = ['abc' , 20]
# TypeError: 'tuple' object does not support item assignment

# In Tuple of lists, individual lists can be modified
employee[0][0] = 'Man'
print(employee[0])
# ['Man', 38]

# Single element tuple need to have a trailing comma, to be considered it
# as a tuple, else it is treated as a string (if member element is string)
my_tuple = ('shashi')
print(my_tuple)
# shashi
print(type(my_tuple))
# <class 'str'>
my_tuple = ('shashi',)
print(my_tuple)
# ('shashi',)
print(type(my_tuple))
# <class 'tuple'>

# Single element int example
my_tuple = (5)
print(type(my_tuple))
# <class 'int'>