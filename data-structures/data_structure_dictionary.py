# dictionary
# Ordered in 3.6+ versions (random iteration order)
# Mutable
# Stores mappings of unique key to values.
# Key can only be Immutable value.

employee = {}
print(type(employee))
# <class 'dict'>

# Following example demonstrates that duplicate values are replaced.
# There are totally 5 elements that are inserted but as one is duplicate key, hence
# the same is replaced. That's why the length of the dictionary is four and the older value
# is replaced with the new value.
employee1 = {'name':'Shashi', 'age':35, 'managers_name':'Mohan', 'location':'Pune', 'name':'Santosh'}
print(len(employee1))
# 4
print(employee1)
# {'name': 'Santosh', 'age': 35, 'location': 'Pune', 'managers_name': 'Mohan'}
print(employee1['name'])
# Santosh

# Override value
employee1['name'] = 'Kant'
print(employee1)
# {'name': 'Kant', 'age': 35, 'location': 'Pune', 'managers_name': 'Mohan'}

# Add new Key value pair
employee1['Name'] = 'Ravi'
print(employee1)
# {'name': 'Kant', 'age': 35, 'Name': 'Ravi', 'location': 'Pune', 'managers_name': 'Mohan'}

# Remove a key value pair
del employee1['managers_name']
print(employee1)
# {'name': 'Kant', 'age': 35, 'Name': 'Ravi', 'location': 'Pune'}

# List cannot be used as a key because it is mutable
# Following line of code will give error
# employee1[[1,2,3]] = 'Mohan'
# TypeError: unhashable type: 'list'

# tuple can be used as a key because it is immutable
employee1[(1,2,3)] = 'Mohan'
print(employee1)
# {'name': 'Kant', 'age': 35, 'Name': 'Ravi', 'location': 'Pune', (1, 2, 3): 'Mohan'}

# + operator is not supported because it does not make sense to add two dictionaries
# Following line of code will give error
# employee1 + employee1
# unsupported operand type(s) for +: 'dict' and 'dict'

# Identity
employee1 = {'name': 'Aakash', 'age': 35, 'location': 'Pune', 'Name': 'Aakash', (1, 2, 3): 'Mohan'}
employee2 = employee1
print(id(employee1))
# 140439925743112
print(id(employee2))
# 140439925743112
print(employee1 is employee2)
# True

# Membership
print('age' in employee1)
# True
print('Aakash' in employee1)
# False

# Dictionary of dictionary
employee1 = {1:{'name':'Jatin', 'age':35}, 2:{'name':'Rohan', 'age':25}}
print(employee1[2]['name'])
# Rohan