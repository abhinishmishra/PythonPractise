'''file creating by with '''
# str = "Hello This is student record data"
# with open("Student.txt",'w') as f:
#     f.write(str)

'''read file'''
# with open("student.txt",'r') as f:
#     print(f.read())

'''append file'''
# str1 = "101 Aman United_University"
# with open("student.txt",'a') as f:
#     print(f.write(str1))

'''Read line again because new line are skipped above program to 
coorect in a good manner'''
with open("student.txt", "r") as f:
    content = f.read()
    print(content)

# Jaha capital letter se naam start hota hai, waha newline daal do (example logic)
fixed = content.replace("101", "\n101").replace("data","\ndata")

with open("student.txt", "w") as f:
    f.write(fixed)

print("File Fixed Successfully")
