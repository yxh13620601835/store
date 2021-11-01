'''
    定义一个学生类和对应的测试类
    1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
    2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：“大家好，我叫xxx，今年xxx岁了！”
    3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的学生的年龄大，则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“我比同桌小xxx岁！”；如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
    4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
    5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
    6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；
'''
class Student:
    __name=""
    __age=0

    def setName(self,name):
        if name.isdigit():
            print("输入非法")
        else:
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

    def introduce(self):
        print("大家好，我叫%s，今年%d岁了！"%(self.__name,self.__age))

    def compareAge(self,person):
        if self.__age>person.getAge():
            return "我比同桌大"+str(self.__age-person.getAge())+"岁！"
        elif self.__age==person.getAge():
            return "我和同桌一样大！"
        else:
            return "我比同桌小"+str(person.getAge()-self.__age)+"岁！"
class TestStudent:
    def __init__(self):
        self.student1 = Student()
        self.student1.setName("笑笑")
        self.student1.setAge(18)
        self.student2 = Student()
        self.student2.setName("美美")
        self.student2.setAge(16)
if __name__ =="__main__":
    test = TestStudent()
    test.student1.introduce()
    data=test.student1.compareAge(test.student2)
    print(data)