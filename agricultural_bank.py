'''
    author:yxh
'''
import random

#农业银行库
agriculture_bank={}
bank_name="中国农业银行北京昌平沙河支行"
bank_choice={1:"开户",2:"存钱",3:"取钱",4:"转账",5:"查询",6:"Bye"}
account_type={
    1:{"max_transform_money":50000,"max_take_money":50000},
    2:{"max_transform_money":20000,"max_take_money":20000}
}
#用户信息
userInfo='''\033[1;33;44m
    ------------个人信息------------
    账号：%s
    账户类型：%s类账户
    姓名:%s
    密码：%s
    地址：
        国籍：%s
        省份：%s
        街道：%s
        门牌号：%s
    账户余额：%s￥
    开户行名称：%s
    -------------------------------
    \033[0m
'''
printInfo='''
    \033[1;33;44m
    ------------个人信息------------
    账号：%s
    账户类型：%s类账户
    账户余额：%s￥
    开户行名称：%s
    -------------------------------
    \033[0m
'''
selectInfo='''
    \033[1;33;44m
    ------------个人信息------------
    当前账号：%s
    密码：%s
    账户余额：%s￥
    用户居住地址：国家：%s 省份：%s 街道：%s 门牌号：%s
    开户行名称：%s
    -------------------------------
    \033[0m
'''
#菜单
def show_menu():
    menu='''
*****************************************
*          中国农业银行账户管理系统          *
*****************************************
*                 选项                   *'''
    choice='''*                {0}.{1}                  *'''
    end="*****************************************"
    print(menu)
    for i in bank_choice:
        print(choice.format(i,bank_choice[i]))
    print(end)

#判断是否存在账号
def findByAccount(account):
    for i in agriculture_bank:
        if agriculture_bank[i]["account"] == account:
            return i
    return False
#开户逻辑
def add_user():
    account = random.randint(10000000,99999999)
    accountType = int(input("请输入您的开户类型："))
    name = input("请输入您的姓名：")
    password = input("请输入6位密码：")
    print("请输入您的详细地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    money = int(input("请输入您的存款余额："))
    status=addUser(account,accountType,name,password,country,province,street,door,money)
    if status == 1:
        print(userInfo%(account,accountType,name,password,country,province,street,door,money,bank_name))
    elif status == 2:
        print("该账号已存在，请带证件去其他银行开户！")
    elif status == 3:
        print("该银行用户库已存满，请带证件去其他银行开户！")

def addUser(account,accountType,name,password,country,province,street,door,money):
    if len(agriculture_bank)>100:
        return 3
    else:
        flag = findByAccount(account)
        if flag == False:
            agriculture_bank[name] = {
                "account": account,
                "accountType": accountType,
                "password": password,
                "country": country,
                "province": province,
                "street": street,
                "door": door,
                "money": money,
                "bank_name": bank_name
            }
            return 1
        else:
            return 2

#存钱逻辑
def save_money():
    account = int(input("请输入您的账号："))
    money = int(input("请输入存入的金额："))
    status = saveMoney(account,money)
    if status == False:
        print("该账号不存在！")
    else:
        print(printInfo%(account,agriculture_bank[status]["accountType"],agriculture_bank[status]["money"],bank_name))

def saveMoney(account,money):
    name = findByAccount(account)
    if name==False:
        return False
    else:
        agriculture_bank[name]["money"] += money
        return name

#取钱逻辑
def take_money():
    account = int(input("请输入您的账号："))
    password = input("请输入您的账户密码：")
    money = int(input("请输入取出的金额："))
    name = findByAccount(account)
    status = takeMoney(name,password,money)
    if status == 0:
        print(printInfo%(account,agriculture_bank[name]["accountType"],agriculture_bank[name]["money"],bank_name))
    elif status == 1:
        print("该账号不存在！")
    elif status == 2:
        print("您输入的密码有误！")
    elif status == 3:
        if account_type[agriculture_bank[name]["accountType"]]["max_take_money"] < money:
            print("您超过了最大转出额度！")
        if agriculture_bank[name]["money"]<money:
            print("您的账户余额不足！")

def takeMoney(name,password,money):
    if name == False:
        return 1
    else:
        if agriculture_bank[name]["password"] == password:
            if account_type[agriculture_bank[name]["accountType"]]["max_take_money"] < money or agriculture_bank[name]["money"]<money:
                return 3
            else:
                agriculture_bank[name]["money"] -= money
                return 0
        else:
            return 2

#转账逻辑
def transform_money():
    account_out = int(input("请输入您的转出账号："))
    account_in = int(input("请输入您的转入账号："))
    password = input("请输入您的转出账户密码：")
    money = int(input("请输入转账的金额："))
    name_out = findByAccount(account_out)
    name_in = findByAccount(account_in)
    status = transformMoney(name_out,name_in,password,money)
    if status == 0:
        print(printInfo%(account_out,agriculture_bank[name_out]["accountType"],agriculture_bank[name_out]["money"],bank_name))
    elif status == 1:
        print("您输入的账号不存在！")
    elif status == 2:
        print("您输入的密码有误！")
    elif status == 3:
        if account_type[agriculture_bank[name_out]["accountType"]]["max_transform_money"] < money:
            print("您超过了最大转账额度！")
        if agriculture_bank[name_out]["money"] < money:
            print("您的账户余额不足！")

def transformMoney(name_out,name_in,password,money):
    if name_out == False or name_in == False:
        return 1
    else:
        if agriculture_bank[name_out]["password"] == password:
            if account_type[agriculture_bank[name_out]["accountType"]]["max_transform_money"] < money or agriculture_bank[name_out]["money"]<money:
                return 3
            else:
                agriculture_bank[name_out]["money"] -= money
                agriculture_bank[name_in]["money"] += money
                return 0
        else:
            return 2

#查询逻辑
def select_user():
    account = int(input("请输入您的账号："))
    password = input("请输入您的账号密码：")
    status = findByAccount(account)
    if status == False:
        print("该用户不存在！")
    else:
        if agriculture_bank[status]["password"] == password:
            print(selectInfo%(account,agriculture_bank[status]["password"],
                              agriculture_bank[status]["money"],
                              agriculture_bank[status]["country"],agriculture_bank[status]["province"],
                              agriculture_bank[status]["street"],agriculture_bank[status]["door"],bank_name))
        else:
            print("您输入的密码错误！")
#功能逻辑
while True:
    show_menu()
    index = input("请输入选项操作：")
    if index.isdigit():
        if index == '1':
            add_user()
        elif index == '2':
            save_money()
        elif index == '3':
            take_money()
        elif index == '4':
            transform_money()
        elif index == '5':
            select_user()
        elif index == '6':
            print("ByeBye!")
            break
        else:
            print("操作非法！")
    else:
        print("别瞎输入！")