from operation import *


class Wallet:
    operations = []
    moneys = {"currency": "amount"}

    def put_money(self, currency, amount, date, tags=None):
        oper = Operation(1, currency, amount, date, tags)
        self.operations.append(oper)

    def take_money(self, currency, amount, date, tags=None):
        self.operations.append(Operation(-1, currency, amount, date(), tags))

    def get_money(self, currency):  # how many money I have in wallet this currency
        pass


if __name__ == '__main__':
    from money import *
    w = Wallet(1, 0, 345, '2016')
    print(op.performent_of_date)