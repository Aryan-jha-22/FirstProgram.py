marks = [74.4, 45.6, 87.5, 86.7, 98.7]
print(len(marks))
print(type(marks))
print(marks[0], marks[1])
student = ["karn,", 98.5, "delhi"]
print(student[0])
student[0] = "arjun"
print(student)
stages_of_human_life = ["infant", "child", "teenager", "adult", "old"]
print(stages_of_human_life[2])
print(stages_of_human_life[2:4])
# List Methods
list = [8, 5, 5, 4, 7, 3]
list.append(9)
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(3,1)
print(list)
list = [8, 5, 5, 4, 7, 3]
list.remove(5)
print(list)
list = [8, 5, 5, 4, 7, 3]
list.pop(4)
print(list)


# Tuples in Python
tup = (2, 1, 3, 1) 
print(type(tup))
print(tup[0])
# Tuple Methods
tup = (2, 3, 1, 8)
print(tup.index(3))
print(tup.count(1))

# Practice Questions
movie1 = input("enter ur favourite movie: ")
movie2 = input("enter ur second favourite movie: ")
movie3 = input("enter ur third favourite movie: ")
movies = []
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

list1 = [1, 2, 1]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("list1 is palindrome")
else:
    print("not palindrome")

grades = ("C", "D", "A", "A", "B")
print(grades.count("A"))

list = ["C", "D", "A", "A", "B"]
list.sort()
print(list)