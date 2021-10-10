'''
    实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
    author:yxh
'''
username="root"
password="admin"
usernameinput=input("请输入用户名：")
passwordinput=input("请输入密码：")
if username==usernameinput:
    if password==passwordinput:
        print("登录成功！")
    else:
        if password==input("请再次输入密码："):
            print("登录成功！")
        else:
            if password == input("请再次输入密码："):
                print("登录成功！")
            else:
                print("密码输错三次，系统已锁定！")
else:
    print("用户名错误！")