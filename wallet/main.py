import wallet
from enums import CurrencyType, OperationType

w = wallet.Wallet()

1
def show():
    choice_currency = int(input("Give the currency type, please (1 - hrn, 2 - usd, 3 - euro): "))
    if choice_currency == 1:
        print("You have", w.get_money(CurrencyType.HRN), "HRN")
    if choice_currency == 2:
        print("You have", w.get_money(CurrencyType.USD), "USD")
    if choice_currency == 3:
        print("You have", w.get_money(CurrencyType.EURO), "EURO")


# Menu
def take():
    print("---------------------")
    print("Operation: take money")
    print("---------------------")
    currency = int(input("Choose currency (1 - hrn, 2 - usd, 3 - euro): "))
    if currency == 1:
        currency = CurrencyType.HRN
    if currency == 2:
        currency = CurrencyType.USD
    if currency == 3:
        currency = CurrencyType.EURO
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    tags = input("Tags:").split()
    w.take_money(currency, amount, operation_date, tags)


def put():
    print("---------------------")
    print("Operation: get money")
    print("---------------------")
    currency = int(input("Choose currency (1 - hrn, 2 - usd, 3 - euro): "))
    if currency == 1:
        currency = CurrencyType.HRN
    if currency == 2:
        currency = CurrencyType.USD
    if currency == 3:
        currency = CurrencyType.EURO
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    tags = input("Tags:").split()
    w.put_money(currency, amount, operation_date, tags)


def reports():
    pass

while True:
    print("\n1. View your wallet\n2. Put money from wallet\n3. Take money to wallet\n4. Reports\n5.Exit")
    try:
        choice = int(input("? "))

        if choice == 1:
            show()
        if choice == 2:
            put()
        if choice == 3:
            take()
        if choice == 4:
            reports()
        if choice == 5:
            break
    except ValueError:
        print("Incorrect data!")
