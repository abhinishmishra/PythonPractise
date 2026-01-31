#Recursion is a function which calls itself

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
n = int(input("enter N: "))
print(f"the factorial is :{factorial(n)}")