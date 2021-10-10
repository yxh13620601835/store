'''
    有以下两个数，使用+，-号实现两个数的调换。
    A=56
    B=78
    实现效果：
    A=78
    B=56
    author:yxh
'''
a=56
b=78
print("A=%d B=%d"%(a,b))
flag = input("请输入操作符：")
if flag=="+" or flag=="-":
    temp=a
    a=b
    b=temp
    print("A=%d B=%d" % (a, b))
else:
    print("输入非法！")
