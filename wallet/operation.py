from money import Money


class Operation:

    def __init__(self, operation, currency, amount, date, tags=None):
        self.type_of_operation = TypeOfOperation()
        self.money = Money(currency, amount)
        self.deal_of_time = date
        self.tags = []
        self.tags.append(tags)

if __name__ == '__main__':
    from money import *
    op = Operation(1, 0, 345, '2016', 'family food')
    print(op.tags)
    enum = TypeOfOperation()

    a = enum.come_in
    b = enum.come_out
    print(a == b)

