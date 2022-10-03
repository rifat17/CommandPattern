from dataclasses import dataclass


@dataclass
class Account:
    name: str
    number: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
