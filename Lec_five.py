# Loops :-
# count = 1 
# while count <= 5 :
#     print("hello")
#     count += 1
# print(count)
# i = 1
# while i <= 200 :
#     print("Aryan", i)
#     i+=1
# print(i)

# Print numbers from 1 to 5
# i = 5
# while i >= 1 :
#     print(i)
#     i-=1
# print("loop ended")
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1
# i = 100
# while i >= 1 : # stopping cond
#     print(i)
#     i -= 1
# i = 1
# n = int(input("enter no. : "))
# while i <= 10 :
#     print(n*i)
#     i += 1
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx +=   1
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36 
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("find at i", i)
#         break
#     i += 1

# Break and continue :-
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# i = 0
# while i <= 50:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
# Loops
# list = [1, 2, 3, 4]
# for val in list :
#     print(val)
# tup = (1, 3, 4, 2, 5, 6, 3)
# for val in tup:
#     print(val)
# str = "Aryan"
# for char in str :
#     print(char)
# str = "Aryan"
# for char in str :
#     if(char == 'r'):
#         print("r found")
#         break
#     print(char)
# else:
#     print("end")
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in list:
#     print(val)
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 64
# idx = 0
# for el in tup:
#     if(el == x):
#         print("no found at idx ", idx)
#     idx += 1
# Range:-
# seq = range(5)
# for i in seq:
#     print(i)
# #oR
# for i in range(11):
#     print(i)
# for i in range(12,99):
#     print(i)
# for i in range(22,33,2): # range(start,stop,step)
#     print(i)
# for i in range(2,100,2):
#     print(i)
# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)
# n = int(input("enter no: "))
# for i in range(1,11):
#     print(n*i)
# Pass statement :-
# for i in range(5):
#     pass
# print("Aryan")

# n = 5 

# sum = 0
# for i in range(1, n+1):
#     sum += i

# print("total sum =", sum)

# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum+=i
#     i += 1
# print(sum)

# n = 5 
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)