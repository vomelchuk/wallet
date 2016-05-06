import wallet.operation
from wallet import operation
from wallet.enums import CurrencyType
from wallet.enums import OperationType


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
        return 1

    def get_money(self, currency):
        return self.moneys[currency]

    def get_operations(self, currency):
        operations = []
        for operation in self.operations:
            if operation.money.currency == currency:
                operations.append((operation.operationType.name, operation.money.currency.name,
                                   operation.money.amount, operation.performDate, operation.tags))
        return operations