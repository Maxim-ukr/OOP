# # Завдання 1
# # Створіть наступні класи:
# #  Rectangle – атрибути width, height
# #  Circle – атрибути radius
# #  Triangle – атрибути a, b, c
#
# # Методи:
# #  get_perimeter()
# #  display_info()
#
# # Напишіть функцію create_figure() яка запитує у користувача
# # тип фігури та потрібні атрибути і повертає об’єкт.
# # Створіть декілька фігур, добавте їх у список та для кожної
# # викличте відповідні методи.
#
# from math import pi
# #import math
#
#
# # поліморфізм
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def display_info(self):
#         perim = self.get_perimeter()
#         print(f"Прямокутник")
#         print(f"ширина: {self.width} "
#               f"висота: {self.height} "
#               f"периметр: {perim} ")
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_perimeter(self):
#         # return 2 * math.pi * self.radius
#         return 2 * pi * self.radius
#
#     def display_info(self):
#         perim = self.get_perimeter()
#         print(f"Коло")
#         print(f"радіус: {self.radius} "
#               f"периметр: {perim} ")
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#     def display_info(self):
#         perim = self.get_perimeter()
#         print(f"Трикутник")
#         print(f"сторони: {self.a}, {self.b}, {self.c} "
#               f"периметр: {perim} ")
#
#
# def create_figure():
#     figure_type = input("Enter figure type: ")
#
#     if figure_type == 'circle':
#         radius = float(input('Enter radius'))
#         return Circle(radius)
#
#     elif figure_type == 'rect':
#         user_width = float(input("Entre width: "))
#         user_height = float(input("Enter height: "))
#         return Rectangle(width=user_width, height=user_height)
#
#     elif figure_type == 'triangle':
#         a = float(input("Enter side a: "))
#         b = float(input("Enter side b: "))
#         c = float(input("Enter side c: "))
#         return Triangle(a, b, c)
#
#     else:
#         print('Unknown figure')



# використання
# figure = create_figure()
#
# print(type(figure))
#
# if figure is not None:
# #     figure.display_info()
#
#
# figures = []
# for _ in range(3):
#     figure = create_figure()
#
#     if figure is not None:
#         figures.append(figure)
#
# print(figures)
#
# for figure in figures:
#     figure.display_info()

# __________________________________________________________
# Завдання 3
# Створіть наступні класи:
#  Car – атрибути speed
#  Bicycle – атрибути speed
#  Boat – атрибути speed
# Методи:
#  move() – виводить повідомлення про рух
# o Car – їде по шосе зі швидкістю
# o Bicycle – їде по дорозі зі швидкістю
# o Boat – пливе по воді зі швидкістю
#  check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні то в __init__ треба викикати ValueError з
# відповідним повідомленням
# o Car – від 20 до 200
# o Bicycle – від 10 до 30
# o Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у
# користувача тип транспорту та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька транспортних засобів, добавте їх у список
# та для кожної викличте відповідні методи

class Car:
    def __init__(self, speed):
        self.check_speed(speed)
        self.speed = speed

    def move(self):
        print(f"Автомобіль їде по шосе зі швидкістю {self.speed}")

    @staticmethod
    def check_speed(speed):
        if speed < 20 or speed > 200:
            raise ValueError("Швидкість не відповідає діапазону [20 .. 200].")


class Bicycle:
    def __init__(self, speed):
        self.check_speed(speed)
        self.speed = speed

    def move(self):
        print(f"Велосипед їде по дорозі зі швидкістю {self.speed}")

    @staticmethod
    def check_speed(speed):
        if speed < 10 or speed > 30:
            raise ValueError("Швидкість не відповідає діапазону [10 .. 30].")


class Boat:
    def __init__(self, speed):
        self.check_speed(speed)
        self.speed = speed

    def move(self):
        print(f"Човен пливе по воді зі швидкістю {self.speed}")

    @staticmethod
    def check_speed(speed):
        if speed < 0 or speed > 50:
            raise ValueError("Швидкість не відповідає діапазону [0 .. 50].")



def create_vehicle():
    try:
        print("Доступний транспорт: Car, Bicycle, Boat")
        vehicle, speed = input("Введіть назву транспорту та швидкість через пробєл: ").split()
        vehicle = vehicle.capitalize()
        speed = int(speed)
    except Exception as err:
        print(err)
        return

    try:
        if vehicle == "Car":
            return Car(speed)
        elif vehicle == "Bicycle":
            return Bicycle(speed)
        elif vehicle == "Boat":
            return Boat(speed)
        else:
            print("Невірно введено назву транспорту.")
    except ValueError as err:
        print(err)

vehicle = create_vehicle()

if vehicle is not None:
    vehicle.move()

