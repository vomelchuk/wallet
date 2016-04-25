import money
from enums import OperationType
from enums import CurrencyType


class Operation:

    def __init__(self, operation, currency, amount, date, tags=[]):
        if operation not in OperationType:
            raise NameError("Unsupported operation!")

        self.type_of_operation = operation
        self.money = money.Money(currency, amount)
        self.performDate = date
        self.tags = tags

if __name__ == '__main__':
    op = Operation(OperationType.PUT, CurrencyType.HRN, 450, '2016')

