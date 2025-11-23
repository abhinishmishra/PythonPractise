
#list are mutable means changeable

friends = ["apple",'orange', 44, 44.5, False ,'Rohan']
print(friends)
print(type(friends))
print(friends[0])
print(friends[0:])

friends[0] = "grapes"
print(friends[0])
print(friends)

#list slicing same sa string
print(friends[1:1:5])

#add removing in list
friends.append("Abhinish")
print(friends)

l1 = [84,5,56,3,6,4,31,1]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(0,333)
print(l1)

print(l1.pop(1))
print(l1)

l1.remove(1)
print(l1)

#Quick Example Using Most Used Methods
lst = [3,1,4]

lst.append(2)       # [3,1,4,2]
lst.remove(1)       # [3,4,2]
lst.insert(1, 10)   # [3,10,4,2]
lst.sort()          # [2,3,4,10]
print(lst.pop())    # 10
print(len(lst))     # 3
print(sum(lst))     # 9
print(lst.count(2)) # 1
