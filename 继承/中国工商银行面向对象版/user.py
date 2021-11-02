'''
    用户类
'''
import random

class User:
    __account=random.randint(10000000,99999999)
    __username=""
    __password=""
    __address=None
    __money=0.0
    __bankname="中国工商银行昌平支行"

    def getAccount(self):
        return self.__account

    def setUserName(self,username):
        self.__username=username
    def getUserName(self):
        return self.__username

    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password

    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address

    def setMoney(self,money):
        if money<0:
            print("输入非法！")
        else:
            self.__money=money
    def getMoney(self):
        return self.__money

    def getBankName(self):
        return self.__bankname