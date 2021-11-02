'''
    人：年龄，性别，姓名。
    现在有个工种，
    工人：年龄，性别，姓名 。
    行为：干活。请用继承的角度来实现该类。
    现在有学生这个工种，
    学生：年龄，性别，姓名，学号。
    行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''
class Person:
    __name=""
    __gender=""
    __age=0

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setGender(self,gender):
        if gender=="男" or gender=="女":
            self.__gender=gender
        else:
            print("输入非法！")
    def getGender(self):
        return self.__gender

    def setAge(self,age):
        if age<0 or age>150:
            print("输入非法！")
        else:
            self.__age=age
    def getAge(self):
        return self.__age

class Worker(Person):
    def work(self,work):
        print("%s的工作是%s"%(self.getName(),work))

class Student(Person):
    __stuno=""
    def setStuno(self,stuno):
        self.__stuno=stuno
    def getStuno(self):
        return self.__stuno
    def learn(self,project):
        print("%s的学号是%s，正在学习%s······"%(self.getName(),self.__stuno,project))
    def sing(self,song):
        print("%s的学号是%s，正在唱%s······"%(self.getName(),self.__stuno,song))

if __name__=="__main__":
    worker = Worker()
    worker.setName("二后生")
    worker.setAge(32)
    worker.setGender("男")
    print(worker.getAge())
    print(worker.getGender())
    worker.work("农民工")

    student = Student()
    student.setName("小华")
    student.setAge(18)
    student.setGender("女")
    student.setStuno("172055219")
    print(student.getAge())
    print(student.getGender())
    student.learn("化学")
    student.sing("小情歌")