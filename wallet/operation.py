import wallet.money
from wallet import money
from wallet.enums import OperationType
from wallet.enums import CurrencyType


class Operation:
    def __init__(self, operation, currency, amount, date, tags=[]):
        if operation not in OperationType:
            raise NameError("Unsupported operation!")
        if currency not in CurrencyType:
            raise NameError("Unsupported currency:", currency)

        self.type_of_operation = operation
        self.money = money.Money(currency, amount)
        self.performDate = date
        self.tags = tags

    def get_operation(self):
        return [self.type_of_operation, self.money, self.performDate, self.tags]
