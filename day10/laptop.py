'''
    笔记本电脑
    属性：屏幕大小，价格，cpu型号，内存大小，待机时长
    方法：打字，打游戏，看视频
'''
class Laptop:
    __brand = ""
    __screensize = 0.0
    __price = 0.0
    __cputype = ""
    __memorysize = 0.0
    __standbytime = 0


    def setBrand(self,brand):
        if brand.isdigit():
            print("输入非法！")
        else:
            self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setScreenSize(self,screensize):
        if screensize<0 or screensize>20:
            print("输入非法！")
        else:
            self.__screensize = screensize
    def getScreenSize(self):
        return self.__screensize

    def setPrice(self,price):
        if price<0 or price>1000000:
            print("输入非法！")
        else:
            self.__price = price
    def getPrice(self):
        return self.__price

    def setCpuType(self,cputype):
        if cputype.isdigit():
            print("输入非法！")
        else:
            self.__cputype = cputype
    def getCpuType(self):
        return self.__cputype

    def setMemorySize(self,memorysize):
        if memorysize<0 or memorysize>1024:
            print("输入非法！")
        else:
            self.__memorysize = memorysize
    def getMemorySIze(self):
        return self.__memorysize

    def setStandByTime(self,standbytime):
        if standbytime<0 or standbytime>168:
            print("输入非法！")
        else:
            self.__standbytime=standbytime
    def getStandByTime(self):
        return self.__standbytime

    def showLaptop(self):
        print(self.__brand,"笔记本电脑的屏幕是",self.__screensize,"寸，CPU型号是",
              self.__cputype,"内存是",self.__memorysize,"G，待机",self.__standbytime,"小时，价格是",
              self.__price,"元。")

    def typeWriting(self):
        print("正在打字中······")

    def playGame(self):
        print("正在打游戏中······")

    def watching(self):
        print("正在看视频中······")

if __name__ == "__main__":
    laptop = Laptop()
    laptop.setBrand("华硕")
    laptop.setScreenSize(15.6)
    laptop.setPrice(5600)
    laptop.setCpuType("酷睿i7")
    laptop.setMemorySize(2)
    laptop.setStandByTime(12)

    laptop.showLaptop()
    laptop.typeWriting()
    laptop.playGame()
    laptop.watching()