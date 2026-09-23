# =========================
# PYTHON SET AND METHODS
# =========================

# Creating a set
s = {1, 2, 3, 4, 5}

print("Original set:", s)
print("Type:", type(s))
print("Length:", len(s))


# 1. add()
s.add(6)
print("After add(6):", s)


# 2. remove()
s.remove(6)
print("After remove(6):", s)


# 3. discard()
s.discard(5)
print("After discard(5):", s)


# 4. pop()
x = s.pop()
print("Element removed by pop():", x)
print("After pop():", s)


# Add elements again for further operations
s.add(5)
s.add(6)


# Creating another set
b = {4, 5, 6, 7, 8}

print("\nSet A:", s)
print("Set B:", b)


# 5. union()
print("Union:", s.union(b))


# 6. intersection()
print("Intersection:", s.intersection(b))


# 7. difference()
print("Difference (A - B):", s.difference(b))


# 8. symmetric_difference()
print("Symmetric Difference:", s.symmetric_difference(b))


# 9. issubset()
a = {4, 5}

print("\nIs A subset of B:", a.issubset(b))


# 10. issuperset()
print("Is B superset of A:", b.issuperset(a))


# 11. isdisjoint()
c = {10, 20, 30}

print("Is B disjoint with C:", b.isdisjoint(c))


# 12. clear()
c.clear()
print("After clear():", c)