class Money:

    currency = None
    amount = None

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return "[Currency:" + str(self.currency) + ", amount:" + str(self.amount) + "]"


class Operation:

    type_of_operation = None
    date_of_waste = None
    money = None
    tag = None

    def __init__(self, operation, currency, amount, date, tags=None):
        self.money = Money(currency, amount)
        self.date_of_waste = date
        self.type_of_operation = operation
        self.tag = tags


class Wallet:
    operations = []

    def put_money(self, currency, amount, date, tag=None):
        oper = Operation(1, currency, amount, date, tag)
        self.operations.append(oper)

    def take_money(self, currency, amount, date, tag=None):
        self.operations.append(Operation(-1, currency, amount, date(), tag))


obj = Wallet()

obj.put_money(0, 1000, '2016', 'Clothes children')
obj.put_money(1, 150, '2015', 'foods')
obj.put_money(0, 1250, '2015')

for item in obj.operations:
    print("Date: {0}, money: {1}, tags: {2}".format(item.date_of_waste, str(item.money), item.tag))
