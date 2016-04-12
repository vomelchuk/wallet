import money
from enums import OperationType


class Operation:

    def __init__(self, operation, currency, amount, date, tags=[]):
        if operation in OperationType:
            self.type_of_operation = operation
        else:
            print("ERROR: Unsupported operation!")
        self.money = money.Money(currency, amount)
        self.deal_of_time = date
        self.tags = tags


if __name__ == '__main__':
    from money import *
    op = Operation(OperationType.get, CurrencyType.hrn, 345, '2016', 'family food')
    print(op.type_of_operation, op.money, op.deal_of_time, op.tags )


