# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass

class Pet:
    def __init__(self, name, satiety = 50, energy = 50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100

    def eat(self, food_amont):
        self.satiety += food_amont

        if self.satiety > 100:
            self.satiety = 100

    def play(self, activity_level): # зменьшує енергію та ситість на рівень актіветі_левел
        # self.satiety -= activity_level
        # self.energy -= activity_level
        #
        # if self.satiety <= 0:
        #     print(f"{self.name} загрався й здох від голоду!")
        #
        # if self.energy == 0:
        #     print(f"{self.name} загрався й вирубився після гри!")
        #     self.sleep()
        # elif self.energy < 0:
        #     print(f"{self.name} не вистачило сил, щоб погратися й він вирубився недогравши!")
        #     self.sleep()
        pass

    def make_sound(self):
        pass



# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть

class Cat(Pet):

    def play(self, activity_level):
         if self.satiety > 60 and 2*activity_level < self.energy and activity_level < self.satiety: # вставляємо додаткові критерій щоб сила активності не первищувала рівень енергії та ситості
            self.energy -= 2*activity_level
            self.satiety -= activity_level
         else:
             print(f"{self.name} не хоче зараз гратися!")

    def make_sound(self):
        print("Мяу!")

    def catch_mouse(self):
        if self.energy > 30:
            if self.satiety >40:
                print("Зловив та погрався з мишкою.")
                self.play(5)
            else:
                print("Зловив та зїв мишку.")
                self.eat(5)
        else:
            print("Немає сил ловити мишку.")



# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5

class Dog(Pet):
    def play(self, activity_level):
        # вставляємо додаткові критерій щоб сила активності не первищувала рівень енергії та ситості
        if self.satiety > 15 and activity_level / 2 < self.energy and activity_level / 2 < self.satiety:
            self.energy -= activity_level/2
            self.satiety -= activity_level/2
        else:
            print(f"{self.name} не хоче зараз гратися!")

    def make_sound(self):
        print("Гав!")

    def catch_mouse(self):
        if self.satiety > 10:
            self.energy -= 5
        else:
            print("Голодний, щоб гратися.")



tuzik = Cat("Tuzik")
print(tuzik.energy)
print(tuzik.satiety)

tuzik.eat(30)
tuzik.sleep()
print(tuzik.energy)
print(tuzik.satiety)

tuzik.play(15)
print(tuzik.energy)
print(tuzik.satiety)

tuzik.catch_mouse()
print(tuzik.energy)
print(tuzik.satiety)
