
import unittest
from decimal import Decimal

from src.account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Habib", 10000)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, Decimal("10000"))

    def test_deposit(self):
        self.account.deposit(2000)
        self.assertEqual(self.account.balance, Decimal("12000"))

    def test_withdrawal(self):
        self.account.withdraw(1500)
        self.assertEqual(self.account.balance, Decimal("8500"))

    def test_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(20000)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_transaction_history(self):
        self.account.deposit(500)
        self.assertEqual(len(self.account.ledger.transactions), 1)


if __name__ == "__main__":
    unittest.main()

