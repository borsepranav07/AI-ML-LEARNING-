age = 22

if(age>18):
    print("vote")
    print("you can vote")
else:
    print("not vote")

color = "eer"

if(color == "red"):
    print("stop")
elif(color == "green"):
    print("go")
elif(color == "yellow"):
    print("look")
else:
    print("wrong color")


age = 14
if(age<13):
    print("child")
elif(age >=13 and age<=18):
    print("teenager")
else:
    print("adult")


username = input("enter username : ")
password = input("enter password : ")

if(username == "admin"  and password == "password"):
    print("Login succesful")
elif(username != "admin"):
    print("wrong username")
else:
    print("wrong password")



num = 33
if(num%5 == 0):
    print("multiple of 5")
else:
    print("not a multiple of 5")

if(num%2 == 0):
    print("nums is even")
else:
    print("num is odd")



# nesting :

username = input("enter username : ")
password = input("enter password : ")

if(username == "admin"  and password == "pass"):
    print("Login succesful")
else:
    if(username != "admin"):
        print("wrong username")
    else:
        print("wrong password")
 


