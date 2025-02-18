# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).

class Bank_ammount:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency

        self.curs = {"UAH": 1,
                     "USD": 42,
                     "EUR": 44,
                     "PLZ": 10}

    def stan_rahunku(self):
        print(f"На рахунку {self.name} наявні {self.balance} {self.currency}.")

    def znyati(self, suma):
        if self.balance >= suma:
            self.balance -= suma
        else:
            print(f'На рахунку недостатньо коштів. Баланс складає - {self.balance} {self.currency}.')

    def popovniti(self, suma):
            self.balance += suma
            print(f'Ваш рахунок поповнено на {suma}. Баланс складає - {self.balance} {self.currency}.')

    def cur_check(self, cur):
        if cur in self.curs:
            return True
        else:
            raise ValueError("Невірно визначена валюта.")

    def currency_exchenge(self, new_cur, suma_to_exchenge):
        # переврка достатності коштів, якщо будемо реалізовувати "обмін валюти в кассі"
        # if self.balance < suma_to_exchenge:
        #     print(f'На рахунку недостатньо коштів. Баланс складає - {self.balance} {self.currency}.')
        #     return

        if self.currency == 'UAH' or new_cur == 'UAH':
             new_sum = self.curs[self.currency] * suma_to_exchenge / self.curs[new_cur]
             print(f"{suma_to_exchenge} {self.currency} еквівалентно {new_sum: .2f}")
        else:
             v_hrn = self.curs[self.currency]  * suma_to_exchenge / self.curs['UAH']
             new_sum = v_hrn / self.curs[new_cur]
             print(f"{suma_to_exchenge} {self.currency} еквівалентно {new_sum: .2f}")

        return new_cur, new_sum

        # результати переведення "обмін в кассі"
        # self.balance -= suma_to_exchenge
        # print(f"Валюту переведено. Результат складає {new_sum: .2f} {new_cur}.")
        # print(f"Баланс Вашого рахунку тепер складає: {self.balance} {self.currency}")

    def chenge_accaunt_curr(self):
        try:
            new_cur = input("Введіть валюту в яку хочете конвертувати свій рахунок: ")

            if client.cur_check(new_cur):
                print('OK')

                suma = self.balance
                new_cur, new_sum = client.currency_exchenge(new_cur,suma)

                client.balance = new_sum
                client.currency = new_cur

                print(f"Баланс Вашого рахунку тепер складає: {self.balance} {self.currency}")

        except ValueError as err:
            print(err)


# def print_curs():
    # якщо будемо реалізовувати "обмін в касі"
    # print("Курс валют.")
    # for curr in client.curs:
    #     print(f"1 {curr} = {client.curs[curr]}")


client = Bank_ammount("Ivan", 300, "USD")

client.stan_rahunku()

client.chenge_accaunt_curr()

client.stan_rahunku()
