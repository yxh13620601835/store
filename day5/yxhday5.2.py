'''
    小明，小刚去超市里购买水果
    小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
    以姓名做key，value仍然是字典
'''
friuts = {
	"苹果":12.3,  # 水果和单价
	"草莓":4.5,
    "香蕉":6.3,
    "葡萄":5.8,
    "橘子":6.4,
    "樱桃":15.8
}
info = {
    '小明':{
        'fruits': {'苹果':4, '草莓':13, '香蕉':10}
    },
    '小刚':{
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30}
    }
}
str1 = 'money'
for k1 in info:
    for k2 in info[k1]:
        money = 0
        for k3 in info[k1][k2]:
            money += friuts[k3]*info[k1][k2][k3]
        info[k1][k2][str1] = money
print(info)

