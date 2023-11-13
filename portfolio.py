import baseModel
import stocks as st 
#BaseModel Herencia
        
class Portfolio(baseModel.BaseModel):
    def __init__(self, dni, name, surnames, accountNumber, balance, stocks):
        super().__init__(dni, name, surnames)
        self.__accountNumber = accountNumber
        self.__balance = balance
        self.__stocks = []

    def getAccountNumber(self):
        return self.__accountNumber
    def getBalance(self):
        return self.__balance
    def getStocks(self):
        return self.__stocks
    
    def setBalance(self, value):
        self.__balance = value
    
    def addStock(self, name, lastPrice, last, quantity):
        if lastPrice > self.getBalance():
            return False
        else:
            existStock = False
            for i in self.getStocks():
                if i.getName() == name:
                    existStock = True
                    quantity = quantity + i.getQuantity()
                    i.setQuantity(quantity)
                
            if existStock:
                balance = self.getBalance() - lastPrice
                self.setBalance(balance)
                return True
            else:
                stock = st.Stocks(name, last, quantity)
                self.__stocks.append(stock)
                balance = self.getBalance() - lastPrice
                self.setBalance(balance)
                return True
        
    def sellStock(self, name, sumBalance, quantity):
        stocks = self.getStocks()
        for i in stocks:
            if i.getName() == name:
                qunatDiff = i.getQuantity() - quantity
                if qunatDiff >= 0:
                    i.setQuantity(qunatDiff)
                    sumBalance = sumBalance + self.getBalance()
                    self.setBalance(sumBalance)
                    if qunatDiff == 0:
                        self.getStocks().remove(i)
                    return True
                else:
                    return False
        return False

