class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        pass 
    def yield_interest(self):
        pass

ba1 = BankAccount(0.09, 1,800)
ba2 = BankAccount(0.09, 10,800)
ba1.deposit(500)
ba1.deposit(900)
ba1.deposit(10,000)
ba1.withdraw(300)
ba1.balance
ba2.deposit(400)
ba2.deposit(4500)
ba2.withdraw(100)
ba2.withdraw(20)
ba2.withdraw(40)
ba2.withdraw(80)
ba2.balance