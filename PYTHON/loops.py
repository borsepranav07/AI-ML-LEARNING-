# # while loop
# j=0


# i=0
# while(i<=5):
#     print(i)
#     i += 1



# # break 

# i=1
# while(i<=10):

#     if(i%6==0):
#         break
#     print(i)
#     i += 1


# # continue :

# i=1
# while(i<=10):

#     if(i%3==0):
#         i+=1
#         continue
#     print(i)
#     i += 1



# i=0
# while(i<=10):
#     print(i)
#     i += 2




# # for loops :

# string = "hello"

# for var in string:
#     print(var)


# if 'o' in string:
#     print("o exist in string")

# for i in range(23):
#     print(i)

# for i in range(13):
#     print("hello world")



# word = "artificial"
# i=0
# for var in word:
#     print(var)
#     i+=1

# print(i)

# i=0

# for var in word:
#     if(var == 'i'):
#         print(var)
#         i+=1

# print(i)





word = "artificial"

count = 0
for ch in word:
    if(ch == 'a' or ch =='e' or ch == 'i' or ch =='o' or ch =='u'):
        count+=1

print(count)





# range function :

for i in range(0,23,2):
    print(i)


sum =0
for i in range(5):
    sum += i

print(sum)
