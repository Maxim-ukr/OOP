# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.

class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата карткою {amount} {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
            self.currency = currency

    def pay(self, amount):
        print(f"оплата PayPal {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата криптогаманцем {amount} {self.currency}")

# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
def create_payment():
    amount = input("Введіть тип створюваного рахунку (CreditCardPayment, PayPalPayment, CryptoPayment): ")
    currency = input('Введіть валюту рахунку: ')

    if amount == 'CreditCardPayment':
        return CreditCardPayment(currency)
    elif amount == 'CryptoPayment':
        return CryptoPayment(currency)
    elif amount == 'PayPalPayment':
        return PayPalPayment(currency)
    else:
        print(f"Невідомий тип рахунку - {amount}.")


spisok = []

for _ in range(2):
    item = create_payment()
    spisok.append(item)


for item in spisok:
    item.pay("100")