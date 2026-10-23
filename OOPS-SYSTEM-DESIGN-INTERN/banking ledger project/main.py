
from src.bank import Bank
from src.currency import CurrencyConverter


def main():
    bank = Bank("Banking Ledger Engine")

    account_number = bank.create_account("Habib", 10000)
    account = bank.get_account(account_number)

    account.deposit(2000)
    account.withdraw(1500)

    bank.display_accounts()
    account.display_account()
    account.ledger.display_history()

    print("\n--- Currency Conversion ---")
    usd = CurrencyConverter.convert(1000, "INR", "USD")
    eur = CurrencyConverter.convert(1000, "INR", "EUR")

    print(f"INR 1000 = USD {usd}")
    print(f"INR 1000 = EUR {eur}")


if __name__ == "__main__":
    main()
