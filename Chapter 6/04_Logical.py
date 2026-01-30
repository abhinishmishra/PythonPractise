'''and,or,not'''
a = 50
v = 70
print(not(a<v))

user1 =int(input("enter num1:"))
user2 =int(input("enter num2:"))
if(user1 && user2 ):
    print("false")
elif(user1 ||  user2):
    print("True")
else:
    print("invalid")