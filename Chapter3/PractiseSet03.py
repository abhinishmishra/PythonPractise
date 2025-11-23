 #1️⃣ Write a python program to display a user entered name followed by Good Afternoon using input() function.
user = input("enter name ")
print(f"Good Afternoon {user}")
print("Good Afternoon",user)

# 2️⃣ Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Abhinish").replace("|Date|","06 November 2050 "))

# 3️⃣ Write a program to detect double space in a string.
name = "abhinish  is a good boy and"
print(name.find("  "))


# 4️⃣ Replace the double space from problem 3 with single spaces.

name = "abhinish  is a good boy and"
print(name.replace("  ", " "))
print(name)

# 5️⃣ Write a program to format the following letter using escape sequence
letter = "Dear Abhinish,\n this python course is nice.\nThanks!"
print(letter)
 