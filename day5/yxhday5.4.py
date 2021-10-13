'''
    有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
    姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
'''
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
employee={}
for i in names:
        employee[i[0]]=dict({"年龄":i[1],
                             "性别":i[2],
                             "编号":i[3],
                             "任职公司":i[4],
                             "薪资":i[5],
                             "部门编号":i[6]})
print(employee)