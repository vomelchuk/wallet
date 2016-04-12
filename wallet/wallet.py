import operation
import datetime
from enums import CurrencyType
from enums import OperationType


class Wallet:

    def __init__(self):
        self.operations = []
        self.moneys = {item: 0 for item in CurrencyType}

    def put_money(self, currency, amount, deal_of_date=datetime.date.today(), tags=[]):
        self.operations.append(operation.Operation(OperationType.put,currency, amount, deal_of_date, tags))
        self.moneys[currency] += amount

    def take_money(self, currency, amount, deal_of_date=datetime.date.today(), tags=[]):
        if self.get_money(currency) < amount:
            print("ERROR: attempting take out ", amount, currency, ": you haven`t money for this "
                "operation! You have only", self.get_money(currency), currency)
            return None
        self.operations.append(operation.Operation(OperationType.get, currency, amount, deal_of_date, tags))
        self.moneys[currency] -= amount

    def get_money(self, currency):
        return self.moneys[currency]

    def get_operations(self):
        for item in self.operations:
            print('|Operation:', item.type_of_operation.value, '|Currency:',
                  item.money.currency.value, '|Sum:', item.money.amount, '|Date:', item.deal_of_time,
                  '|Tags:', item.tags)


if __name__ == '__main__':
    import operation
    w = Wallet()
    w.put_money(CurrencyType.usd, 150, '2016-04-12', 'monitor technics')
    w.put_money(CurrencyType.usd, 98, '2016-04-12', 'clothes jeans')
    w.put_money(CurrencyType.euro, 50, '2016-04-08', 'sallary')
    w.put_money(CurrencyType.usd, 5)
    w.get_operations()
    print(CurrencyType.usd.value, w.get_money(CurrencyType.usd))
    w.take_money(CurrencyType.usd, 5, '2016-04-12', 'food bread')
    w.get_operations()
    print(CurrencyType.usd.name, w.get_money(CurrencyType.usd))
