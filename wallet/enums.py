from enum import Enum


class CurrencyType(Enum):
    HRN, USD, EURO = range(3)


class OperationType(Enum):
    PUT, GET = range(2)


