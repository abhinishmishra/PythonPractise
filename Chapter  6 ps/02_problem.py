'''WAP check student passed or fail it require a total of 40% and at least 33% in each
subject Assume 3 subject and take input from the user'''

marks1 = int(input("enter marks1:"))
marks2 = int(input("enter marks2:"))
marks3 = int(input("enter marks3:"))
sum = marks1+marks2+marks3
percentage = sum/3

if(percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("You are Pass")
else:
    print("you are fail")