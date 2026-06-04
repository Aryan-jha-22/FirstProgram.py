# Function definition
# def calc_sum(a, b): # a & b are called parameters
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(677, 999) # Function call ; a & b are called arguments
# def print_hello():
#     print("hello")
# print_hello()
# avg of 3 no.
# def avg_cal(a, b, c):
#     avg = (a + b + c)/3
#     print(avg)
#     return avg
# avg_cal(20, 30, 40)
# print("Welcome", end = " ")
# print("Aryan")

# Default parameters
# def cal_product(a=1, b=1):
#     product = a*b
#     print(product)
#     return product
# cal_product()
# cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
# def len_of_cities(cities):
#     print(len(cities))
#     return len(cities)
# len_of_cities(cities)
# OR
# def print_len(list):
#     print(len(list))
#     return len(list)
# print_len(cities)
# cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
# print(cities[0], end = " ") 
# print(cities[1])
# cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
# heroes = ["Iron Man", "Spider Man", "Super Man", "Batman"]
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(cities)
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)
# def converter(usd_value):
#     inr_value = usd_value * 95
#     print(usd_value, "USD =", inr_value, "INR")
# converter(4)
# def even_odd(num):
#     if(num%2 == 0):
#         print("Even")
#     else:
#         print("Odd")
# even_odd(6)

# Recursion and loops are interconnected.
# def show(n):
#     if(n == 0): # Base case
#         return
#     print(n)
#     show(n-1)
#     # print("END")
# show(6)
# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     return fact(n-1)*n
# print(fact(5))
# def fun(n):
#     if(n == 0):
#         return 0
#     return fun(n-1) + n
# print(fun(5))
# def print_list(list, index):
#     if(index== len(list)):
#         return
#     print(list[index])
#     print_list(list, index + 1)
# cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
# print_list(cities, 0)