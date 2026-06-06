# del keyword:
# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Aryan")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private(like) attributes & methods:
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_password(self):
#         print(self.__acc_pass)
# acc1 = Account("12345", "abcd")
# print(acc1.acc_no)
# print(acc1.reset_password())
# print(acc1.__acc_pass)
# class Person:
#     __name = "anonymous"
#     def __hllo(self):
#         print("hllo person")
#     def wel(self):
#         self.__hllo()
# p1 = Person()
# print(p1.wel())
# print(p1.__name)
# print(p1.__hllo())

# Inheritance
# class Car:
#     colour = "Black"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
# c1 = ToyotaCar("Audi")
# c2 = ToyotaCar("Benz")
# print(c1.name)
# print(c1.start())
# print(c1.colour)
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.name = brand
# class Audi(ToyotaCar):
#     def __init__(self, type):
#         self.type = type
# c1 = Audi("Petrol")
# c1.start()

# class A:
#     varA = "welcome to classA"
# class B:
#     varB = "welcome to classB"
# class C(A, B):
#     varC = "welcome to classC"
# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)
# class Car:
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()
# c1 = ToyotaCar("pirus", "electric")
# print(c1.type)

# Class Method:
# class Person:
#     name = "Print"
#     # def changeName(self, name):
#         #  Person.name = name OR
#         # self.__class__.name = "Apna" OR
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
# p1 = Person()
# p1.changeName("Apna")
# print(p1.name)
# print(Person.name)

# Property: (getter and setter two more decorator)
# class Student:
#     def __init__(self, ph, ch, mh):
#         self.ph = ph
#         self.ch = ch
#         self.mh = mh
        
#     # def cal_per(self):
#     #     self.percentage = str((self.ph + self.ch + self.mh)/3) + "%"
#     @property
#     def percentage(self):
#         return str((self.ph + self.ch + self.mh)/3) + "%"
# s1 = Student(98, 99, 100) 
# print(s1.percentage)
# s1.ph = 97
# print(s1.percentage)

# Polymorphism
# print(1+2)
# print("apna"+" "+"college") # concatenate
# print([1, 2, 3]+[4, 5, 6]) # merge
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def showNumber(self):
#         print(self.real, "i+", self.img,"j")
#     def __sub__(self, num2):
#         newReal = self.real - num2.real # add, sub, mul, truediv, mod(%), gt
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
# num1 = Complex(1, 3)
# num1.showNumber()
# num2 = Complex(4, 5)
# num2.showNumber()
# num3 = num1-num2
# num3.showNumber()
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)
# el1 = Employee("to monitor", "manager", "10000000")
# el1.showDetails()
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")
# en1 = Engineer("elon", 48)
# en1.showDetails()
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def __gt__(self, o2):
#         return self.price > o2.price
# o1 = Order("chips", 30)
# o2 = Order("tea", 10)
# print(o1 > o2)