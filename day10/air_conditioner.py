'''
    定义一个空调类和对应的测试类
    1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
    2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
    3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
    4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
    5、使用空调对象获取空调的品牌和价格并打印到控制台上；
    6、使用空调对象调用开机方法；
    7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
    其中语句中的“xxx”是调用方法时传递的具体数据值；
'''

class AirConditioner:
    __brand = ""
    __price= 0.0

    def setBrand(self,brand):
        if brand.isdigit():
            print("输入非法！")
        else:
            self.__brand=brand
    def getBrand(self):
        return self.__brand

    def setPrice(self,price):
        if price<0:
            print("输入非法！")
        else:
            self.__price=price
    def getPrice(self):
        return self.__price

    def start(self):
        print("空调开机了...")

    def shutdown(self,minute=0):
        print("空调将在%d分钟后自动关闭..."%(minute))

class Test:

    def __init__(self,brand,price):
        self.air = AirConditioner()
        self.air.setBrand(brand)
        self.air.setPrice(price)


if __name__=="__main__":
    test= Test("格力",10000)
    test.air.start()
    test.air.shutdown(52)