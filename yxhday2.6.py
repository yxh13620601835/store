import math
a = int(input("请输入第一条边的长度："))
b = int(input("请输入第二条边的长度："))
c = int(input("请输入第三条边的长度："))

if a+b>c and b+c>a and c+a>b:
    perimeter = a+b+c #周长
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("该三角形的周长为%d,该三角形的面积为%d"%(perimeter,area))
else:
    print("构不成三角形！！")