class Account:
    def __init__(self, first_name, last_name, occupation, account_balance, account_id):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.account_balance = account_balance
        self.account_id = account_id

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "occupation": self.occupation,
            "account_balance": self.account_balance,
            "account_id": self.account_id
        }
