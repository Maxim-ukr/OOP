# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт

# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min
# Приклад рецептів:
# Recipe("Піца",
#  ["борошно", "вода", "дріжджі", "томат", "сир"],
#  "Готуємо тісто, додаємо інгредієнти та запікаємо",
#  30)
#
#  Recipe("Салат",
#  ["томат", "огірок", "зелень", "олія"],
#  "Нарізаємо овочі, додаємо зелень та поливаємо
# олією",
#  10)
#
#  Recipe("Суп",
#  ["вода", "картопля", "морква", "м'ясо"],
#  "Варимо всі інгредієнти до готовності",
#  45)

# class Recipe:
#     def __init__(self, name, ingredients, text, time):
#         self.name = name
#         self.ingredients = ingredients
#         self.text = text
#         self.time = time
#
#     def __str__(self):
#         return self.name
#
#     def __contains__(self, item):
#         return item in self.ingredients
#
#     def __gt__(self, other):
#         return self.time > other.time
#
#     def display_info(self):
#         return (f"{self.name} "
#                 f"- {self.ingredients} - "
#                 f"{self.text} - {self.time}")
#
#
# recipe1 = Recipe("Піца",
#  ["борошно", "вода", "дріжджі", "томат", "сир"],
#  "Готуємо тісто, додаємо інгредієнти та запікаємо",
#  30)
#
# recipe2 = Recipe("Салат",
#  ["томат", "огірок", "зелень", "олія"],
#  "Нарізаємо овочі, додаємо зелень та поливаємо олією",  10)
#
# recipe3 = Recipe("Суп",
#  ["вода", "картопля", "морква", "м'ясо"],
#  "Варимо всі інгредієнти до готовності",
#  45)
#
# cookingbook = [recipe1, recipe2, recipe3]
#
# for recip in cookingbook:
#     if recip.__contains__('томат'):
#         print(recip.name)
#
# min_recip = min(cookingbook)
# print(min_recip)
