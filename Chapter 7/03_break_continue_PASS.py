"""Break, continue, pass"""

for i in range(10):
    if(i==8):
        break
    print(i)
print()

""", continue, """
for i in range(10):
    if(i==2):
        continue
    print(i)

"""pass"""

for i in range(50):
    pass

i = [2,3,4,3]
if(3 in i):
    print("present 3")
else:
    print("not present 3")