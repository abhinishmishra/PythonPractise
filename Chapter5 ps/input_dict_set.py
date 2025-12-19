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


values = input("Enter values: ").split()
s = set(values)
print(s)
