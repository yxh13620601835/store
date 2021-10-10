'''
  1.随机点名
  2.随机生成处罚遍数
    技术选型：
        容器类型：int str double boolean
            元组：(1,5,7,4)  不允许做任何修改
            列表：[1,5,7,8,10,41]  可以做任何操作
            字典:{}
    列表的几个方式：
        append()
        remove  pop(index)
        直接赋值
        直接打印即可
        len()取长度
优化代码：循环 键盘输入一个数字，判断为1那么生成人名，判断为2 那么生成遍数 判断为q or Q 退出
'''
import random
list=["吴承恩","汉弗莱","刘醒","兰尼斯特","流星花园","舒克","汉弗莱1"]
while True:
    keycode = input("请用户输入：")
    if keycode=='q' or keycode=='Q':
        break
    elif keycode=='1':
        name=random.randint(0,len(list)-1)
        print("人名为：",list[name])
    elif keycode=='2':
        count=random.randint(0,100)
        print("处罚了%d遍"%count)
    else:
        print("输入非法，请重新输入！")