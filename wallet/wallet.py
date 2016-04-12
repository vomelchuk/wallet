from operation import *
from datetime import date


class Wallet:

    def __init__(self):
        self.operations = []
        self.operation = None

    def put_money(self, currency, amount, deal_of_date=date.today(), tags=None):
        self.operation = Operation('in', currency, amount, deal_of_date, tags)
        self.operations.append(self.operation)

    def take_money(self, currency, amount, deal_of_date=date.today(), tags=None):
        if self.get_money(currency) < amount:
            print("ERROR: attempting take out ", amount, currency, ": you haven`t money for this "
                "operation! You have only", self.get_money(currency), currency)
            return
        self.operation = Operation('out', currency, amount, deal_of_date, tags)
        self.operations.append(self.operation)

    def get_money(self, currency):
        count = 0
        for item in self.operations:
            if item.money.currency == currency:
                count += item.money.amount
        return count

    def get_operations(self):
        for item in self.operations:
            print('Operation:', item.type_of_operation, 'Currency:',
                  item.money.currency, 'Sum:',item.money.amount, 'Date:', item.deal_of_time,
                  'Tags:', item.tags)


if __name__ == '__main__':
    from money import *
    w = Wallet()
    w.put_money('hrn', 100, 2016, 'food family')
    w.put_money('usd', 345, 2016, 'food family')
    w.put_money('usd', 1000, 2016, 'food clothes')
    w.take_money('hrn', 1000, 2016, 'food clothes')
    w.put_money('usd', 1000)
    w.get_operations()
