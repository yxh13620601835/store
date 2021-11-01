'''
    i.	定义了一个学生类：
    属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
    行为：学习（要求参数传入学习的时间），
        玩游戏（要求参数传入游戏名），
        编程（要求参数传入写代码的行数），
        数的求和（要求参数用变长参数来做，返回求和结果）
'''
class Student:
    __stuno=""
    __name=""
    __age=0
    __sex=""
    __height=0.0
    __weight=0.0
    __grade=0.0
    __address=""
    __phone=""
    def setStuNo(self,stuno):
        self.__stuno=stuno
    def getStuNo(self):
        return self.__stuno

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        if age<0 or age>150:
            print("输入非法！")
        else:
            self.__age=age
    def getAge(self):
        return self.__age

    def setSex(self,sex):
        if sex == "男" or sex=="女":
            self.__sex=sex
        else:
            print("输入非法！")
    def getSex(self):
        return self.__sex

    def setHeight(self,height):
        if height<0 or height>300:
            print("输入非法！")
        else:
            self.__height=height
    def getHeight(self):
        return self.__height

    def setWeight(self,weight):
        if weight<0 or weight>1000:
            print("输入非法！")
        else:
            self.__weight=weight
    def getWeight(self):
        return self.__weight

    def setGrade(self,grade):
        if grade<0 or grade>100:
            print("输入非法！")
        else:
            self.__grade=grade
    def getGrade(self):
        return self.__grade

    def setAddress(self,address):
        self.__address=address
    def getAddress(self):
        return self.__address

    def setPhone(self,phone):
        if phone is None:
            print("输入非法！")
        else:
            self.__phone=phone
    def getPhone(self):
        return self.__phone

    def learn(self,time):
        print("学习%.2f个小时"%time)

    def game(self,game):
        print("玩一局%s游戏！"%game)

    def program(self,rows):
        print("需要写%d行代码······"%rows)

    def sum(self,*grade):
        sum = 0.0
        if len(grade)==0:
            return sum
        for i in grade:
            sum += i
        return sum
    def introduce(self):
        print("%s的学号是%s，年龄是%d，性别是%s，身高为%.2fcm，体重%.2f斤，成绩是%.2f分，家庭地址是%s，电话号码是%s"
              %(self.__name,self.__stuno,self.__age,self.__sex,self.__height,self.__weight,self.__grade,self.__address,self.__phone))

if __name__=="__main__":
    stu = Student()
    stu.setStuNo("172055219")
    stu.setName("小华")
    stu.setAge(25)
    stu.setSex("女")
    stu.setHeight(153.4)
    stu.setWeight(100.1)
    stu.setGrade(99.5)
    stu.setAddress("山西省太原市尖草坪区")
    stu.setPhone("151035081840")
    stu.introduce()
    stu.learn(2.3)
    stu.game("王者荣耀")
    stu.program(150)
    print(stu.sum(1, 2, 3, 4, 5, 6, 7, 8, 9))