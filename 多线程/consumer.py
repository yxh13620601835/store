'''
    消费者类
'''
from threading import Thread
from kfc import *
import time

class Consumer(Thread):
    __name=""
    __count=0
    __money=3000
    __kfc=None

    def __init__(self,name,kfc):
        Thread.__init__(self)
        self.name=name
        self.__kfc=kfc


    def getCount(self):
        return self.__count

    def getMoney(self):
        return self.__money

    def run(self) -> None:
        while True:
            if self.__kfc.getBasket()==0:
                time.sleep(3)
            elif self.__kfc.getBasket()>0 and self.__kfc.getBasket()<=500 and self.__money>0:
                self.__count += 1
                self.__kfc.setBasket(self.__kfc.getBasket()-1)
                self.__money -= 3
                self.__kfc.setMoney(self.__kfc.getMoney()+3)
                print(self.name, "买了", self.__count, "个蛋挞")
            elif self.__money<=0:
                print(self.name, "总共买了", self.__count, "个蛋挞,还剩钱", self.__money,"元")
                break

