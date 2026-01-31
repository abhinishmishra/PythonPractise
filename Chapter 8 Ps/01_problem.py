# wap use function to find greatest of three no:

def greatestnum(a,b,c):
    if(a>b and a>c):
        print(f"a value is greater {a}")
    elif(b>c and b>a):
        print(f" b value is greater {b}")
    else:
        print(f"c is greater{c}")
a = int(input('enter a:'))
b = int(input('enter b:'))
c= int(input('enter c:'))
greatestnum(a,b,c)