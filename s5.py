# static vs instance method example 
# both static and instance method are stored in the class itself not in the indiviual object
# static method can be used for utility fuction that do not rely on specific instance data 

class BankAcccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self._log_transaction('deposit', amount)
            print(f'Deposited {amount}')
        else:
            print('Invalid deposit amount')

    def _is_valid_amount(self, amount):
        return amount > 0

    def _log_transaction(self, transaction_type, amount):
        print(f'Logged transaction of {amount}. New balance is {self._balance}') # example of how it can be used

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5  # between 5% and 0%


account = BankAcccount('sahil', 1000)
account.deposit(100)


print(BankAcccount.is_valid_interest_rate(2.5))

print(BankAcccount.is_valid_interest_rate(12.5))

        
