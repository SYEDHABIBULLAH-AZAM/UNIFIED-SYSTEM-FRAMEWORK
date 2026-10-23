
from decimal import Decimal
from src.transaction import Transaction
from src.ledger import TransactionLedger


class BankAccount:
    """Represents a bank account with transaction tracking."""

    def __init__(self, account_holder: str, opening_balance=0):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")

        opening_balance = Decimal(str(opening_balance))

        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_holder = account_holder
        self._balance = opening_balance
        self.currency = "INR"
        self.ledger = TransactionLedger()

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount

        transaction = Transaction.create(
            transaction_type="DEPOSIT",
            amount=amount,
            balance_after=self._balance,
        )
        self.ledger.add_transaction(transaction)

    def withdraw(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient balance.")

        self._balance -= amount

        transaction = Transaction.create(
            transaction_type="WITHDRAWAL",
            amount=amount,
            balance_after=self._balance,
        )
        self.ledger.add_transaction(transaction)

    def display_account(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.account_holder)
        print(f"Balance: {self.currency} {self.balance:.2f}")
        print("Total Transactions:", len(self.ledger.transactions))
