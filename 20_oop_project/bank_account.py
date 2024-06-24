
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name) -> None:
        self.balance = initial_amount
        self.name = account_name
        print(
            f"\n{'*'* 20}\nAccount for customer '{self.name}' created\nBalance= ${self.balance:.2f} \n{'*'* 20}")

    def get_balance(self):
        print(
            f"\nAccount for customer {self.name}, balance : ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(
            f'\nDeposit completed for customer {self.name}. Amount : +{amount}')
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account for customer '{self.name}' has only a balance of {self.balance: .2f}.\nMaximum authorized withdraw is ${self.balance}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f'Withdraw of {amount} completed !')
            self.get_balance()

        except BalanceException as e:
            print(f'Withdraw interrupted:\n{e}')

    def transfer(self, amount, account):
        print(f'\n\n{"*" * 20}\nStarting Transfer :\n')
        try:
            self.withdraw(amount)
            print(
                f'\nTransfer of {amount} to customer {account.name} completed !')

        except BalanceException as e:
            print(f'Transfer interrupted:\n{e}')

        print(f'\nClosing Transfer :\n\n{"*" * 20}')


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print('\nDeposit completed')
        self.get_balance()


class SavingsAccount(InterestRewardsAccount):
    fee: int = 5

    def __init__(self, initial_amount, account_name) -> None:
        super().__init__(initial_amount, account_name)

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f'Withdraw on Saving account of {amount} completed !')
            self.get_balance()
        except BalanceException as e:
            print(f'Withdraw interrupted:\n{e}')
