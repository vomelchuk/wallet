from wallet.wallet import Wallet
from wallet.enums import CurrencyType
import os


def print_head(title):
    head = title
    gaps = len(head) * "-"
    print("{0}\n{1}\n{2}".format(gaps, head, gaps))


def clear():
    os.system("clear")


def return_to_menu():
    if input("Return to menu (y - Yes) ? ").upper() != "Y":
        return True
    return False


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
    clear()
    print_head("How much money you have")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    print("You have", w.get_money(currency), currency.name)
    if return_to_menu():
        show()


def put():
    clear()
    print_head("Operation: put money into wallet")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    tags = input("Tags (through `;`):").split(";")
    w.put_money(currency, amount, operation_date, tags)
    if return_to_menu():
        put()


def take():
    clear()
    print_head("Operation: take money from wallet")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    tags = input("Tags (through `;`):").split(";")
    if w.take_money(currency, amount, operation_date, tags) is False:
        print("Operation denied! You have less than need!")
    if return_to_menu():
        take()


def reports():
    clear()
    print_head("Report")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    result = w.get_operations(currency)
    for item in result:
        print(item)
    print("Remain:", w.get_money(currency), currency.name)
    if not len(result):
        print("Nothing was made")
    if return_to_menu():
        take()


w = Wallet()
while True:
    clear()
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
