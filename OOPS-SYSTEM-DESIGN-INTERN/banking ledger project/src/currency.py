
from decimal import Decimal


class CurrencyConverter:
    """Converts money between supported currencies."""

    RATES = {
        "INR": Decimal("1"),
        "USD": Decimal("83"),
        "EUR": Decimal("90"),
    }

    @classmethod
    def convert(cls, amount, from_currency, to_currency):
        amount = Decimal(str(amount))
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        if from_currency not in cls.RATES:
            raise ValueError("Unsupported source currency.")

        if to_currency not in cls.RATES:
            raise ValueError("Unsupported target currency.")

        amount_in_inr = amount * cls.RATES[from_currency]
        result = amount_in_inr / cls.RATES[to_currency]

        return result.quantize(Decimal("0.01"))
