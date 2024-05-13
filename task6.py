class BankAccount():
    def __init__(self, balance, balance_number):
        self.balance = balance
        self.balance_number = balance_number
    
    def show_balance(self):
        print(f'Balansinizda {self.balance} vesait var')
    
    def add_money_to_balance(self, money):
        self.balance += money

    def get_money_from_balance(self, money):
        if money < self.balance:
            self.balance -= money
        else: 
            print('Balansinizda kifayet mebleg yoxdur')
    
class CreditAccount(BankAccount):
    def __init__(self, balance, balance_number, credit_amount = 0):
        super().__init__(balance, balance_number)
        self.credit_amount = credit_amount

    def give_credit(self, credit_amount):
        self.credit_amount += credit_amount
        self.balance += self.credit_amount
    
    def pay_credit(self):
        self.credit_amount -= self.credit_amount / 12
        self.balance -= self.credit_amount / 12
    
    def account_info(self):
        print(f'Balans: {self.balance}. \nKredit borcu: {self.credit_amount}')

bankAccount1 = BankAccount(1000, 1)
bankAccount1.show_balance()
bankAccount1.add_money_to_balance(500)
bankAccount1.show_balance()
bankAccount1.get_money_from_balance(200)
bankAccount1.show_balance()

creditAccount1 = CreditAccount(1000, 1, 0)
creditAccount1.give_credit(500)
creditAccount1.account_info()
creditAccount1.pay_credit()
creditAccount1.account_info()