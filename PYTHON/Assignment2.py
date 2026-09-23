"""

# q1.

salary = int(input("enter the salary : "))

if(salary < 30000) :
    tax = 5*salary/100
elif(salary >30000 and salary < 70000) :
    tax = 15*salary/100
else:
    tax = salary*25/100

print("salary : " , salary)
print("tax " , tax)




# q2.

def int(a,b) :
    for i in range(a,b,2):
        print(i)

print(int(2,20))

# q3.

def digits(n):

    while(n>0):
        a=n%10
        n=n//10

        print(a,"    ")

print(digits(12323))


# q4.


def count(n):

    cnt = 0


    while(n>0):
        a=n%10
        n=n//10

        cnt = cnt+1

        print(a,"    ")
    print(cnt)

print(count(123231212))


# q5.

def sum(n):

    sum = 0


    while(n>0):
        a=n%10
        n=n//10

        sum = sum+a

    
    print(sum)

print(sum(1234))




# q6.

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)
"""

# q7.

while True:
    n = input("Enter a number or 'Quit' to exit: ")

    if n == "Quit":
        break

    n = int(n)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")


# q8.

def calculator(a,b,operation):

    if(operation=="+"):
        print(a+b)
    elif(operation=="-"):
        print(a-b)
    elif(operation=="*"):
        print(a*b)
    else:
        print(a/b)


calculator(1,2,"+")


# q9

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(10))



# q10.


secret_number = 25

while True:

    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct! You guessed it.")
        break


