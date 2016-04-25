from enums import CurrencyType


class Money:

    def __init__(self, currency, amount):
        if currency not in CurrencyType:
            raise NameError("Unsupported currency:", currency)

        self.currency = currency
        self.amount = amount


if __name__ == '__main__':
    mon = Money(CurrencyType.HRN, 234)
    mon1 = Money(CurrencyType.USD, 234)

    #asd = CurrencyType.hRN
    mon2 = Money(CurrencyType2.hRN, 45)