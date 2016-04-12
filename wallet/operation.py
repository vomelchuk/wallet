from money import Money


class Operation:

    def __init__(self, operation, currency, amount, date, tags=None):
        if operation in ['in', 'out']:
            self.type_of_operation = operation
        else:
            print("ERROR: Incorrect type of the operation!\n")
        self.money = Money(currency, amount)
        self.deal_of_time = date
        self.tags = []
        self.tags.append(tags)

if __name__ == '__main__':
    from money import *
    op = Operation('in', 'usd', 345, '2016', 'family food')
    print(op.type_of_operation, op.money, op.deal_of_time, op.tags )


