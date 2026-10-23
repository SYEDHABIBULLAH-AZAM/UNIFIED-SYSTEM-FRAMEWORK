
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    transaction_type: str
    amount: Decimal
    balance_after: Decimal
    timestamp: str

    @classmethod
    def create(cls, transaction_type, amount, balance_after):
        return cls(
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
            timestamp=datetime.now().isoformat(timespec="seconds"),
        )
