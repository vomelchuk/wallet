import wallet
from enums import CurrencyType, OperationType

w = wallet.Wallet()


def print_head(title):
    head = title
    gaps = len(head) * "-"
    print("{0}\n{1}\n{2}".format(gaps, head, gaps))


def get_currency():
    """ Return right value of currency """
    # forming list all types of currency
    currency_list = " "
    for item in CurrencyType:
        currency_list += str(item.value) + "-" + item.name + " "
    # user`s choice
    currency = int(input("Choose currency (" + currency_list + "): "))
    currency = CurrencyType(currency)
    return currency


def show():
    """ Show us how much money choosing currency we have got"""
    print_head("How much money you have")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    print("You have", w.get_money(currency), currency.name)


def put():
    print_head("Operation: get money")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    tags = input("Tags:").split()
    w.put_money(currency, amount, operation_date, tags)


def take():
    print_head("Operation: take money")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    tags = input("Tags:").split()
    w.take_money(currency, amount, operation_date, tags)


def reports():
    pass


while True:
    print_head("MENU")
    print(
        "1. View your wallet\n2. Put money from wallet\n3. Take money to wallet\n4. Reports(is developing...)\n5. Exit")
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
        print("Incorrect choice!")
