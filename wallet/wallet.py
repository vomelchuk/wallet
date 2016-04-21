import operation
from enums import CurrencyType
from enums import OperationType


class Wallet:

    def __init__(self):
        self.operations = []
        self.moneys = {item: 0 for item in CurrencyType}

    def put_money(self, currency, amount, deal_of_date, tags=[]):
        self.operations.append(operation.Operation(OperationType.PUT, currency, amount, deal_of_date, tags))
        self.moneys[currency] += amount

    def take_money(self, currency, amount, deal_of_date, tags=[]):
        if self.get_money(currency) < amount:
            return None
        self.operations.append(operation.Operation(OperationType.GET, currency, amount, deal_of_date, tags))
        self.moneys[currency] -= amount

    def get_money(self, currency):
        return self.moneys[currency]

if __name__ == '__main__':
    w = Wallet()

    w.put_money(CurrencyType.HRN, 345, '2016', ["clothes", "wife"])
    w.take_money(CurrencyType.HRN, 20, '2016')

    a = w.get_money(CurrencyType.HRN)
    print(a)