class Withdrawal:
    @staticmethod
    def withdraw_money(initial_balance, withdrawal_amount):
        if initial_balance <= 0 | initial_balance-withdrawal_amount < 0:
            print("insufficient balance")
            return ["insufficient balance"]
        new_balance = initial_balance - withdrawal_amount
        return ["balance updated", new_balance]
