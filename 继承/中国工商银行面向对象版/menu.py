'''
    界面类
'''

class Menu:

    __bank_choice = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye"}  # 银行业务选项
    # 开户成功的信息模板
    __myinfo = '''
        \033[0;32;40m
        ------------账户信息------------
        账号：{account}
        姓名：{username}
        密码：{password}
        地址：
            国家：{country}
            省份：{province}
            街道：{street}
            门牌号：{door}
        账户余额：{money}
        注册银行名：{bank_name}
        -------------------------------
        \033[0m
    '''
    # 欢迎模板
    __welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

    __welcome_item = '''*              {0}.{1}             *'''

    def getBankChoice(self):
        return self.__bank_choice
    def getMyinfo(self):
        return self.__myinfo

    def print_welcome(self):
        print(self.__welcome, end="")
        keys = self.__bank_choice.keys()
        for i in keys:
            print(self.__welcome_item.format(i, self.__bank_choice[i]))
        print("**********************************")

    # 输入帮助方法：chose是打印选项
    def inputHelp(self,chose, datatype="str"):
        while True:
            print("请输入", chose, ":")
            i = input(">>>:")
            if len(i) == 0:
                print("该项不能为空！请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i

    # 判断是否存在该银行选项
    def isExists(self,chose, data):
        if chose in data:
            return True
        return False