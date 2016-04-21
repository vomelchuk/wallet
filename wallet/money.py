from enums import CurrencyType


class Money:

    def __init__(self, currency, amount):
        try:
            if currency not in CurrencyType:
                print("no")
                raise NameError
            else:
                print("yes")
                self.currency = currency
        except NameError:
            print("Unsupported currency:", currency)
        self.amount = amount


if __name__ == '__main__':
    #mon = Money(CurrencyType.HRN, 234)
    mon1 = Money(CurrencyType.USD, 234)


    mon2 = Money(CurrencyType.hRN, 45)
