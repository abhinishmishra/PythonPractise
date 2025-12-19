s = {1,2,3,4,1234,1,2,3,4}
s.pop()
print(s)
print(s.remove(4))
print(s)
print(s.add(5))
print(s)
print(type(s))
s={}
print(type(s))

# set union or intersection
s1 = {1,2,4,5,6}
s2 = {7,8,9,1,2,4}
print(s1.union(s2))
print(s1.intersection(s2))