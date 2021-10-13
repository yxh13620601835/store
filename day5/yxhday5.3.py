'''
    编写一个函数，传入一个列表，并统计每个数字出现的次数。
    返回字典数据：{21:3,56:9,10:3}
'''
def numcount(list=[]):
    result = {}
    for i in range(len(list)):
        result[list[i]] = list.count(list[i])
    return result

list = list(input("请输入数字"))
for i in range(len(list)):
    list[i] = int(list[i])

print(numcount(list))