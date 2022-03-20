class BankAccount:
    account_create = 0

    def __init__(self,number, client, balance=10):
        self.number = number
        self.client = client
        self.balance = 10
        BankAccount.account_create

    def display_balance(self):
        print(self.balance)

        account_create= BankAccount()


