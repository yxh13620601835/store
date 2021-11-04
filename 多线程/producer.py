'''
    生产者类
'''
from threading import Thread
from kfc import *
import time
class Producer(Thread):
    __name=""
    __count=0
    __money=0
    __kfc=None
    def __init__(self,name,kfc):
        Thread.__init__(self)
        self.name=name
        self.__kfc=kfc

    def getCount(self):
        return self.__count

    def setMoney(self,money):
        if money<0:
            print("输入非法！")
        else:
            self.__money=money
    def getMoney(self):
        return self.__money

    def run(self) -> None:
        while True:
            if self.__kfc.getBasket()==500:
                time.sleep(3)
                print(self.name,"总共做了",self.__count,"个蛋挞,工资是",self.__money)

            elif self.__kfc.getBasket()<500 and self.__kfc.getBasket()>=0:
                self.__count +=1
                self.__kfc.setBasket(self.__kfc.getBasket()+1)
                self.__money = self.__count*12
                self.__kfc.setMoney(self.__kfc.getMoney()-12)
                print(self.name, "做了", self.__count, "个蛋挞")
            # if self.__kfc.getBasket()>500:
            #     print(self.name,"总共做了",self.__count,"个蛋挞,工资是",self.__money)
            #     break


