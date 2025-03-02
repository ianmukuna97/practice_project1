# data, name, phone number, gender, amount
# account
# deposit, withdrawal, check balance
# oop -- like a bank account

# Matatu -- number, driver, conductor, route

class Account:
    def __init__(self, full_name, acc_number, phone, balance): #constructor ---(set up info)
        self.full_name = full_name
        self.acc_number = acc_number
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount ${amount} has been successfully deposited to ${self.acc_number}")