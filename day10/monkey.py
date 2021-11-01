'''
    猴子类：
    属性：类别，性别，身体颜色，体重。
    行为：造火（要求传入造火的材料：比如木棍还是石头），
        学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
'''
class Monkey:
    __type=""
    __gender=""
    __color=""
    __weight=0.0

    def setType(self,type):
        self.__type=type
    def getType(self):
        return self.__type

    def setGender(self,gender):
        if gender=="母" or gender=="公":
            self.__gender=gender
        else:
            print("输入非法！")
    def getGender(self):
        return self.__gender

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        if weight<0 or weight >1000:
            print("输入非法！")
        else:
            self.__weight=weight
    def getWeight(self):
        return self.__weight

    def introduce(self):
        print("%s的%s颜色是%s，体重%.2f公斤"%(self.__gender,self.__type,self.__color,self.__weight))

    def makeFire(self,material):
        print("%s用%s造火"%(self.__type,material))

    def learn(self,*things):
        print(self.__type,"要学习的内容有：",end="")
        for i in things:
            print(i,end=" ")

if __name__=="__main__":
    monkey = Monkey()
    monkey.setType("金丝猴")
    monkey.setGender("母")
    monkey.setColor("金色")
    monkey.setWeight(50.3)
    monkey.introduce()
    monkey.makeFire("木棒")
    monkey.learn("吃饭","喝水","玩耍","察言观色")