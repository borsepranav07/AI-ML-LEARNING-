word = "string"
word2 = "stir"

print(word)
print(word+word2)
print(word+" "+word2)

print(word2[2])
print(word[0:3])
print(word[0:])
print(word[0:len(word)])

for ch in word:
    print(ch)


#  string formating :

# 1. format function :
a = 2
b = 4

sum = a+b

print("sum is {}".format(sum))
print("sum is {} and {} is {}".format(a,b,sum))
print("language is {}".format("python"))

# index based formating
print("sum is {1} and {0} is {2}".format(a,b,sum))


# valuse based formating :

print("values of variables {a} & {b}".format(a=5, b=10))





# 2. f-string:

q = 2
r = 45

print(f"sum of {q} & {r} is {q+r}")

