'''Wap to find the name present in list or not'''

list = ['joya', 'soya','mona','raju','ranjeet','aman','amit']
name = input("enter name which u finding in list:")
if(name in list):
    print(name, "is present in list")
else:
    print("Not present in list")