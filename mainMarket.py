import controllerMarket as cM
controllerMarkets = cM.ControllerMarket()

print("1 - Add Portfolio")
print("2 - Delete Portfolio")
print("3 - Buy stock for a client")
print("4 - Sell stock for a client")
print("5 - List a Client's Portfolio")
print("6 - Exit")
try:
    option = int(input("Option: "))

    while option != 6:
        if option == 1:
            try:
                dni = input("Input DNI: ")
                name = input("Input Name: ")
                surnames = input("Input Surnames: ")
                account = input("Input Account Number: ")
                balance = float(input("Input initial Balance: "))
                market = controllerMarkets.addPortfolio(dni, name, surnames, account, balance)
    
                if market:
                    print("\n¡Portafolio added succesfully!\n")
                else:
                    print("\n¡Portfolio could not be added!\n")

            except ValueError:
                print("\n¡!The balance needs to be a poitive Float\n")

        elif option == 2:
            dni = input("Input DNI: ")
            market = controllerMarkets.deletePortfolio(dni)

            if market:
                print("\n¡Portafolio deleted succesfully!\n")
            else:
                print("\n¡Portafolio could not be deleted!\n")

        elif option == 3:
            try:
                dni = input("Input DNI: ")
                allMarkets = controllerMarkets.listAllMarkets()
                for i in allMarkets:
                    print("Stock key:", i["tickerName"], "->", i["name"], ":", i["last"])
                stockName = input("Select stock: ")
                quantity = int(input("Input quantity: "))
                if quantity > 0:

                    stockAdded = controllerMarkets.buyStockClient(stockName, dni, quantity)

                    if stockAdded:
                        print("\n¡Stock bought successfully!\n")
                    else:
                        print("\n¡Stock could not be bought!\n")
                else:
                    print("\n¡The quantity needs to be a positive integer!\n")
            except ValueError:
                print("\n¡!The quantity needs to be a poitive Integer\n")
            except KeyError:
                print("\n¡Stock not found!\n")


        elif option == 4:
            try:
                dni = input("Input DNI: ")
                allMarkets = controllerMarkets.listAllMarkets()
                for i in allMarkets:
                    print("Stock key:", i["tickerName"], "->", i["name"], ":", i["last"])
                stockName = input("Select stock: ")
                quantity = int(input("Input quantity: "))
                if quantity > 0:
                    sellStock = controllerMarkets.sellStockClient(dni, stockName, quantity)
                    if sellStock:
                        print("\n¡Stock selled successfully!\n")
                    else:
                        print("\n¡Stock could not be selled!\n")
                else:
                    print("\n¡The quantity needs to be a positive integer!\n")
            except ValueError:
                print("\n¡!The quantity needs to be a poitive Integer\n")
            except KeyError:
                print("\n¡Stock not found!\n")

        elif option == 5:
            dni = input("Input DNI: ")
            portfolio = controllerMarkets.listPorfolioUser(dni)
            if portfolio == False:
                print("\n¡Dni not found!\n")
            else:
                print("\tDNI:", portfolio.getDni())
                print("\tName:", portfolio.getName())
                print("\tSurnames:", portfolio.getSurnames())
                print("\tAccount Number:", portfolio.getAccountNumber())
                print("\tBalance:", round(portfolio.getBalance(), 2))
                stocks = portfolio.getStocks()
                for i in stocks:
                    print("\t\tStock Name:", i.getName())
                    print("\t\tStock Last Price:", i.getLastPrice())
                    print("\t\tStock Quantity:", i.getQuantity(), "\n")

        else:
            print("\n¡Option not valid!\n")
        listPort = controllerMarkets.getlistPortfolios()
        print("Currently there are", len(listPort) , "portfolios registered!")
        print("1 - Add Portfolio")
        print("2 - Delete Portfolio")
        print("3 - Buy stock for a client")
        print("4 - Sell stock for a client")
        print("5 - List a Client's Portfolio")
        print("6 - Exit")
        option = int(input("Option: "))


    print("BYE 😊")
except IndexError:
    print("\n¡The option needs to be a integer!\n")


