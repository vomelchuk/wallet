import money
from enums import OperationType
from enums import CurrencyType


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