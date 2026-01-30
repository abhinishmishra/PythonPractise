'''Check a uername is less 10 character by userinput 
'''
username = input("Enter Name: ")
length = len(username)
if(length<=10):
    print("valid name")
else:
    print("invalid because more than 10 character")