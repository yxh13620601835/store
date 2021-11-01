'''
    面向对象版的中国工商银行系统
    属性：账号、用户名、密码、国家、省份、街道、门牌号、余额、银行名称
    行为：开户、存钱、取钱、转账、查询、退出
'''
class Bank:
    __account=""
    __username=""
    __passwork=""
    __country=""
    __province=""
    __street=""
    __door=""
    __money=0.0
    __bankname="中国工商银行昌平支行"

    def addUser(self,username,password,country,province,street,door,money):
        pass
    def saveMoney(self,account,money):
        pass
    def takeMoney(self,account,password,money):
        pass
    def transformMoney(self,outaccount,inaccount,outpassword,outmoney):
        pass
    def selectUser(self,account,password):
        pass
    def quit(self):
        pass

if __name__=="__main__":
    pass