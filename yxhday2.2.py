import math

r = float(input("请输入圆的半径："))
perimeter = 2*math.pi*r #圆的周长
print("圆的周长为：%.2f"%perimeter)
area = math.pi*(r**2) #圆的面积
print("圆的面积为：%.2f"%area)