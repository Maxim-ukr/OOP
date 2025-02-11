# Class

# Опис класу

# class Dog:
#     # атрибути
#     name = "Lef"
#     age = 2
#     weight = 5
#
#     # можливість гавкати
#     # метод
#     def make_sound(self):
#         print("Gav!")
#
# dog1 = Dog()
#
# print(dog1.name)
# print(dog1.age)
#
# dog1.make_sound()

# ____конструктор класу
# class Dog:
#     # конструктор для створення об'єктів класу
#     def __init__(self, name, age, weight):
#         # self -- обєкт класу(конкретний пес)
#         if age < 0:
#             raise ValueError("вік пса неможе бути від'ємні")
#
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     # можливість гавкати
#     # метод
#     def make_sound(self):
#         print("Гав")
#
#
#     def print_info(self):
#         # вивід інформації про песика
#         print(self.name, self.age, self.weight)
#
#
#     def rename(self, new_name):
#         # зміна імені песика
#         self.name = new_name
#
#     dog = Dog('Carl', 5, 10)
#     dog.print_info()
#
#     dog.rename("Петро")  # self = dog,  new_name = "Петро"
#     dog.print_info()
#
#     # line.replace(',', ' ')
#     #
#     # def replace(self, old, new):


# _______________________________
# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def print_info(self):
#         print(f"Імя: {self.name}, вік: {self.age}")
#
# student1 = Student("Andry", 22)
#
# student1.print_info()

# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def print_info(self):
#         print(f"Імя: {self.name}, вік: {self.age}")
#
# students = []
#
# for _ in range(3):
#     name, age = input("Введіть імя та вік студента в строчку через пробіл: ").split()
#
#     student = Student(name, age)
#     students.append(student)
#
#
# for student in students:
#     student.print_info()

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

# class Circle():
#
#     def __init__(self, radius):
#         self.radius = radius
#
#
#     def sqear(self):
#         return self.radius * 3.14
#
# rad = int(input("Введіть радіус кола: "))
#
# cercul1 = Circle(rad)
#
# area1 = cercul1.sqear()
#
# print(f"Площа кола з радіусом {rad} дорівнює {area1}")

# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

# class BankAccount():
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, sum):
#         if self.balance >= amount:
#           self.balance -= sum
#         else:
#             print("Недостатньо грошей.")
#
#     def print_info(self):
#         print(f"На рахунку {self.owner} баланс складає {self.balance}")
#
# account1 = BankAccount("Ivan", 300)
# account1.print_info()
#
# account1.deposit(100)
# account1.print_info()
#
# account1.withdraw(21)
# account1.print_info()

# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready

# class Car():
#     def __init__(self, brand, year, is_ready=False):
#         self.brande = brand

