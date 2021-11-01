'''
    人类：
    属性:
    姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
    功能：
    发短信（要求参数传入短信内容）。
    打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，按照时间长度扣费并返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））
'''
class Person:
    __name=""
    __sex=""
    __age=0
    __phonecharge=0.0   #手机剩余话费
    __phonebrand="" #手机品牌
    __battery=0
    __screensize=0.0
    __standbytime=0
    __scorecard=0.0 #积分

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setSex(self,sex):
        if sex=="男" or sex=="女":
            self.__sex=sex
        else:
            print("输入非法！")
    def getSex(self):
        return self.__sex

    def setAge(self,age):
        if age<0 or age>150:
            print("输入非法！")
        else:
            self.__age=age
    def getAge(self):
        return self.__age

    def setPhoneCharge(self,phonecharge):
        if phonecharge<0:
            print("输入非法！")
        else:
            self.__phonecharge=phonecharge
    def getPhoneCharge(self):
        return self.__phonecharge

    def setPhoneBrand(self,phonebrand):
        self.__phonebrand=phonebrand
    def getPhoneBrand(self):
        return self.__phonebrand

    def setBattery(self,battery):
        if battery<0:
            print("输入非法！")
        else:
            self.__battery=battery
    def getBattery(self):
        return self.__battery

    def setScreenSize(self,screensize):
        if screensize<0:
            print("输入非法！")
        else:
            self.__screensize=screensize
    def getScreenSize(self):
        return self.__screensize

    def setStandByTime(self,standbytime):
        if standbytime<0:
            print("输入非法！")
        else:
            self.__standbytime = standbytime
    def getStandByTime(self):
        return self.__standbytime

    def setScoreCard(self,scorecard):
        if scorecard<0:
            print("输入非法！")
        else:
            self.__scorecard = scorecard
    def getScoreCard(self):
        return self.__scorecard

    def introduce(self):
        print("我叫%s，%s性，%d岁，手机是%s牌子的，电池容量为%dmA,屏幕为%.2f寸，可待机%d小时，话费为%.2f，积分有%.2f分"
              %(self.__name,self.__sex,self.__age,self.__phonebrand,self.__battery,self.__screensize,self.__standbytime,self.__phonecharge,self.__scorecard))
    def sendMessage(self,message):
        print(message)

    def call(self,phonenumber,time):
        if phonenumber is None:
            print("您所拨打的电话是空号！")
        elif self.__phonecharge<1:
            print("您的话费已不足一元！")
        else:
            print("已拨通，正在通话中······")
            if time>0 and time<=10:
                self.__phonecharge -= time*1
                self.__scorecard += time*15
                return time*1
            elif time>10 and time<=20:
                self.__phonecharge -= time*0.8
                self.__scorecard += time*39
                return time*0.8
            else:
                self.__phonecharge -= time*0.65
                self.__scorecard += time*48
                return time*0.65

if __name__=="__main__":
    p = Person()
    p.setName("小杰")
    p.setSex("男")
    p.setAge(26)
    p.setPhoneCharge(20)
    p.setPhoneBrand("华为")
    p.setPhoneCharge(52.3)
    p.setBattery(2000)
    p.setStandByTime(24)
    p.setScreenSize(5.1)
    p.setScoreCard(1000.5)

    p.introduce()
    p.sendMessage("下班了，记得叫我。")
    charge=p.call(15103508184,20.5)
    print("通话结束，通话费用为%.2f"%charge)