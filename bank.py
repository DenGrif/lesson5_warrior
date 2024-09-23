class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы успешно пополнили счёт. Сумма на счёте - {self.balance}')

    def withdraw(self, money):
        if money > self.balance:
            print(f"недостаточно средств на счёте")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счёте {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс {self.balance}")


man = Account("17847218", 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)

