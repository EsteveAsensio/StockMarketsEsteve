import portfolio as po
import requests

#ANA:SM, ANE:SM, AENA:SM, ACX:SM, AMS:SM, ACS:SM, SAN:SM, BBVA:SM, CABK:SM, CLNX:SM, ENG:SM, ELE:SM, FER:SM, GRF:SM, IAG:SM, IBE:SM, ITX:SM, IDR:SM, MAP:SM, MEL:SM, NTGY:SM, REP:SM, TEF:SM, UNI:SM, SLR:SM, SOL:SMclass ControllerMarket:
class ControllerMarket():

    def __init__(self):
        self.__listPortfolios = {}

    def addPortfolio(self, dni, name, surnames, accountNumber, balance):
        if balance < 0:
            raise ValueError
        else:
            if dni not in self.__listPortfolios:
                port = po.Portfolio(dni, name, surnames, accountNumber, balance, None)
                self.__listPortfolios[dni] = port
                return True
            return False
        
    def deletePortfolio(self, dni):
        if dni in self.__listPortfolios:
            self.__listPortfolios.pop(dni)
            return True
        else:
            return False 
        
    def listAllMarkets(self):
        url = "https://bb-finance.p.rapidapi.com/market/get-full"

        querystring = {"id":"ANA:SM, ANE:SM, AENA:SM, ACX:SM, AMS:SM, ACS:SM, SAN:SM, BBVA:SM, CABK:SM, CLNX:SM, ENG:SM, ELE:SM, FER:SM, GRF:SM, IAG:SM, IBE:SM, ITX:SM, IDR:SM, MAP:SM, MEL:SM, NTGY:SM, REP:SM, TEF:SM, UNI:SM, SLR:SM, SOL:SM"}

        headers = {
            "X-RapidAPI-Key": "9ce6b7b13amshb7fa76956d29723p1e82f8jsn28537b61e560",
            "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        listMarket = []

        for i in data["result"].values():
            tickerName = i["tickerName"]
            name = i["name"]
            last = i["last"]
            stock_data = {"tickerName": tickerName, "name": name, "last": last}
            listMarket.append(stock_data)

        return listMarket


    def buyStockClient(self, name, dni, quantity):
            try:
                url = "https://bb-finance.p.rapidapi.com/market/get-full"

                querystring = {"id": name}

                headers = {
                    "X-RapidAPI-Key": "9ce6b7b13amshb7fa76956d29723p1e82f8jsn28537b61e560",
                    "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers, params=querystring)
                data = response.json()

                for i in data["result"].values():
                    nameStock = i["name"]
                    last = i["last"]

                balance = float(last) * quantity
                
                if dni in self.__listPortfolios:
                    port = self.__listPortfolios[dni]
                    stock = port.addStock(nameStock, balance, last, quantity)
                    return stock
                return False
            except KeyError:
                raise KeyError
        
    def sellStockClient(self, dni, sotckName, quantity):
        try:
            url = "https://bb-finance.p.rapidapi.com/market/get-full"

            querystring = {"id": sotckName}

            headers = {
                "X-RapidAPI-Key": "9ce6b7b13amshb7fa76956d29723p1e82f8jsn28537b61e560",
                "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            for i in data["result"].values():
                name = i["name"]
                last = i["last"]

            sumBalance = float(last) * quantity
                
            if dni in self.__listPortfolios:
                port = self.__listPortfolios[dni]
                stock = port.sellStock(name, sumBalance, quantity)
                return stock
            return False
        except KeyError:
            raise KeyError


    def listPorfolioUser(self, dni):
        if dni in self.__listPortfolios:
            portfolio = self.__listPortfolios[dni]
            return portfolio
        return False 

    def getlistPortfolios(self):
        return self.__listPortfolios

