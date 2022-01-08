# List
# Mutable
# Created using square brackets
# Multiple items in single variable
# List allows duplicate values
# Ordered (random iteration order)
# Need not be homogeneous, single list can contain different data types

employee = ['Shashi', 35, 'Pune', '9527354004']
print(employee[0])
# Shashi
print(employee[-0])
# Shashi
print(employee[-4])
# Shashi
print(employee[-1])
# 9527354004

employee[0] = 'Santosh'
print(employee)
# ['Santosh', 35, 'Pune', '9527354004']

# Prints value from 0 to 9
# Returns a range object which provides value from 0 to 9
range_var = range(10)
for x in range_var:
    print(x)
print(type(range_var))
# <class 'range'>

# Prints value from 1 to 9
range_var = range(1, 10)
for x in range_var:
    print(x)

print(list(range(1, 10, 2)))
# [1, 3, 5, 7, 9]

print(list('Python'))
# ['P', 'y', 't', 'h', 'o', 'n']

numbers1 = list(range(1, 5))
print(numbers1)
# [1, 2, 3, 4]
numbers2 = list(range(4, 10))
print(numbers2)
# [4, 5, 6, 7, 8, 9]
print(numbers1 + numbers2)
# [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
print(numbers1.__add__(numbers2))
# [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
print(numbers1 * 2)
# [1, 2, 3, 4, 1, 2, 3, 4]
print(list(range(-1, -6, -1)))
# [-1, -2, -3, -4, -5]
print(numbers1 > numbers2)
# False
print(len(numbers1))
# 4
print(['Shashi'] > ['shashi'])
# False

numbers1 = list(range(1, 5))
numbers2 = numbers1
print(id(numbers1))
# 139757846054408
print(id(numbers2))
# 139757846054408
print(numbers1 is numbers2)
# True

# Modifying the list object is reflected in both the variables
# numbers1 and numbers2
numbers1[0] = 10
print(numbers1)
# [10, 2, 3, 4]
print(numbers2)
# [10, 2, 3, 4]

# In the following example variable numbers1 is assigned to another
# object [30, 40, 50], hence doing any change via numbers1 will have no effect
# on the object numbers2 is pointing to.
numbers1 = [30, 40, 50]
numbers1[0] = 100
print(numbers1)
# [100, 40, 50]
# [30, 40, 50]
print(numbers2)
# [10, 2, 3, 4]
print(id(numbers1))
# 139757846054792
print(id(numbers2))
# 139757845558984


# del
# delete a number at specified index of list
numbers = [30, 40, 50]
del numbers[0]
print(numbers)
# [40, 50]


names1 = ['Aakash', 'Mohan', 'Rajiv', 'Ricky', 'Vijay']
names2 = names1
print(id(names1))
# 139757846027720
print(id(names2))
# 139757846027720
print(names1 is names2)
# True
print(names1 == names2)
# True
names3 = ['Aakash', 'Mohan', 'Rajiv', 'Ricky', 'Vijay']
print(id(names3))
# 139757846013768
print(names1 is names3)
# False
print(names1 == names3)
# True


# List of Lists
employee1 = ['Shashi', 37]
employee2 = ['Ravi', 45]
employee3 = ['Mom', 70]
employees = [employee1, employee2, employee3]
print(employees)
# [['Shashi', 37], ['Ravi', 45], ['Mom', 70]]
print(employees[0])
# ['Shashi', 37]
print(employees[0][0])
# Shashi
print(employees[0][0][0])
# S
print(employees[-1])
# ['Mom', 70]
print(employees[-1][-1])
# 70


# List of Lists of Lists
employees = [['Jatin', 35, ['Pune', 'Bangalore']], ['Mohan', 25, ['Delhi']]]
print(employees)
# [['Jatin', 35, ['Pune', 'Bangalore']], ['Mohan', 25, ['Delhi']]]
print(employees[0][2][1])
# Bangalore

# Following code will give error because string is immutable
# 'str' object does not support item assignment
# employees[0][2][1][0] = 'd'

# index based assignment cannot be used to insert new items
# it can be only used to update or delete items
list1 = [1,2,3]
# Following code will give error
# IndexError: list assignment index out of range
# list1[3] = 4


employee1 = ['Shashi', 37]
employee2 = ['Ravi', 45]
employee3 = ['Mom', 70]
employees = [employee1, employee2, employee3]
print(employee1)
# ['Shashi', 37]
print(employees)
# ['Shashi', 37], ['Ravi', 45], ['Mom', 70]]
employee1[0] = 'Yatin'
print(employees)
# [['Yatin', 37], ['Ravi', 45], ['Mom', 70]]

# Assigning the employee1 variable to new object will have no effect
# on employees
employee1 = ['aakash', 20]
print(employees)
# [['Yatin', 37], ['Ravi', 45], ['Mom', 70]]

# Reassignment to employees object fetches new object details and hence values
# for variable
employees = [employee1, employee2, employee3]
print(employees)
# [['aakash', 20], ['Ravi', 45], ['Mom', 70]]

# Remove variable employee1
del employee1
print(employees)
# [['aakash', 20], ['Ravi', 45], ['Mom', 70]]