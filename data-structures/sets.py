# Sets
# Unordered Collection
# Mutable (does not have hash value)
# No duplicate elements
# Can hold elements of different data types
# Can only hold elements of immutable data types
# Mutable data types like list cannot be used as an element
# Uses: Membership testing and eliminating duplicate entries
# Supports Mathematical operations like Union, intersection, difference and symmetric difference

# To create sets, set() or curly braces with few elements can be used.
var = set()
print(type(var))
# <class 'set'>

# Elements with different data types inside the set
var = {1, 2, "shashi",(1,2,3)}
print(var)
# {1, 2}
print(type(var))
# <class 'set'>

for i in var:
    print(i)
    print(type(i))


set_a = {1, 2, 3, 4}
set_b = {1, 2, 5}

# Union: Element from both the sets
print(set_a | set_b)
# {1, 2, 3, 4, 5}
print(set_a.union(set_b))
# {1, 2, 3, 4, 5}

# Intersection: Elements that are common in both
print(set_a & set_b)
# {1, 2}
print(set_a.intersection(set_b))
# {1, 2}

# Difference: A - B is a set of elements that are only in A
# bot not in B
print(set_a - set_b)
# {3, 4}
print(set_a.difference(set_b))
# {3, 4}

# Symmetric Difference: Elements in A or B but not in both
print(set_a ^ set_b)
# {3, 4, 5}
print(set_a.symmetric_difference(set_b))
# {3, 4, 5}