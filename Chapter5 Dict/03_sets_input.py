#taking user input in set 

s ={}
name = input("Enter name:")
ss = set(name)
print(ss)
print(type(ss))

name = 'Raju'
age = "45"
gender = 'M'
Graduation = "MSc"

n = input("enter multiple numbers:")
student ={}
for j in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age:"))
    student[name] = age
print(student)