
s = {1, 2, 3, 3}
print(s)   # output: {1,2,3}
s = {1, 2}
s.add(3)
s.remove(2)

#📌 5. Loop Through Set
s = {"apple","banana","kiwi"}
for x in s:
    print(x)
#📌 7. Frozen Set (Immutable Set)
fs = frozenset([1,2,3])
