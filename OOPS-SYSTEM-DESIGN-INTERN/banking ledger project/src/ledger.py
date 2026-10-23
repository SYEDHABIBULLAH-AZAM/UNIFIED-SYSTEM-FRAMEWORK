
class TransactionLedger:
    """Stores and displays bank transaction records."""

    def __init__(self):
        self._transactions = []

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    @property
    def transactions(self):
        return tuple(self._transactions)

    def display_history(self):
        print("\n--- Transaction History ---")

        if not self._transactions:
            print("No transactions found.")
            return

        for transaction in self._transactions:
            print(
                f"{transaction.timestamp} | "
                f"{transaction.transaction_type} | "
                f"INR {transaction.amount:.2f} | "
                f"Balance: INR {transaction.balance_after:.2f}"
            )
