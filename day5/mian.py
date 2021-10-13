'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
import  random
#商品
shop=[
#     0      1
    ["刀🔪",999],#0
    ["斧子",200],#1
    ["👍",90000],#2
    ["coco",150],#3
    ["枸杞",900],#4
]
#初始化余额
money=random.randint(0,99999)
print(money)
#购物车
mycart=[]
#展示商品
#消费总计
allcost = 0
while True:
    for index,value in enumerate(shop):
        print(index,":",value)
    chose=input("请输入商品编号")
    if chose.isdigit():#str判断引号内是否为数字
        chose=int(chose)#转换成整型
        if chose <len(shop):#判断输入的内容是否小于列表的长度
            if money>shop[chose][1]:#判断money是否大于商品的价格
                mycart.append(shop[chose])#把商品加入购物车
                coupon=random.randint(1, 10)#获取单个商品优惠券
                cost = 0
                if coupon==1:
                    print(shop[chose][0],"抽到免单优惠券！")
                    cost=0
                elif coupon==2:
                    print(shop[chose][0],"抽到1折优惠券！")
                    cost=shop[chose][1]*0.1
                elif coupon==5:
                    print(shop[chose][0],"抽到5折优惠券！")
                    cost=shop[chose][1] * 0.5
                elif coupon==10:
                    print(shop[chose][0],"抽到9折优惠券！")
                    cost=shop[chose][1] * 0.9
                else:
                    print(shop[chose][0],"没有抽到优惠券！")
                    cost=shop[chose][1]
                money = money - cost
                allcost += cost
                print("恭喜你成功加入购物车，您的余额为：",money,shop[chose][0],"花费了",cost)
            else:
                print("gun")
        else:
            print("没有此商品")
    elif chose=="q"or chose=="Q":
        print("=================")
        for index, value in enumerate(mycart):
            print(index, ":", value)
        allcoupon = random.randint(1, 10)  # 获取购物车优惠券
        savemoney = 0
        if allcoupon == 1:
            print("购物车抽到免单优惠券！")
            savemoney = allcost
        elif allcoupon == 2:
            print("购物车抽到1折优惠券！")
            savemoney =allcost * (1-0.1)
        elif allcoupon == 5:
            print("购物车抽到5折优惠券！")
            savemoney = allcost * (1-0.5)
        elif allcoupon == 10:
            print("购物车抽到9折优惠券！")
            savemoney = allcost * (1-0.9)
        else:
            print("购物车没有抽到优惠券！")
        allcost -=savemoney
        print("您的消费总计为：%.1f"%allcost)
        money += savemoney
        print("您的余额为：%.1f"%money)
        break
    else:
        print("别瞎弄")
