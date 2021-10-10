'''
    从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
    author:yxh
'''
list=[]
sum=0
for i in range(10):
    list.append(int(input("请输入第%d个数："%(i+1))))
max=list[0]
for i in range(10):
    sum+=list[i]
    if i!=0 and list[i]>=max:
        max=list[i]
average=sum/10
print("最大的数为：",max)
print("求和结果为：",sum)
print("平均数为：",average)