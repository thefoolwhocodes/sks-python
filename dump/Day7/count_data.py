'''
Following program counts the line, word and characters in a given file.
We can validate the same in the given file using "wc"
    santosh@docker:~/Python/Day7/DataFiles$ wc data.txt 
     5 20 75 data.txt
'''

print("Example1")
abs_path=input("Please enter a filename!")
fh=open(abs_path,"r")
line_count,word_count,character_count = 0,0,0

for line in  fh.readlines():
    line_count+=1
    word_count+=len(line.split(" "))
    character_count+=len(line)
print("line count:",line_count)
print("word count:",word_count)
print("character count",character_count)


print("Example2:With Context Manager")
fh.seek(0)
line_count,word_count,character_count = 0,0,0
with open(abs_path,"r") as fh:
    for line in  fh.readlines():
        line_count+=1
        word_count+=len(line.split(" "))
        character_count+=len(line)
    print("line count:",line_count)
    print("word count:",word_count)
    print("character count",character_count)

