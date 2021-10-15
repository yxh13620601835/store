import random
print("***************************")
print("*   中国工商银行账户管理系统   *")
print("***************************")
print("*         1、开户          *")
print("*         2、存钱          *")
print("*         3、取钱          *")
print("*         4、转账          *")
print("*         5、查询          *")
print("*         6、再见          *")
print("***************************")

#1、开户逻辑
bank={}#空的银行账户数据库
bank_name="中国工商银行昌平分行"
#传入参数添加到字典里面
def bank_add(account,username,password,country,province,street,door):
    if username in bank:#说明用户已存在
        return 2
    elif len(bank)>=100:
        return 3
    else:
        bank[username]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
def useradd():
    account=random.randint(10000000,99999999)
    username=input("请输入您的用户名：")
    password=input("请输入您的用户密码：")
    print("下面请输入你的详细地址")
    country=input("\t\t请输入您的国家：")
    province=input("\t\t请输入您的省份：")
    street=input("\t\t请输入您的街道：")
    door=input("\t\t请输入您的门牌号：")
    add=bank_add(account,username,password,country,province,street,door)
    if add == 3:
        print("数据库已满请到其他银行开户!")
    elif add ==2:
        print("请输入其他用户名！")
    elif add== 1:
        print("开户成功,下面是你的详细信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
#2、存钱
def save_money():
    username=input("请输入您的用户名：")
    money = int(input("请输入存入的金额："))
    save = savemoney(username,money)
    if save == False:
        print("您输入的用户名不存在！")
    else:
        print("存入成功！")
        info = '''
                    ------------用户信息------------
                    用户名:%s
                    账号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, bank[username]["account"], bank[username]["money"], bank_name))

def savemoney(username,money):
    if username in bank:
        bank[username]["money"] = money
    else:
        return False

#3、取钱
def draw_money():
    username = input("请输入您的用户名：")
    password = input("请输入您的用户密码：")
    money = int(input("请输入取出的金额："))
    draw = drawmoney(username,password,money)
    if draw == 0:
        print("取出成功！")
        info = '''
                    ------------用户信息------------
                    用户名:%s
                    账号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, bank[username]["account"], bank[username]["money"], bank_name))
    elif draw == 1:
        print("您输入的用户不存在！")
    elif draw == 2:
        print("您输入的用户密码错误！")
    elif draw == 3:
        print("您的账户余额不足！")

def drawmoney(username,password,money):
    if username in bank:
        if bank[username]["password"] == password:
            if bank[username]["money"]>=money:
                bank[username]["money"] -= money
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1
#4、转账
def transfer_accounts():
    username_out = input("请输入您的用户名：")
    username_in = input("请输入您要转入账户的用户名：")
    password_out = input("请输入您的用户密码：")
    money = int(input("请输入转账的金额："))
    transfer = transferaccounts(username_out,username_in,password_out,money)
    if transfer==0:
        print("转账成功！")
        info = '''
                    ------------用户信息------------
                    用户名:%s
                    账号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username_out, bank[username_out]["account"], bank[username_out]["money"], bank_name))
    elif transfer == 1:
        print("您输入的用户名有误！")
    elif transfer == 2:
        print("您输入的用户密码错误！")
    elif transfer == 3:
        print("您的账户余额不足！")
def transferaccounts(username_out,username_in,password_out,money):
    if username_out in bank and username_in in bank:
        if bank[username_out]["password"]==password_out:
            if bank[username_out]["money"]>=money:
                bank[username_out]["money"] -= money
                bank[username_in]["money"] += money
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1
#5、查询
def query_user():
    username = input("请输入您的用户名：")
    password = input("请输入您的用户密码：")
    queryuser(username,password)
def queryuser(username,password):
    if username in bank:
        if bank[username]["password"] == password:
            info = '''
                        ------------用户信息------------
                        用户名:%s
                        当前账号：%s
                        余额：%s
                        用户居住地址：%s%s省%s%s 
                        开户行名称：%s
                    '''
            # 每个元素都可传入%
            print(info % (username, bank[username]["account"], bank[username]["money"], bank[username]["country"],bank[username]["province"],bank[username]["street"],bank[username]["door"],bank_name))
        else:
            print("您输入的用户密码有误！")
    else:
        print("该用户不存在！")
while True:
    index=int(input("请输入您的操作："))
    if index ==1:
        print("1、开户")
        useradd()
    elif index ==2:
        print("2、存钱")
        save_money()
    elif index ==3:
        print("3、取钱")
        draw_money()
    elif index ==4:
        print("4、转账")
        transfer_accounts()
    elif index ==5:
        print("5、查询")
        query_user()
    elif index ==6:
        print("再见！")
        break
    else:
        print("输入非法！")
