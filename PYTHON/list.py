# list is mutable sequence of value 

marks = [1,2,3,4,5,5]

print(marks)
print(marks[0])
print(marks[0:4])
print(len(marks))

marks[3] = 34

print(marks)
print(type(marks))

#  list methods:

marks.append(5656)
print(marks)

marks.insert(2,56)
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)


for i in range(len(marks)):

    if(marks[i] == 5):
        print(i)
        break




#  practice problem :

info = [
    ("alice", "math"),
    ("bob", "science"),
    ("alice", "science"),
    ("charlie", "math"),
    ("bob", "english"),
    ("charlie", "english"),
]


unique_courses = set()





for val in info :
    unique_courses.add(val[1])
print(unique_courses)



for name , course in info:
    print(name, course)


for name,course in info:
    if(course == "english"):
        print(name)


dict = {}

for name , course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)


print(dict)  