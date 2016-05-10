from wallet.wallet import Wallet
from wallet.enums import CurrencyType
from datetime import date
import os
import pickle
import json


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


def show(obj):
    """ Show us how much money choosing currency we have got"""
    clear()
    print_head("How much money you have")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    print("You have", obj.get_money(currency), currency.name)
    if return_to_menu():
        show(obj)


def put(obj):
    clear()
    print_head("Operation: put money into wallet")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    amount = float(input("amount: "))
    operation_date = input("Date (yyyy-mm-dd): ")
    if len(operation_date) == 0:
        operation_date = date.today()
    else:
        operation_date = operation_date.split("-")
        operation_date = date(int(operation_date[0]), int(operation_date[1]), int(operation_date[2]))
    tags = input("Tags (through `;`):").split(";")
    obj.put_money(currency, amount, operation_date, tags)
    if return_to_menu():
        put(obj)


def take(obj):
    clear()
    print_head("Operation: take money from wallet")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    amount = float(input("amount: "))
    operation_date = input("Date: ")
    if len(operation_date) == 0:
        operation_date = date.today()
    else:
        operation_date = operation_date.split("-")
        operation_date = date(int(operation_date[0]), int(operation_date[1]), int(operation_date[2]))
    tags = input("Tags (through `;`):").split(";")
    if obj.take_money(currency, amount, operation_date, tags) is None:
        print("Operation denied! You have less than need!")
    if return_to_menu():
        take(obj)


def reports(obj):
    clear()
    print_head("Report")
    currency = get_currency()
    if currency is None:
        print("Incorrect choice!")
        return
    result = obj.get_operations(currency)
    for item in result:
        print(item)
    print("Remain:", obj.get_money(currency), currency.name)
    if not len(result):
        print("Nothing was made")
    if return_to_menu():
        reports(obj)


def file_open(obj):
    clear()
    print_head("Opening file")
    file_name = input("Type a file name: ")

    if not os.path.isfile(file_name):
        print("File doesn`t exist!")
        if return_to_menu():
            file_open(obj)
        return

    file = open(file_name, 'rb')
    global wallet
    wallet = pickle.load(file)
    file.close()


def file_open_json(obj):
    clear()
    print_head("Opening file")
    file_name = input("Type a file name: ")

    if not os.path.isfile(file_name):
        print("File doesn`t exist!")
        if return_to_menu():
            file_open_json(obj)
        return

    file = open(file_name, 'r')
    data = file.read()
    file.close()
    parse_json = json.loads(data)
    for item in parse_json["operations"]:
        currency = CurrencyType(item['money']['currency'])
        amount = item['money']['amount']
        raw_date = item['performDate'].split('-')
        perform_date = date(int(raw_date[0]), int(raw_date[1]), int(raw_date[2]))
        tags = item['tags']
        if item['operationType'] == 1:
            obj.put_money(currency, amount, perform_date, tags)
        if item['operationType'] == 2:
            obj.take_money(currency, amount, perform_date, tags)


def file_save(obj):
    clear()
    print_head("Saving file")
    file_name = input("Type a file name: ")
    file = open(file_name, 'wb')
    pickle.dump(obj, file)
    file.close()


def file_save_json(obj):
    clear()
    print_head("Saving file")
    file_name = input("Type a file name: ")
    file = open(file_name, 'w')
    file.write(obj.to_json())
    file.close()


wallet = Wallet()
menu = {"1": [show, "View your wallet"], "2": [put, "Put money to wallet"], "3": [take, "Take money from wallet"],
        "4": [reports, "Reports"], "5": [file_open, "Open file"], "6": [file_save, "Save file"],
        "7": [file_save_json, "Save file to JSON"], "8": [file_open_json, "Open file from JSON"], "9": [exit, "Exit"]}
while True:
    clear()
    print_head("MENU")
    for item in sorted(menu.keys()):
        print(item, end='')
        print(".", menu[item][1])

    try:
        choice = input("? ")
        function = menu[choice][0]
        function(wallet)
    except ValueError:
        print("Incorrect choice!")
