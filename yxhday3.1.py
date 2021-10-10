'''
    实现输入10个数字，并打印10个数的求和结果
    author:yxh
'''
sum=0
for i in range(1,11):
    sum+=int(input("请输入第%d个数："%i))
print("求和结果为：",sum)