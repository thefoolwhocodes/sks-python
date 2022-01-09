
file_name=input("Please enter file name!")
infile=open("/home/santosh/Python/Day7/"+file_name,"r")

line_count=0
word_count=0
character_count=0

for i in infile.readlines():
    line_count +=1
    word_count+=len(i.split(" "))
    character_count = character_count+len(i)
#    for data in i.split(" "):
#       character_count=character_count+len(data)

print("Line count:",line_count)
print("Word count:",word_count)
print("Word count:",character_count)    
