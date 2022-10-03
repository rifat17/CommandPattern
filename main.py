from banking.bank import Bank
from banking.commands import Deposit, Withdraw, Transfer, Batch
from banking.constroller import BankController


def main() -> None:
    # create bank
    bank = Bank()

    # create bank controller
    controller = BankController()

    # create account
    account1 = bank.create_account("Sally")
    account2 = bank.create_account("Bob")
    account3 = bank.create_account("Ted")

    controller.execute(Batch(commands=[
        Deposit(account1, 1000),
        Deposit(account2, 1000),
        Deposit(account3, 1000),
    ]))
    # controller.execute(Deposit(account1, 1000))
    # controller.execute(Deposit(account2, 1000))
    # controller.execute(Deposit(account3, 1000))
    # controller.undo()
    # controller.redo()

    # account1.deposit(100)
    # account2.deposit(100)
    # account3.deposit(100)

    # transfer
    controller.execute(Transfer(from_account=account1, to_account=account2, amount=100))
    # account2.withdraw(100)
    # account1.deposit(100)

    # withdraw
    controller.execute(Withdraw(account1, 500))
    # account1.withdraw(50)

    controller.undo()
    print(bank)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
