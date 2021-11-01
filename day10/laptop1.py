'''
    笔记本：
    属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。
    行为：打游戏（传入游戏的名称）,办公。
'''
class Laptop:
    __type=""
    __standbytime=0.0
    __color=""
    __weight=0.0
    __cputype=""
    __memorysize=0
    __harddisksize=0

    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type

    def setStandByTime(self,standbytime):
        if standbytime<0:
            print("输入非法！")
        else:
            self.__standbytime=standbytime
    def getStandByTime(self):
        return self.__standbytime

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        if weight<0:
            print("输入非法！")
        else:
            self.__weight=weight
    def getWeight(self):
        return self.__weight

    def setCpuType(self, cputype):
        self.__cputype = cputype

    def getCpuType(self):
        return self.__cputype

    def setMemorySize(self, memorysize):
        if memorysize < 0:
            print("输入非法！")
        else:
            self.__memorysize = memorysize

    def getMemorySize(self):
        return self.__memorysize

    def setHardDiskSize(self, harddisksize):
        if harddisksize < 0:
            print("输入非法！")
        else:
            self.__harddisksize = harddisksize

    def getHardDiskSize(self):
        return self.__harddisksize

    def introduce(self):
        print("%s笔记本电脑的待机时间是%d，颜色是%s，%.2f公斤，CPU是%s，内存%dG，硬盘%dG"%
              (self.__type,self.__standbytime,self.__color,self.__weight,self.__cputype,self.__memorysize,self.__harddisksize))

    def game(self,game):
        print("正在玩%s······"%game)

    def work(self):
        print("办公中，请勿扰······")

if __name__=="__main__":
    computer = Laptop()
    computer.setType("ThinkPad")
    computer.setStandByTime(24)
    computer.setColor("金色")
    computer.setWeight(5.3)
    computer.setCpuType("酷睿i5")
    computer.setMemorySize(6)
    computer.setHardDiskSize(128)
    computer.introduce()
    computer.game("英雄联盟")
    computer.work()