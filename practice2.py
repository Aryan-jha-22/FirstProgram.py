# i = 33
# while i <= 133:
#     print("i am aryan jha", i)
#     i += 1
# i = 100
# while i >= 0:
#     print(i)
#     i -= 1
# i = 1
# n = int(input("Enter a number: "))
# while i <= 20:
#     print(n*i)
#     i += 1
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# i = 0
# while i < len(num):
#     if num[i] == x:
#         print("Found at index:", i)
#     i += 1
# i = 1
# while i <= 10:
#     print(i)
#     if(i == 8):
#         break
#     i += 1
# i = 10
# while i >= 1:
#     print(i)
#     if(i == 8):
#         break
#     i -= 1
# i = 1
# while i <= 70:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)
# str = "Apna College"
# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)
# info = (1, 6, 8, 9, 5, 4, 3, 2, 7)
# x = 7
# idx = 0
# for el in info:
#     if(el == x):
#         print("no found at idx ", idx)
#     idx += 1
#     print(el)
# for i in range(12, 34, 3):
#     print(i)
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n*i)
# n = 6
# sum = 0
# i = 1
# while i <= n:
#     sum+=i
#     i += 1
# print(sum)
# n = 5 
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum =", sum)
# n = 5 
# sum = 1
# for i in range(1, n+1):
#     sum *= i
# print("total sum =", sum)
# def cal_sum(a, b):
#     sum = a+b
#     print(sum)
#     return
# cal_sum(4, 5)
# def cal_sum(a, b, c):
#     sum = (a + b + c)/3
#     print(sum)
#     return
# cal_sum(5, 6, 7)
# print("HI", end = " ") # (" ") --> works as /t
# print("Aryan")
# print("HI", end = "\n")
# print("Aryan")
# def cal_sum(a=1, b=1):
#     sum = a+b
#     print(sum)
#     return
# cal_sum()
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)