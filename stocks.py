class Stocks():
    def __init__(self, name, last, quantity):
        self.__name = name
        self.__last = last
        self.__quantity = quantity

    def getName(self):
        return self.__name
    def getLastPrice(self):
        return self.__last
    def getQuantity(self):
        return self.__quantity
    
    def setQuantity(self, value):
        self.__quantity = value
