# string are immutable

s = "Banana"
print(s.find("a"))
print(s.count("a"))
print(s.replace("a","o"))

#methods
print("length of s is:",len(s))
print("length of s is:",min(s))
print("length of s is:",max(s))

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())


print(s.endswith("b"))
print(s.startswith("b"))


data = "a,b,c"
print(data.split(","))  # ['a','b','c']

words = ['Hello', 'Python']
print(" ".join(words))  # Hello Python

'''scape	Meaning
\n	New line
\t	Tab space
\'	Single quote
\"	Double quote
\\	Backslash'''

print("this is \n\"double\" quote")
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\'World")
print("Hello\\World")

#f-string (Best & Modern)
name = "Abhinish"
age = 21
print(f"My name is {name} and I am {age} years old")

print("Hello {}, your age is {}".format(name, age))


s = 'abhinish hello world'
index = s.find('abhinish')
print(index)



