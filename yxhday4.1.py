'''
    1.统计每个人的平均薪资
    2.统计每个人的平均年龄
    3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
    4.统计公司男女人数
    5.每个部门的人数
    author:yxh
'''
names = [
            ["曹操","56","男","106","IBM", 500 ,"50"],
            ["大乔","19","女","230","微软", 501 ,"60"],
            ["小乔", "19", "女", "210", "Oracle", 600, "60"],
            ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
        ]
#1.统计每个人的平均薪资
allsalary = 0
for i in names:
    allsalary += i[5]
avgsalary = allsalary / len(names)
print("每个人的平均工资为：",avgsalary)
#2.统计每个人的平均年龄
allage = 0
for i in names:
    allage += int(i[1])
avgage = allage / len(names)
print("每个人的平均年龄为：",avgage)
#3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
names.append(["刘备","45","男","220","alibaba",500,"30"])
print(names)
#统计公司男女人数
malenum=0
femalenum=0
for i in names:
    if i[2]=="女":
        femalenum +=1
    elif i[2]=="男":
        malenum +=1
print("公司男性人数为：",malenum)
print("公司女性人数为：",femalenum)
#每个部门的人数
dict={}
for i in range(len(names)):
    if names[i][-1]not in dict:
        dict[names[i][-1]] = 1
    else:
        dict[names[i][-1]] += 1
for i in dict:
    print("%s部门的人数为%d"%(i,dict[i]))