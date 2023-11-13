class BaseModel():
    def __init__(self, dni, name, surnames):
        self.__dni = dni
        self.__name = name
        self.__surnames = surnames

    def getDni(self):
        return self.__dni
    def getName(self):
        return self.__name
    def getSurnames(self):
        return self.__surnames
    def __str__(self):
        return self.__surnames + ", " + self.__name + ", " + self.__dni
        