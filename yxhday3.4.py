'''
    从键盘输入任意三边，判断是否能形成三角形，若可以，
    则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
    author:yxh
'''
list=input("请输入三条边的数值：").split(" ")
list1=[]
for i in range(len(list)):
    list1.append(int(list[i]))
print(list1)
a=list1[0]
b=list1[1]
c=list1[2]
if a+b>c and b+c>a and c+a>b:
    if a==b or b==c or c==a:
        if a==b and b==c and c==a:
            print("是等边三角形！")
        else:
            print("是等腰三角形！")
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
        print("是直角三角形！")
    else:
        print("是普通三角形！")
else:
    print("不能构成三角形！")
