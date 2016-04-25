from enums import CurrencyType


class Money:

    def __init__(self, currency, amount):
        if currency not in CurrencyType:
            raise NameError("Unsupported currency:", currency)

        self.currency = currency
        self.amount = amount