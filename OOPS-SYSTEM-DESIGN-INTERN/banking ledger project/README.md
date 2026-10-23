
# Multi-Currency Banking & Ledger Engine

A Python-based banking simulation project demonstrating
Object-Oriented Programming (OOP), transaction management,
input validation, and multi-currency conversion.

## Features

- Create and manage bank accounts
- Deposit and withdraw money
- Validate transactions and prevent insufficient-balance withdrawals
- Maintain transaction history with timestamps
- Manage multiple accounts
- Convert between INR, USD, and EUR using configured demo rates
- Automated unit tests using Python's unittest framework

## Technologies Used

- Python 3
- Object-Oriented Programming
- Decimal arithmetic
- Dataclasses
- Unit Testing

## Project Structure

```text
Banking Ledger Project/
├── main.py
├── src/
│   ├── account.py
│   ├── bank.py
│   ├── currency.py
│   ├── ledger.py
│   └── transaction.py
├── tests/
│   └── test_account.py
├── README.md
└── .gitignore
```

## Requirements

Python 3.10 or later recommended.

No external packages are required.

## Run the Project

Open a terminal in the project folder and run:

```bash
python main.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Currency Conversion

The project currently uses fixed demonstration exchange rates.
They are not live market rates and should not be used for real
financial transactions.

## Disclaimer

This is an educational banking simulation. It is not connected
to real bank accounts or payment systems.
