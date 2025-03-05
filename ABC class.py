# # наслідування
#
# # переведення числа в діапазон [0, 100]
#
# value = -10
#
# # варіант через if
# # if value > 100:
# #     value = 100
# # elif value < 0:
# #     value = 0
#
# # через min max
#
# value = -10
# new_value = min(value, 100)
# new_value = max(new_value, 0)
#
# new_value = max(0, min(100, value))  # clip
#
# print(new_value)

# використання методів батьківського класу
# from abc import ABC, abstractmethod
#
# class Animal(ABC):  # абстрактний клас(не можна створити об'єкт)
#     @abstractmethod
#     def __init__(self, name, age):
#         self._check_name(name)
#         self._check_age(age)
#         self.name = name
#         self.age = age
#
#     def _check_name(self, name):
#         # перевірка чи тип даних str
#         if not isinstance(name, str):
#             raise ValueError(f"Ім'я має бути рядком, отримано тип {type(name)}")
#
#         # лише літери та символи ' ' '-'
#         for sym in name:
#             if not(sym.isalpha() or sym in ' -'):
#                 raise ValueError("Ім'я має складатися лише з літер та ' -'")
#
#     def _check_age(self, age):
#         # перевірка чи тип даних int float
#         if not isinstance(age, (int, float)):
#             raise ValueError(f"Вік має бути числом, отримано тип {type(age)}")
#
#         if age <= 0 or age >= 20:
#             raise ValueError(f"Вік має бути в діапазоні [0, 20]")
#
#
#     def info(self):
#         print(f"Ім'я: {self.name}, {self.age} років")
#
#
# class Cat(Animal): # name, age, is_vaccinated
#     def __init__(self, name, age, is_vaccinated=True):
#         super().__init__(name, age)
#         self.is_vaccinated = is_vaccinated
#
#     def catch_mouse(self):
#         print("Ловить мишу")
#
#     def info(self):  # додатково писало що це кіт
#         print("Кіт")
#         # super() # super -- батьківський клас
#         super().info() # info з класу Animal
#
#         if self.is_vaccinated:
#             print("Вакцинований")
#         else:
#             print("Потрібно вакцинувати")
#
#
# # cat1 = Cat('Tom', 5)
# # cat1.info()
# # #cat1.catch_mouse()
# # print()
# #
# # cat = Animal('Roger', 10)
# # cat.info()
#
# # приховані атрибути\методи
#
# class Cat(Animal): # name, age, is_vaccinated
#     def __init__(self, name, age, is_vaccinated=True):
#         super().__init__(name, age)
#         self._is_vaccinated = is_vaccinated  # прихований атрибут
#
#     def catch_mouse(self):
#         print("Ловить мишу")
#
#     def info(self):  # додатково писало що це кіт
#         print("Кіт")
#         # super() # super -- батьківський клас
#         super().info() # info з класу Animal
#
#         if self._is_vaccinated:
#             print("Вакцинований")
#         else:
#             print("Потрібно вакцинувати")
#
#     def vaccinate(self):
#         self._is_vaccinated = True
#
#     def unvaccinate(self):
#         self._is_vaccinated = False
#
#
# class Kitten(Cat):
#     pass
#
#
# cat1 = Cat('Tom', 2.5)
#
# cat1.info()
#
# cat1.unvaccinate()
#
# cat1.info()
#
# # print(cat1._Cat__is_vaccinated)
#
# kitten = Kitten("Murchyck", 1)
# kitten.info()

