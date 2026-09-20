def hello():
    print("hello")
    print("hello python")

hello()

def sum(a,b):
    print(a+b)

sum(9,4)

def sum(a,b):
    return a+b
print(sum(9,4))

# types of functions :

# lambda functions :

sum = lambda a,b:a+b

print(sum(4,5))




# factorial :

def factorial(n):

    fact = 1
    i=1
    while(i<=n):
        fact = fact * i
        i += 1

    return fact

print(factorial(5))

def factorial(n):

    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact




print(factorial(4))

