'''
    主程序
'''
from menu import *
from bank import *

bank = Bank("localhost","root","123456","company")
menu = Menu()
while True:
    menu.print_welcome()
    chose = menu.inputHelp("选项")
    if menu.isExists(chose,menu.getBankChoice()):
        if chose  == "1":
            bank.addUser(menu)
        elif chose == "2":
            bank.saveMoney(menu)
        elif chose == "3":
            bank.takeMoney(menu)
        elif chose == "4":
            bank.transformMoney(menu)
        elif chose == "5":
            bank.selectUser(menu)
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")