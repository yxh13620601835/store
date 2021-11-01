'''
    车类：
    属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。
    功能：跑（要求参数传入车的具体功能，比如越野，赛车）
    创建：法拉利，宝马，铃木，五菱，拖拉机对象
'''
class Car:
    __type=""
    __wheelnum=0
    __color=""
    __weight=0.0
    __fuelstorge=0.0

    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type

    def setWheelNum(self,wheelnum):
        if wheelnum<0 or wheelnum>20:
            print("输入非法！")
        else:
            self.__wheelnum=wheelnum
    def getWheelNum(self):
        return self.__wheelnum

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

    def setFuelStorge(self,fuelstorge):
        if fuelstorge<0:
            print("输入非法！")
        else:
            self.__fuelstorge=fuelstorge
    def getFuelStorge(self):
        return self.__fuelstorge

    def introduce(self):
        print("%s的车有%d个车轮，车身颜色是%s，%.2f公斤，%.2fL油箱。"%
              (self.__type,self.__wheelnum,self.__color,self.__weight,self.__fuelstorge))

    def run(self,function):
        print("%s的功能是%s"%(self.__type,function))

if __name__=="__main__":
    falali=Car()
    falali.setType("法拉利")
    falali.setWheelNum(4)
    falali.setColor("黄色")
    falali.setWeight(5000.5)
    falali.setFuelStorge(30.5)
    falali.introduce()
    falali.run("赛车")

    baoma=Car()
    baoma.setType("宝马")
    baoma.setWheelNum(4)
    baoma.setColor("宝石蓝")
    baoma.setWeight(2300)
    baoma.setFuelStorge(40)
    baoma.introduce()
    baoma.run("赛车")

    lingmu=Car()
    lingmu.setType("铃木")
    lingmu.setWheelNum(4)
    lingmu.setColor("炫彩紫")
    lingmu.setWeight(5600)
    lingmu.setFuelStorge(60)
    lingmu.introduce()
    lingmu.run("越野")

    wuling=Car()
    wuling.setType("五菱")
    wuling.setWheelNum(4)
    wuling.setColor("粉色")
    wuling.setWeight(3200)
    wuling.setFuelStorge(28.3)
    wuling.introduce()
    wuling.run("越野")

    tuolaji=Car()
    tuolaji.setType("拖拉机")
    tuolaji.setWheelNum(3)
    tuolaji.setColor("绿色")
    tuolaji.setWeight(4800)
    tuolaji.setFuelStorge(48.3)
    tuolaji.introduce()
    tuolaji.run("拉货")