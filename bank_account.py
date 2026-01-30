class BankAccount:
    def __init__(self , holder_name,account_number,):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self,amount):
        self.balance= self.balance + amount
        print("Amount Deposited:",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:",amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Name:",self.holder_name)
        print("Account Number:",self.account_number )
        print("Current Bank Balance:",self.balance)


#inheritance

class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        if amount - self.balance >= 500:
            self.balance = self.balance - amount
            print("Amount withdrawn:",amount)
        else:
            print("Minimum Balance of 500 required")


account1 = BankAccount("Akash",101)
account2 = SavingsAccount("vinoth",102)

print("\n Account 1")
account1.deposit(1000)
account1.withdraw(200)
account1.show_balance()


print("\n Account 2")
account2.deposit(2000)
account2.withdraw(1000)
account2.show_balance()


