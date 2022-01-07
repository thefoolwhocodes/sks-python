"""
continue example:
Print 1 to 10 but skip 5
"""
print("continue example")
count=0
while count<10:
    count+=1
    if count == 5:
        continue
    print("Value: %d" % count)

"""
break example:
Print 1 to 4
"""
print("break example")
count = 0
while count<10:
    count += 1
    if count == 5:
        break
    print("Value: %d" % count)

"""
pass:
    Can be used indented block
    Interpreter does nothing
"""
print("pass example")
count = 6
if count == 5:
    print("Count is 5")
else:
    pass

# Empty class using pass
class Example:
    pass

# Empty function using pass
def function(args):
    pass