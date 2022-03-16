class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate # your code here! (remember, instance attributes go here)
        self.balance = balance
        BankAccount.accounts.append(self) # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount 
        return self# your code here
    def withdraw(self, amount):
        if(self.balance - amount) >=0:
            self.balance -= amount 
        else:
            print(f"insufficient Funds : Chargin a $5 fee")
            self.balance -= 5 
        return self # your code here
    def display_account_info(self):
        return f"{self.balance}"
        # your code here
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self # your code here
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance + self.int_rate)
        return self
        
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
        
savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)
savings.deposit(10).deposit(30).deposit(50).withdraw(250).yield_interest().display_account_info()
checking.deposit(10).deposit(30).withdraw(50).withdraw(250).withdraw(40).yield_interest().display_account_info()

BankAccount.print_all_accounts()
class User:
    
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(.05,1000)
        

        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.display_account_info()}")
        return self



josh = User("Josh")
kyle = User("Kyle")
jeremy = User("Jeremy")






josh = User("Josh")

josh.account.deposit(100)
josh.display_user_balance()
