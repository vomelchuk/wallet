from wallet.operation import Operation
from wallet.enums import CurrencyType
from wallet.enums import OperationType


class Wallet:
    def __init__(self):
        self.operations = []
        self.moneys = {item: 0 for item in CurrencyType}

    def put_money(self, currency, amount, deal_of_date, tags=[]):
        self.operations.append(Operation(OperationType.PUT, currency, amount, deal_of_date, tags))
        self.moneys[currency] += amount

    def take_money(self, currency, amount, deal_of_date, tags=[]):
        if self.get_money(currency) < amount:
            return None
        self.operations.append(Operation(OperationType.GET, currency, amount, deal_of_date, tags))
        self.moneys[currency] -= amount
        return 1

    def get_money(self, currency):
        return self.moneys[currency]

    def get_operations(self, currency):
        operations = []
        for operation in self.operations:
            if operation.money.currency == currency:
                operations.append(operation.get_operation())
        return operations

    def to_json(self):

        operations = []
        for item in self.operations:
            operations.append(item.to_json())

        moneys = {}
        for item2 in self.moneys:
            moneys[str(item2.value)] = self.moneys[item2]

        result = str(dict(operations=operations, moneys=moneys)).replace("'", '"')
        return result
