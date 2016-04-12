from enums import CurrencyType


class Money:

    # currency global variables constans
    # throw exeption

    def __init__(self, currency, amount):
        if currency in CurrencyType:
            self.currency = currency
        else:
            print('ERROR: Unsupported currency!')
        self.amount = amount

    def __str__(self):
        return "[Currency:" + str(self.currency) + ", amount:" + str(self.amount) + "]"


if __name__ == '__main__':
    m = Money(CurrencyType.hrn1, 345)
    print(m.currency, ": ", m.amount)
    print(str(m))
    # print(m.something)
    pass
