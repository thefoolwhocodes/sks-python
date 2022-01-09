
infile=open("/home/santosh/Python/Day7/data.txt","w")
my_dict=dict()

def load_data():
    cont=True
    while cont:
        data=infile.readline().split()
        my_dict.add[data[0]] = data[1]
    print(my_dict)

def valid_user():
    uid=input("Please enter user id")

def add_user():
    uid=input("Please enter user id")
    pwd=input("Please enter password")
    uid_pwd=uid+","+pwd
    infile.write(uid_pwd+"\n")
    infile.flush()

def update_pwd():
    uid=input("Please enter user id")

def remove_user():
    uid=input("Please enter user id")

load_data()

while True:
    choice=input("Please enter choice!")
    if(choice=="add"):
        add_user()
    elif(choice=="update"):
        update_pwd
    elif(choice=="remove"):
        remove_user
    elif(choice=="validate"):
       er()