# _____________________________________________________________
# from abc import ABC, abstractmethod
#
#
# class Robot(ABC):
#     def __init__(self, name, battery_level=100, status="off"):
#         self.name = name
#         self.battery_level = battery_level
#         self.status = status
#
#     @abstractmethod
#     def info(self):
#         print(f"назва робота або id: {self.name}")
#         print(f"рівень заряду: {self.battery_level}%")
#         print(f"поточний стан: {self.status}")
#
#     def charge(self):
#         self.battery_level = 100
#
#     def turn_on(self):
#         self.status = "on"
#
#     def turn_off(self):
#         self.status = "off"
#
#
# # robot1 = Robot("abs", 90)
# # robot1.info()
#
# # Створіть дочірній клас CleaningRobot
# # Додаткові атрибути:
# #  dust_capacity – ємність контейнеру для пилу(за
# # замовчуванням 0%)
# #  water_capacity – ємність контейнеру для води(за
# # замовчуванням 100%)
# #  cleaning_mode – тип прибирання(вологе або сухе)
# # Методи:
# #  info() – додатково виводить інформацію про робота
#
# #  turn_on() – якщо контейнер для пилу повний або
# # контейнер для води порожній то виводить повідомлення,
# # інакше запускається turn_on() з класу Robot
#
# #  empty_dustbin() – очищає контейнер для пилу
# #  fill_water() – заповнює контейнер для води
# #  swap_mode() – змінює тип прибирання на протилежний
# #  clean(energy, dust, water=None) – чистить поверхню,
# # якщо прибирання сухе, то просто перенести пил у
# # контейнер(якщо місця не достатньо вивести помилку),
# # якщо прибирання вологе то додатково витратити воду.
# # Також зменшує рівень заряду на energy
#
# class CleaningRobot(Robot):
#     def __init__(self, name, battery_level=100, status="off", dust_capacity=0,
#                  water_capacity=100, cleaning_mode="wet"):
#         super().__init__(name, battery_level, status)
#         self.dust_capacity = dust_capacity
#         self.water_capacity = water_capacity
#         self.cleaning_mode = cleaning_mode
#
#     def info(self):
#         super().info()
#         print(f"ємність контейнеру для пилу: {self.dust_capacity}%")
#         print(f"ємність контейнеру для води: {self.water_capacity}%")
#         print(f"тип прибирання: {self.cleaning_mode}")
#
#     #  turn_on() – якщо контейнер для пилу повний або
#     # контейнер для води порожній то виводить повідомлення,
#     # інакше запускається turn_on() з класу Robot
#     def turn_on(self):
#         if self.dust_capacity == 100 or self.water_capacity == 0:
#             print("контейнер для пилу повний або контейнер для води порожній")
#         else:
#             super().turn_on()
#
#     def empty_dustbin(self):
#         self.dust_capacity = 0
#
#     def fill_water(self):
#         self.water_capacity = 100
#
#     def swap_mode(self):
#         if self.cleaning_mode == 'wet':
#             self.cleaning_mode = "dry"
#         else:
#             self.cleaning_mode = "wet"
#
#     #  clean(energy, dust, water=None) – чистить поверхню,
#     # якщо прибирання сухе, то просто перенести пил у
#     # контейнер(якщо місця не достатньо вивести помилку),
#     # якщо прибирання вологе то додатково витратити воду.
#     # Також зменшує рівень заряду на energy
#
#     def clean(self, energy, dust, water=None):
#         if self.status == "off":
#             print("Robot is off!")
#             return
#
#         if self.battery_level < energy:
#             print("Low battery_level!")
#             return
#
#         if self.dust_capacity + dust > 100:
#             print("Empty dust_capacity!")
#             return
#
#         if self.cleaning_mode == "wet":
#             if self.water_capacity < water:
#                 print("Nor Enough water!")
#                 return
#
#         print("Working!")
#         self.battery_level -= energy
#         self.dust_capacity += dust
#
#         if self.cleaning_mode == "wet":
#             self.water_capacity -= water
#
#
# # robot2 = CleaningRobot("Abs")
# # robot2.turn_on()
# # robot2.clean(50, 20, 20)
# # robot2.info()
#
#
# # Завдання 4
# # Створіть дочірній клас AssistantRobot
# # Додаткові атрибути:
# #  tasks – список завдань(за замовчуванням порожній)
# #  current_task – поточне завдання(за замовчуванням None)
# # Методи:
# #  info() – додатково виводить інформацію про робота
# #  add_task(task) – додає завдання до списку
# #  change_task() – змінює поточне завдання, виводить на
# # екран список завдань та просить користувача вибрати
# # одне з них
# #  execute_task() – виконує поточне завдання, видяляє його
# # зі списку, та змінює current_task на наступне
#
#
# class AssistantRobot(Robot):
#      def __init__(self, name, battery_level=100, status="off", tasks=None, current_task=None):
#         super().__init__(name, battery_level, status)
#         if tasks is None:
#             self.tasks = []
#         else:
#             self.tasks = tasks
#         self.current_task = current_task
#
#     def info(self):
#         super().info()
#         for task in self.tasks:
#             print(task)
#         print(self.current_task)
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def change_task(self):
#         if not self.tasks:
#             print('Нема завдань')
#             return
#
#         print('Список завдань:')
#         for ind, task in enumerate(self.tasks, start=1):
#             print(f'Номер {ind} - {task}')
#
#         choice = int(input('Виберіть номер завдання: '))
#         self.current_task = self.tasks[choice - 1]
#
#     def execute_task(self):
#         if not self.current_task:
#             print('Немає поточного завдання')
#             return
#
#         print('Виконано завдання', self.current_task)
#         self.tasks.remove(self.current_task)
#
#         if self.tasks:
#             self.current_task = self.tasks[0]
#         else:
#             print('Завдань немає')
#             self.current_task = None