#can we have a set with 18int and '18' str as a value in it: "yes" or "not" 

s = set()
s.add(19)
s.add('19')
print(s)
print(type(s))









s = set()
user = input("enter num1: ")
s.add(user)
user2 = input("enter num2: ")
s.add(user2)
print(s)