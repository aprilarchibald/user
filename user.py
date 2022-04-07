from re import A


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    # adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance} ")
        return self

    def transfer_money(self, firstUser, amount):
        firstUser.make_deposit(amount)
        self.make_withdrawal(amount)
        firstUser.display_user_balance()
        self.display_user_balance()
        return self
        

#create 3 instances of the User class
Art = User("Art", "art@gmail")
Bob = User("Bob", "bob@yahoo")
Carol = User("Carol", "carol@gmail")

Art.make_deposit(250).make_deposit(400).make_deposit(300).make_withdrawal(150).display_user_balance()


Bob.make_deposit(250).make_deposit(400).make_withdrawal(300).make_withdrawal(150).display_user_balance()


Carol.make_deposit(250).make_withdrawal(400).make_withdrawal(300).make_withdrawal(150).display_user_balance()


Art.transfer_money(Carol, 600)