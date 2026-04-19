#Car class example last sem
class car:
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model

    def car_details(self):
        print(self.brand)
        print(self.model)

car1 = car("Kia","Saltos")
car2 = car("Toyota","Supra")

car1.car_details()
car2.car_details()

# Bank Account Class Exercise
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(self.balance)

    def details(self):
        print(self.account_number)
        print(self.balance)

acc = BankAccount(1234567890,100000)

acc.deposit(500)
acc.withdraw(2000)
acc.deposit(800)
acc.check_balance()
acc.details()
