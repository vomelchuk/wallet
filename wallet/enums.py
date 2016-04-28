from enum import Enum


class CurrencyType(Enum):
    HRN, USD, EURO, ZLT = range(1, 5)


class OperationType(Enum):
    PUT, GET = range(1, 3)
