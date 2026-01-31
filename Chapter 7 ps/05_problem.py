#wap to of factorial

num = int(input("enter num: "))
product = 1
for i in range(1, num+1):
    product = product*i
print(f"the factorial of {num} is {product}")