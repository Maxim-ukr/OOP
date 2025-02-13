# Class
from itertools import filterfalse


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

# _____________________DZ__________________________

# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

# class Cart():
#     def __init__(self, client, items):
#         self.client = client
#         self.items = items
#
#     def add(self, item):
#         self.items.append(item)
#
#     def delleting(self, item):
#         if item in self.items:
#             self.items.remove(item)
#
#     def print_cart(self):
#         print(f"У клієнта {self.client} в кошику наступний товар: ")
#         for item in self.items:
#             print(item)
#
# item = ['apple']
#
# user1 = Cart("User1", item)
#
# user1.add('banana')
# user1.add('apricot')
# user1.add('carrot')
#
# user1.print_cart()
#
# user1.delleting("watermellon")
# user1.delleting("carrot")
#
# user1.print_cart()

# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон
#
# class Phone():
#     def __init__(self, number, battery_level):
#         self.number = number
#         self.battery_level = battery_level
#
#
#     def battery_lower(self, vidsotok):
#         if self.battery_level < vidsotok:
#             print(f"Неможливо зменьшити заряд на {vidsotok}%, оскільки в телефоні вже меньше заряду.")
#         else:
#             self.battery_level -= vidsotok
#             print(f"Заряд зменшено на {vidsotok}%.")
#             if self.battery_level < 20:
#                 print(f"Заряд телефону меньше ніж 20%, а саме {self.battery_level}%")
#
#
# tel1 = Phone("+380XX-YYY-OOOO", 30)
#
# print(f"{tel1.number, tel1.battery_level}")
#
# vidsotok = int(input("Введіть наскільки відсотків сів аккумулятор: "))
#
# tel1.battery_lower(vidsotok)
#
# print(f"{tel1.number, tel1.battery_level}")

# ______________________________________________________________________
#
# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису

# class Project:
#     def __init__(self, name, budget, tasks):
#         self.name = name
#         self.budget = budget
#         self.tasks = tasks
#
#         self.expenses = 0
#         self.is_finished = False
#         self.spent_time = 0  # місяці
#
#     def display_info(self):
#         print(f"Проєкт {self.name}")
#         print(f'Час виконання {self.spent_time} місяців')
#         print(f'Витрачено {self.expenses}/{self.budget}$')
#         print(f'Залишилось {self.budget - self.expenses}$')
#
#         if self.is_finished: # якщо проект завершений
#             print("Стан проекту: завершений")
#         else:
#             print("Стан проекту: незавершений")
#
#             print('Задачі що залишились:')
#             for task in self.tasks:
#                 print(f'   - {task}')
#         print()
#         print()
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def divide_task(self, task, subtasks):
#         if task not in self.tasks:
#             print(f'Немає такої задачі {task}')
#             return
#
#         # задача є в списку задач self.tasks
#         self.tasks.remove(task)
#
#         self.tasks += subtasks
#
#     def do_task(self, task, duration, price):
#         # чи є така задача
#         if task not in self.tasks:
#             print(f'Немає такої задачі {task}')
#             return
#
#         # чи вистачає бюджету
#         free_money = self.budget - self.expenses
#         if price > free_money:
#             print("Недостатньо коштів")
#             return
#
#         # виконуємо задачу
#         self.expenses += price
#         self.tasks.remove(task)
#         self.spent_time += duration
#
#         # чи завершений проект
#         if len(self.tasks) == 0:
#             self.is_finished = True
#
#     def update_budget(self, amount):
#         self.budget += amount
#
#
#
# project = Project(name='Ігрушка',
#                   budget=10_000,
#                   tasks=['Знайти інвесторів',
#                          'Придумати загальну ідею'])
#
# project.display_info()
#
# project.add_task('Вибрати ПЗ для гри')
#
# project.display_info()
#
# project.divide_task('Організувати бенкет',
#                     ['витратити бюджет']
#                     )
#
# project.divide_task('Придумати загальну ідею',
#                     ['Обрати між 2D та 3D',
#                      'Придумати сюжет',
#                      'Прописати персонажів']
#                     )
#
# project.display_info()
#
# project.do_task('Придумати сюжет', 6, 1000)
# project.do_task('Обрати між 2D та 3D', 3, 200)
# project.do_task('Прописати персонажів', 15, 6000)
#
# project.update_budget(2500)
#
# project.do_task('Знайти інвесторів', 10, 3000)
# project.do_task('Вибрати ПЗ для гри', 5, 1800)
#
# project.display_info()

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

class Telefon:
    def __init__(self, memory, apps):
        self.memory = memory
        self.apps = apps

        self. is_on = False
        # рахуємо стартову память використану
        self.used_memory = 0
        for app in self.apps:
            self.used_memory += self.apps[app]

    def print_memoruinfo(self):
        print(f"Залишилось вільної памяті {self.memory - self.used_memory}")
        print("Встановлені додатки: ")
        for app in self.apps:
            print(f"Встановлениый додаток {app} - {self.apps[app]} ГБ")

        print()
        print()

    def delete_app(self,remuve_app):
        if remuve_app not in self.apps:
            print(f"Додаток {remuve_app} не встановлений.")
            return

        app_memory = self.apps.pop(remuve_app)

        self.used_memory -= app_memory

    def install_app(self, app_name, app_memory):
        if self.used_memory + self.memory >= app_memory:

            if app_name in self.apps:
                print(f"Додаток {app_name} вже встановлений.")
                return

            self.apps[app_name] = app_memory
            self.used_memory += app_memory

        else:
            print("Недостатньо памяті")

    def update_app(self, app_name, new_memory):
        free_memory = self.memory - self.used_memory
        app_memory = self.apps[app_name]
        need_memory = new_memory - app_memory

        if app_name not in self.apps:
            print("Немає такої програми.")
            return

        if free_memory >= need_memory:
            self.apps[app_name] = new_memory
            self.used_memory += need_memory
        else:
            print("Недостатньо памяті")

    def tern_on(self):
        self.is_on = True

    def tern_off(self):
        self.is_on = False


telefon = Telefon(128,
                  {"Google": 30, 'YouTube': 10})
telefon.print_memoruinfo()

telefon.delete_app("YouTube")
telefon.print_memoruinfo()

telefon.install_app("angru berds", 20)
telefon.print_memoruinfo()

telefon.update_app("angru berds", 50)
telefon.print_memoruinfo()


# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального
# Завдання 4
# Створіть клас Студент з атрибутами:
#  ім’я
#  словник з предметами, де ключ – назва предмету,
# значення – список оцінок
# Додайте методи:
#  додати новий предмет
#  видалити предмет
#  вчити предмет(якщо отримана оцінка, то додати про це
# інформацію)
#  отримати середню оцінку за конкретним предметом
#  вивести загальну інформацію: ім’я та список предметів
# з середніми оцінками

# Завдання 5
# Створіть клас Магазин з атрибутами:
#  назва
#  заробіток
#  словник з товарами, де ключ – назва товару, значення –
# кількість на складі
#  словник з товарами, де ключ – назва товару, значення –
# ціна
# Додайте методи:
#  вивід інформації: назва та список доступних товарів
#  поповнення складу певним товаром(може бути новий)
#  оформлення замовлення, якщо товар у достатній
# кількості доступни
