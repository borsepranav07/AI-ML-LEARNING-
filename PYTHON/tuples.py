# tuples are immutable :

tup = (1,2,3,4,5,6,7)

print(tup)
print(type(tup))
print(len(tup))
print(tup[2])
print(tup[0:3])

# tup[3] = 10

for val in tup:
    print(val)


print(tup.index(4))
print(tup.count(2))