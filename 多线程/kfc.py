'''
    蛋挞店类
'''

class KFC:
    __money=0
    __basket=500

    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money

    def setBasket(self,basket):
        self.__basket=basket
    def getBasket(self):
        return self.__basket

