from dataclasses import dataclass, field

from banking.account import Account
from banking.transaction import Transaction


@dataclass
class Deposit:
    account: Account
    amount: float

    @property
    def transaction_details(self) -> str:
        return f'Depositing {self.amount} to {self.account.name}'

    def execute(self) -> None:
        self.account.deposit(self.amount)
        print(self.transaction_details)

    def undo(self) -> None:
        self.account.withdraw(self.amount)
        print(f"Undid {self.transaction_details}")

    def redo(self) -> None:
        # self.execute()
        self.account.deposit(self.amount)
        print(f"Redid {self.transaction_details}")


@dataclass
class Withdraw:
    account: Account
    amount: float

    @property
    def transaction_details(self) -> str:
        return f'Withdrawing {self.amount} from {self.account.name}'

    def execute(self) -> None:
        self.account.withdraw(self.amount)
        print(self.transaction_details)

    def undo(self) -> None:
        self.account.deposit(self.amount)
        print(f"Undid {self.transaction_details}")

    def redo(self) -> None:
        # self.execute()
        self.account.withdraw(self.amount)
        print(f"Redid {self.transaction_details}")


@dataclass
class Transfer:
    from_account: Account
    to_account: Account
    amount: float

    @property
    def transaction_details(self) -> str:
        return f'Transferring {self.amount} from {self.from_account.name} to {self.to_account.name}'

    def execute(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(self.transaction_details)

    def undo(self) -> None:
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)
        print(f"Undid {self.transaction_details}")

    def redo(self) -> None:
        # self.execute()
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Redid {self.transaction_details}")


@dataclass
class Batch:
    commands: list[Transaction] = field(default_factory=list)

    def execute(self) -> None:
        completed_commands = []
        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)
        except ValueError as e:
            print(e)
            for command in reversed(completed_commands):
                command.undo()

    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()

    def redo(self) -> None:
        for command in self.commands:
            command.redo()
