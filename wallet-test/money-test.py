import unittest
import wallet.money
import wallet.enums as enum


class TestMoney(unittest.TestCase):
    pass

w = wallet.money.Money(enum.CurrencyType.USD, 456)

if __name__ == '__main__':
    # w = wallet.money.Money(CurrencyType.USD, 456)
    pass
    # unittest.main()