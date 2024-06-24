from bank_account import *

dave = BankAccount(account_name='Dave', initial_amount=2_000)
mike = BankAccount(account_name='Mike', initial_amount=1_500)
sara = BankAccount(account_name='Sara', initial_amount=1_000)

dave.get_balance()
mike.get_balance()


mike.deposit(2_300)
mike.withdraw(5_000)

dave.transfer(amount=300, account=sara)

jim = InterestRewardsAccount(account_name="Jimmy", initial_amount=2000)
jim.get_balance()
jim.deposit(1000)
jim.transfer(amount=200, account=dave)

ali = SavingsAccount(account_name="Ali", initial_amount=3000)
ali.get_balance()
ali.deposit(2000)

ali.transfer(amount=10_000, account=sara)
ali.transfer(amount=1_000, account=sara)
