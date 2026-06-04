# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()
# f = open("demo.txt", "r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()
# f = open("demo.txt", "w")
# f.write("I am Aryan")
# f.close()
# f = open("demo.txt", "a")
# f.write("\nI wanna go to goa")
# f.close()
# f = open("sample.txt", "w")
# f.close()
# f = open("demo.txt", "r+") # no truncate
# f.write("abc")
# print(f.read())
# f.close()
# f = open("demo.txt", "w+") # truncate
# f.write("abc")
# print(f.read())
# f.close()
# With Syntax
# with open("demo.txt", "r") as f: # f.close(not necessary here)
#     data = f.read()
#     print(data)
# Deleting a file
# import os
# os.remove("demo.txt")
# f = open("demo.txt", "w")
# f.write("ayz")
# f.close()
# f = open("practice.txt", "w")
# f.write("HI everyone.\nwe are learning file I/O.\nusing java.\nI like programming in java ")
# f.close()
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("java", "Python")
# print(new_data)
# with open("practice.txt", "w") as f:
#     data = f.write(new_data)
# def check_for_words():
#     x = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(x)):
#             print("found")
#         else:
#             print("not found")
# check_for_words()
# def check_for_line():
#     x = "learning"
#     data = True
#     line_no = 1 
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(x in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(num)
#             num = ""
#         else:
#             num += data[i]
# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()
# num = data.split(",")
# for val in num:
#     if(int(val)%2 == 0):
#         count += 1
# print(count)