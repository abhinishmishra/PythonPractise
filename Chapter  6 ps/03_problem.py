'''A spam comment is defined as a text:
"make a lot of money"
"Buy now"
"subsribe this"
"click this",   WAP  to detect these spams'''

p1 = "make a lot of money"
p2= "Buy now"
p3="subsribe this"
p4 = "click this"
message = input("enter your comment: ")

if((p1 in message)or (p2 in message) or (p3 in message)or (p4 in message)):
    print("This comment is SPAM")
else:
    print("this is not SPAM")