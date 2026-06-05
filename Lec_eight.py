# class Student: # Here Student is class name
#     name = "Aryan Jha"
#     def __init__(self, fullname):
#         self.name = fullname
        
#         print("adding new student in database..")
# s1 = Student("Aryan")
# print(s1.name)
# print(s1.name)
# s2 = Student()
# print(s2.name)
# class Car:
#     colour = "Blue"
#     brand = "Mercedes"
# c1 = Car()
# print(c1.colour)
# print(c1.brand)
# class Car:
#     Car_company = "AUDI"
#     brand = "HIT"
#     def __init__(self, brand, colour):
#         self.brand = brand # obj att > class att (if both preference is same)
#         self.colour = colour
#         print("info about car")
# c1 = Car("Audi", "Black")
# print(c1.brand, c1.colour)
# print(c1.Car_company)
# class Student:
#     college_name = "APNA COLLEGE"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         return self.marks
# s1 = Student("Aryan", 97)
# s1.welcome()
# print(s1.get_marks())
# class Student:
#     def __init__(self, name, marks): 
#         self.name = name
#         self.marks = marks
#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "ur average marks is: ", sum/3)
# s1 = Student("Aryan", [97, 98, 99])
# s1.avg_marks()
# s1.name = "ironman"
# s1.marks = [300, 200, 100]
# s1.avg_marks()

# STATIC METHOD:
# class Student:
#     @staticmethod
#     def college():
#         print("Apna college")
# s1 = Student()
# s1.college()
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.acc = True
#         self.brk = True
#         self.clutch = True
#         print("car started....")
# c1 = Car()
# c1.start()

# class Account:
#     def __init__(self, balance, acc):
#         self.balance = balance
#         self.acc = acc
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("total bal =", self.get_balance())
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.",amount,"is credited")
#         print("total bal =", self.get_balance())
#     def get_balance(self):
#         return self.balance
# acc1 = Account(11000, 1234)
# acc1.debit(1000)
# acc1.credit(5000)
# acc1.credit(60000)