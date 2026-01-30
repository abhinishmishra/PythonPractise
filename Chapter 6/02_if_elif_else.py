age  = int(input('enter your age:')) 
if(age>=18):
    print("Adult")
elif(age<0):
    print("You are entering invalid age")
elif(age==0):
    print("You are entering 0 invalid age")
else:
    print("child")