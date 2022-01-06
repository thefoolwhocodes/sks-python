'''
Examples demonstrates evaluated False value in conditions
'''

# Booleans
if False:
    print("False is True")
else:
    print("False is not True")
# True

# Number int
if 0:
    print("0 is True")
else:
    print("0 is False")
# 0 is False

# Number float
if 0.0:
    print("0.0 is True")
else:
    print("0.0 is False")
# 0.0 is False

# String
if "":
    print("Empty string is True")
else:
    print("Empty string is False")
# Empty string is False

# Tuple
if ():
    print("Empty tuple is True")
else:
    print("Empty tuple is false")
# Empty tuple is false

# List
if []:
    print("Empty list is True")
else:
    print("Empty list is False")
# Empty list is False

# Dictionary
if {}:
    print("Empty dictionary is True")
else:
    print("Empty dictionary is False")
# Empty dictionary is False

