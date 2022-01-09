employee = {'name': 'Aakash', 'age': 35, 'location': 'Pune', 'Name': 'Aakash', (1, 2, 3): 'Mohan'}

# Remove the item from dictionary using key
del employee['location']
print(employee)
# {'name': 'Aakash', 'age': 35, (1, 2, 3): 'Mohan', 'Name': 'Aakash'}
print(employee)
# {'name': 'Aakash', 'age': 35, (1, 2, 3): 'Mohan', 'Name': 'Aakash'}

# Get list of keys present in dictionary
list_of_keys = list(employee)
print(list_of_keys)
# ['name', 'age', (1, 2, 3), 'Name']

# Get tuple of keys present in dictionary
tuple_of_keys = tuple(employee)
print(tuple_of_keys)
# 'name', 'age', (1, 2, 3), 'Name')

# Using Dictionary items.
# Items returns a set like object that gives view of dictionary items
employee = {'name': 'Akash', 'age': 35, (1, 2, 3): 'Mohan'}
def print_dict_items():
    for i in employee.items():
        print(i)
print_dict_items()
