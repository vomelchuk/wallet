class Money:
    type_currency = ["Usd", "Euro", "Hrn"]

    def __init__(self, index_currency, amount):
        self.currency = self.type_currency[index_currency]
        self.amount = amount

    def add_money(self, index_currency, val):
        self.amount += val
        self.currency = self.type_currency[index_currency]

    def __str__(self):
        return "Wallet has " + str(self.amount) + self.currency
        pass


class Wallet:
    tags = []

    def __init__(self):
        self.money = Money(0, 0)

    def put_money(self, amount):

        pass

    def take_money(self, amount):
        pass





