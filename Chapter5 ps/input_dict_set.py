s = set()
user = input("enter num1: ")
s.add(user)
user2 = input("enter num2: ")
s.add(user2)
print(s)


name = input("Enter name: ")
age = int(input("Enter age: "))

student = {
    "name": name,
    "age": age
}

print(student)

#✅ Example 2: Multiple Inputs Using Loop
n = int(input("How many students? "))

students = {}

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    students[name] = age

print(students)

#Enter numbers: 1 2 3 3 4 5
#✅ Example 2: Take list input and convert to set
values = input("Enter values: ").split()
s = set(values)
print(s)
