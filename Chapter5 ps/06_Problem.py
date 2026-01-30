'''Create a empty dictionary. Allow 4 friend to enter their favourte language as a value use key as their name. Assume that the name are unique.'''

s = {}
name = input("enter name1:")
language = (input("enter fav lang: "))
s.update({name:language})
name = input("enter name2:")
language = (input("enter fav lang: "))
s.update({name:language})
name = input("enter name3:")
language = (input("enter fav lang: " ))
s.update({name:language})
name = input("enter name4:")
language = (input("enter fav lang: "))
s.update({name:language})

print(s)