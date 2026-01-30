''' give the grade according to the marks '''
sub1= int(input("Enter marks1: "))
sub2= int(input("Enter marks2: "))
sub3= int(input("Enter marks3: "))
sub4= int(input("Enter marks4: "))
sub5= int(input("Enter marks5: "))
sum = sub1+sub2+sub3+sub4+sub5
marks = sum//5
print("percentage of 5 subject total marks =",marks,'%')

if(marks<=100 and marks>=90):
    print("Excellent")
elif( marks<=90 and marks>=80):
    print("A")
elif(marks>=70 and marks<=80):
    print("B")
elif(marks>=60 and marks<=70):
    print("C")
elif(marks>=50 and marks<=60):
    print("D")
else:
    print("Fail")