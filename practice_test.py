# data, name, phone number, gender, amount
# account
# deposit, withdrawal, check balance
# oop -- like a bank account

# Matatu -- number, driver, conductor, route

class Account:
    def __init__(self, full_name, acc_number, phone, balance):  # anonymous function--constructor ---(set up info)
        self.full_name = full_name
        self.acc_number = acc_number
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount ${amount} has been successfully deposited to {self.acc_number}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient balance. Your balance is ${self.balance}")
        else:
            self.balance -= amount
        print(f"Amount ${amount} has been successfully withdrawn from account {self.acc_number}")

    def check_balance(self):
        print(f"The balance of account {self.acc_number} is: ${self.balance}")


# data and methods used to manipulate the data
joe_acc = Account("Joe Mbugua", "0001", "0712345678", 1000)
sasha_acc = Account("Sasha Wanjiru", "0002", "0722334455", 2000)
joe_acc.deposit(1000)
joe_acc.check_balance()
joe_acc.withdraw(500)
joe_acc.check_balance()

sasha_acc.deposit(1000)
sasha_acc.check_balance()
sasha_acc.withdraw(700)
sasha_acc.check_balance()
