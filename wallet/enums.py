from enum import Enum


class CurrencyType(Enum):
    hrn = "гривня"
    usd = "долар"
    euro = "євро"


class OperationType(Enum):
    put = "Покласти в гаманець"
    get = "Витягнути з гаманця"



if __name__ == '__main__':
    print(OperationType.put)

    for item in CurrencyType:
        print(item)

