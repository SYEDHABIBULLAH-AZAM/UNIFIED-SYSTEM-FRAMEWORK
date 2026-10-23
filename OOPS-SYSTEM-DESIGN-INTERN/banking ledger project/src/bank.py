
from src.account import BankAccount


class Bank:
    """Manages multiple bank accounts."""

    def __init__(self, name):
        self.name = name
        self._accounts = {}

    def create_account(self, account_holder, opening_balance=0):
        account_number = f"ACC{len(self._accounts) + 1001}"

        account = BankAccount(account_holder, opening_balance)
        self._accounts[account_number] = account

        return account_number

    def get_account(self, account_number):
        account = self._accounts.get(account_number)

        if account is None:
            raise ValueError("Account not found.")

        return account

    def display_accounts(self):
        print(f"\n--- {self.name} Accounts ---")

        for number, account in self._accounts.items():
            print(
                number,
                "|",
                account.account_holder,
                "|",
                f"{account.currency} {account.balance:.2f}",
            )
