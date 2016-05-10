from wallet.enums import CurrencyType


class Money:
    def __init__(self, currency, amount):
        if currency not in CurrencyType:
            raise NameError("Unsupported currency:", currency)

        self.currency = currency
        self.amount = amount

    def to_json(self):
        return dict(currency=self.currency.value, amount=self.amount)
