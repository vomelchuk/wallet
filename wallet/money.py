class Money:

    def __init__(self, currency, amount):
        if currency in ['hrn', 'usd', 'euro']:
            self.currency = currency
        else:
            print('ERROR: Incorrect value of the currrency!\n')
        self.amount = amount

    def __str__(self):
        return "[Currency:" + str(self.currency) + ", amount:" + str(self.amount) + "]"

if __name__ == '__main__':
    m = Money("usd", 345)
    print(m.currency, ": ", m.amount)
    print(str(m))
    # print(m.something)
    pass
