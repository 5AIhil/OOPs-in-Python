# static vs instance method example 

class BankAcccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount >0:
            self._balance += amount
            print(f'Deposited {amount}')
        else:
            print('Invalid deposit amount')

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5  # between 5% and 0%


account = BankAcccount('sahil', 1000)
account.deposit(100)

print(BankAcccount.is_valid_interest_rate(2.5))

print(BankAcccount.is_valid_interest_rate(12.5))

        
