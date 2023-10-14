from app.account_creation import Account
from app.withdrawal import Withdrawal
from app.deposit import Deposit


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, first_name, last_name):
        account = Account(first_name, last_name,
                          "developer", 0, len(self.accounts))
        acc = list(self.accounts)
        acc.append(account.to_dict())
        self.accounts = acc

    def withdraw_money(self, account_id, withdrawal_amount):
        for account in self.accounts:
            if account["account_id"] == account_id:
                message, new_balance = Withdrawal.withdraw_money(
                    account["account_balance"], withdrawal_amount)
                if message == "balance updated":
                    account["account_balance"] = new_balance
                else:
                    print(message)

    def deposit_money(self, account_id, deposit_amount):
        for account in self.accounts:
            if account["account_id"] == account_id:
                new_balance = Deposit.deposit_money(
                    account["account_balance"], deposit_amount)
                account["account_balance"] = new_balance

    def get_all_accounts(self):
        return self.accounts


def main():
    bank = Bank()
    first_name = input("input your first name: ")
    last_name = input("input your last name: ")
    print(bank.get_all_accounts())
    bank.create_account(first_name, last_name)
    deposit_am = int(input("input amount to deposit: "))
    bank.deposit_money(0, deposit_am)
    print(bank.get_all_accounts())
    withdrawal_am = int(input("withdraw amount: "))
    bank.withdraw_money(0, withdrawal_am)
    print(bank.get_all_accounts())


main()
