from wallet.money import Money
from wallet.enums import OperationType
from wallet.enums import CurrencyType
from datetime import date


class Operation:
    def __init__(self, operation, currency, amount, performDate, tags=[]):

        if operation not in OperationType:
            raise NameError("Unsupported operation!")
        if currency not in CurrencyType:
            raise NameError("Unsupported currency:", currency)

        self.operationType = operation
        self.money = Money(currency, amount)
        self.performDate = performDate
        self.tags = tags

    def get_operation(self):
        return [self.operationType.name, self.money.currency.name, self.money.amount, self.performDate, self.tags]

    def get_tags(self):
        result = '['
        for item in self.tags:
            result += '"' + item + '"' + ","
        result = result[:-1]
        result += ']'

        return result

    def to_json(self):
        return '{"operationType":"' + self.operationType.name + '",' + '"money":' + self.money.to_json() + ',"performDate":"' \
               + str(self.performDate) + '",' + '"tags":' + self.get_tags() + "}"
