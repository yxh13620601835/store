'''
    银行类
'''
from DBUtils import *
from  user import *
from address import *
import datetime

class Bank:

    __dbutils=None

    def __init__(self,host,user,password,database):
        self.__dbutils=DBUtils(host,user,password,database)

    # 通过账号获取账户信息
    def findByAccount(self,account):
        sql = "select * from user where account = %s"
        param = [account]
        data = self.__dbutils.select(sql, param)
        if len(data) != 0:
            return data
        return None

    # 银行的开户方法
    def bank_addUser(self,account,username,password,country,province,street,door,money,bank_name):

        # 查询是否已满
        sql = "select count(*) from user"
        param = []
        data = self.__dbutils.select(sql, param)
        if len(data) >= 100:
            return 3

        # 查询是否存在
        sql1 = "select * from user where username  = %s"
        param1 = [username]
        data1 = self.__dbutils.select(sql1, param1)
        if len(data1) != 0:
            return 2

        # 插入数据
        sql2 = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account, username, password, country, province, street, door, money, datetime.datetime.now(),
                  bank_name]
        self.__dbutils.update(sql2, param2)
        return 1

    # 银行的存钱方法
    def bank_saveMoney(self,ac, money):
        data = self.findByAccount(ac)
        if data != None and len(data) != 0:
            sql = "update user set money=money+%s where account = %s"
            param = [money, ac]
            self.__dbutils.update(sql, param)
            return True
        return False

    # 银行的查询功能
    def bank_selectUser(self,account, password,menu):
        data = self.findByAccount(account)
        if data != None and len(data) != 0:
            for i in range(len(data)):
                if password == data[i][2]:
                    print(menu.getMyinfo().format(account=data[i][0],
                                        username=data[i][1],
                                        password=data[i][2],
                                        country=data[i][3],
                                        province=data[i][4],
                                        street=data[i][5],
                                        door=data[i][6],
                                        money=data[i][7],
                                        bank_name=data[i][9]
                                        ))
                else:
                    print("用户密码错误！")
        else:
            print("该用户不存在！")

    # 银行的取钱功能
    def bank_takeMoney(self,account, password, money):
        data = self.findByAccount(account)
        if data != None and len(data) != 0:
            for i in range(len(data)):
                if password == data[i][2]:
                    if data[i][7] < money:
                        return 3
                    else:
                        sql = "update user set money=money-%s where account = %s"
                        param = [money, account]
                        self.__dbutils.update(sql, param)
                        return 0
            else:
                return 2
        else:
            return 1

    # 银行的转账功能
    def bank_transformMoney(self,outputaccount, inputaccount, outputpassword, outputmoney):
        outdata = self.findByAccount(outputaccount)
        indata = self.findByAccount(inputaccount)
        if outdata != None and len(outdata) != 0 and indata != None and len(indata) != 0:
            for i in range(len(outdata)):
                if outputpassword == outdata[i][2]:
                    if outdata[i][7] < outputmoney:
                        return 3
                    else:
                        sql = "update user set money=money-%s where account = %s "
                        param = [outputmoney, outputaccount]
                        self.__dbutils.update(sql, param)
                        sql1 = "update user set money=money+%s where account = %s"
                        param1 = [outputmoney, inputaccount]
                        self.__dbutils.update(sql1, param1)
                        return 0
                else:
                    return 2
        else:
            return 1

    # 开户方法
    def addUser(self,menu):
        user = User()
        address = Address()
        user.setUserName(menu.inputHelp("用户名"))
        user.setPassword(menu.inputHelp("密码"))
        address.setCountry(menu.inputHelp("居住地址：1.国家："))
        address.setProvince(menu.inputHelp("省份"))
        address.setStreet(menu.inputHelp("街道"))
        address.setDoor(menu.inputHelp("门牌号"))
        user.setMoney(menu.inputHelp("银行卡余额", "int"))

        # 调用银行的开户方法完成开户操作  返回 1 2 3
        status = self.bank_addUser(user.getAccount(), user.getUserName(),
                                   user.getPassword(), address.getCountry(),
                                   address.getProvince(), address.getStreet(),
                                   address.getDoor(), user.getMoney(),user.getBankName())
        # 判断1   2   3
        if status == 1:
            data = self.findByAccount(user.getAccount())
            if data != None and len(data) != 0:
                print("恭喜开户成功！以下是您的开户信息：")
                for i in range(len(data)):
                    print(menu.getMyinfo().format(account=data[i][0],
                                        username=data[i][1],
                                        password=data[i][2],
                                        country=data[i][3],
                                        province=data[i][4],
                                        street=data[i][5],
                                        door=data[i][6],
                                        money=data[i][7],
                                        bank_name=data[i][9]
                                        ))
        elif status == 2:
            print("该用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
        elif status == 3:
            print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

    # 存钱
    def saveMoney(self,menu):
        account = menu.inputHelp("账号")
        m = menu.inputHelp("存入的金额", "int")
        flag = self.bank_saveMoney(account, m)
        if flag:
            print("存储成功!您的个人信息为：")
            data = self.findByAccount(account)
            if data != None and len(data) != 0:
                for i in range(len(data)):
                    print(menu.getMyinfo().format(account=data[i][0],
                                        username=data[i][1],
                                        password=data[i][2],
                                        country=data[i][3],
                                        province=data[i][4],
                                        street=data[i][5],
                                        door=data[i][6],
                                        money=data[i][7],
                                        bank_name=data[i][9]
                                        ))
        else:
            print("对不起，您的个人信息不存在！请先开户后再次操作！")

    # 取钱
    def takeMoney(self,menu):
        account = menu.inputHelp("账户")
        password = menu.inputHelp("密码")
        tmoney = menu.inputHelp("取出金额", "int")

        f = self.bank_takeMoney(account, password, tmoney)

        if f == 1:
            print("该用户不存在！")
        elif f == 2:
            print("密码错误！")
        elif f == 3:
            print("取款金额不足！")
        elif f == 0:
            print("取款成功！")
            self.bank_selectUser(account, password,menu)

    # 转账功能
    def transformMoney(self,menu):
        output = menu.inputHelp("转出的账号")
        input = menu.inputHelp("转入的账号")
        outputpass = menu.inputHelp("转出的密码")
        outputmoney = menu.inputHelp("要转出的金额", "int")

        f = self.bank_transformMoney(output, input, outputpass, outputmoney)

        if f == 1:
            print("转出或转入的账号不存在！")
        elif f == 2:
            print("输入密码错误！")
        elif f == 3:
            print("转账金额不足！")
        elif f == 0:
            print("转账成功！")
            print("您的个人信息：")
            self.bank_selectUser(output, outputpass,menu)
        elif f == 4:
            print("转账失败！")

    # 查询账户方法
    def selectUser(self,menu):
        account = menu.inputHelp("账号")
        password = menu.inputHelp("密码")

        self.bank_selectUser(account, password,menu)