'''
    全年的销售总额
    每种衣服的销售（件数）占比
    每种衣服的月销售（件数）占比
    每种衣服的销售额占比

    最畅销的衣服是那种
    每个季度最畅销的衣服
    全年销量最低的衣服

'''
#导入xlrd
import xlrd

#打开工作簿
wd = xlrd.open_workbook(r"E:\pythonprogram\testcase\day7\2020年每个月的销售情况.xlsx",encoding_override=True)

#全年的销售额和销售量
allSales=0
allnum = 0
#每种衣服全年的销售量和销售额
all_clothes_num={}
all_clothes_sales={}
#每月每种衣服的销售量和销售额
month_clothes_num={}
quarter_clothes_num={"春季":{},"夏季":{},"秋季":{},"冬季":{}}

def creatdict(key,dict,data):
    if key in dict:
        dict[key] += data
    else:
        dict[key] = data

#打开选项卡
for i in range(12):
    st = wd.sheet_by_index(i)
    #获取行数，列数
    rows = st.nrows
    cols = st.ncols
    #横向获取数据
    monthnum = 0
    month_clothes_num[i]={}
    for j in range(1,rows):
        data = st.row_values(j)
        allSales += data[2]*data[4]
        allnum += data[4]
        creatdict(data[1],all_clothes_num,data[4])
        creatdict(data[1], all_clothes_sales, data[2]*data[4])
        creatdict(data[1], month_clothes_num[i], data[4])
        if i == 0 or i == 10 or i == 11:
            if data[1] in quarter_clothes_num["冬季"]:
                quarter_clothes_num["冬季"][data[1]] += data[4]
            else:
                quarter_clothes_num["冬季"][data[1]] = data[4]
        elif i == 1 or i==2 or i==3:
            if data[1] in quarter_clothes_num["春季"]:
                quarter_clothes_num["春季"][data[1]] += data[4]
            else:
                quarter_clothes_num["春季"][data[1]] = data[4]
        elif i== 4 or i==5 or i==6:
            if data[1] in quarter_clothes_num["夏季"]:
                quarter_clothes_num["夏季"][data[1]] += data[4]
            else:
                quarter_clothes_num["夏季"][data[1]] = data[4]
        elif i == 7 or i == 8 or i == 9:
            if data[1] in quarter_clothes_num["秋季"]:
                quarter_clothes_num["秋季"][data[1]] += data[4]
            else:
                quarter_clothes_num["秋季"][data[1]] = data[4]

    monthnum = allnum
    month_clothes_num[i]["总销售量"] = monthnum



#全年的销售总额
print("全年销售额为：%.2f"%allSales)
print("------------------------------------")
#每种衣服的销售（件数）占比
for key in all_clothes_num:
    print("%s的销售占比为(百分比)：%.2f "%(key,all_clothes_num[key]/allnum*100))
print("------------------------------------")
#每种衣服的月销售（件数）占比
for month in month_clothes_num:
    for name in month_clothes_num[month]:
        if name != "总销售量":
            print("%s的%s月销售占比为(百分比)：%.2f " % (name,month+1,month_clothes_num[month][name]/month_clothes_num[month]["总销售量"]*100))
print("------------------------------------")
#每种衣服的销售额占比
for key in all_clothes_sales:
    print("%s的销售额占比为(百分比)：%.2f "%(key,all_clothes_sales[key]/allSales*100))
print("------------------------------------")
#最畅销的衣服是那种
#全年销量最低的衣服
maxnum = all_clothes_num["羽绒服"]
minnum = all_clothes_num["羽绒服"]
for key in all_clothes_num:
    if all_clothes_num[key]>maxnum:
        maxnum = all_clothes_num[key]
        maxname = key
for key in all_clothes_num:
    if all_clothes_num[key]<minnum:
        minnum = all_clothes_num[key]
        minname = key
print("最畅销的衣服是：",maxname)
print("全年销量最低的衣服是：",minname)
print("------------------------------------")
#每个季度最畅销的衣服
for i in quarter_clothes_num:
    maxquarternum = quarter_clothes_num[i]["羽绒服"]
    for j in quarter_clothes_num[i]:
        if quarter_clothes_num[i][j]> maxquarternum:
            maxquarternum = quarter_clothes_num[i][j]
            maxquartername = j
    print("%s季度最畅销的衣服是：%s"%(i,maxquartername))
