class User: 
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdraw(self, amount):
        self.balance -= amount

    def display_user_balance(self, balance):
        print(self.balance)

    def transfer_money(self, amount, user):
        self.balance -= amount
        user.balance += amount
        print(self.balance)

user1 = User('bob', 'bob23@hotmail.com', 2,000)
user2 = User('john', 'johndoe56@yahoo.com', 400)
user3 = User('steve', 'steve101@gmail.com', 5,000)

user1.make_deposit(450)
user1.make_deposit(8,000)
user1.make_deposit(200)
user1.make_withdraw(250)
print(user1.balance)

user2.make_deposit(5,000)
user2.make_deposit(10,000)
user2.make_withdraw(450)
user2.make_withdraw(30)
print(user2.balance)

user3.make_deposit(20,000)
user3.make_withdraw(5,000)
print(user3.balance)

user1.transfer_money(200, user2)



