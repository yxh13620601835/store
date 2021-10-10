'''
    一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，
    晚上下滑2米，问第几天能出来？请编程求出。
    author:yxh
'''
well_height=20
height=0
day=1
while height<well_height:
    height +=3
    if height>=well_height:
        break
    else:
        height = height-2
        day +=1
print("第%d天能出来"%day)

