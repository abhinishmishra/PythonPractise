a = (1,2,3.5,4,5,5,False,'rohan')
print(a)
print(type(a))

no = a.count(5)
print(no)

i = a.index(5)
print(i)


t = (1, 2, 2, 3, 4)
print(t.count(2))    # 2
print(t.index(3))    # 3
print(len(t))        # 5
print(min(t))        # 1
print(max(t))        # 4
print(sum(t))        # 12
print(2 in t) #true
print(5 in t) #False 


# Convert list to tuple
lst = [5,6,7]
t2 = tuple(lst)
print(t2)            # (5,6,7)

#Tuples, like lists and strings, support indexing and slicing.
#Basic Slicing Syntax
'''t[start:stop:step]
start → index to start (inclusive, default 0)
stop → index to end (exclusive)
step → step size (default 1)'''
t = (10, 20, 30, 40, 50)

print(t[0])   # 10 (first element)
print(t[-1])  # 50 (last element)


print(t[1:4])    # (20, 30, 40) → from index 1 to 3
print(t[:3])     # (10, 20, 30) → from start to index 2
print(t[2:])     # (30, 40, 50) → from index 2 to end
print(t[-3:])    # (30, 40, 50) → last 3 elements
print(t[::2])    # (10, 30, 50) → every 2nd element
print(t[::-1])   # (50, 40, 30, 20, 10) → reversed tuple