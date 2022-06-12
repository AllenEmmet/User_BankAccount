class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount 
        else:
            print("insufficient funds")
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance +(self.balance * self.int_rate)
        return self

class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.account = BankAccount(.02, 0)
    def makedeposit(self, amount):
        self.account.deposit(amount)
        return self
    def makewithdrawal(self, amount):
        self.account.withdrawal(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self

emmet = user("emmet", "allen", "ea@gmail", 24)
sophia = user("sophia", "ws", "sws@gmail", 26)
lucy = user("lucy", "ws", "lws@gmail", 23)

emmet.makedeposit(50).makewithdrawal(10).display_user_balance()