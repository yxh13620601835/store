import  xlrd
from DBUtils import *

wb = xlrd.open_workbook(r"2020年每个月的销售情况.xlsx",encoding_override=True)
for i in range(12):
    st = wb.sheet_by_index(i)
    sql = "create table %s月 (日期 varchar(5) primary key," \
          "服装名称 varchar(15)," \
          "单价 float," \
          "本月库存数量 int," \
          "销售量 int)"
    param = [int(i+1)]
    # sql = "drop table %s月"
    update(sql,param)
    rows = st.nrows
    cols = st.ncols
    for j in range(1,rows):
        data = st.row_values(j)
        sql1 = "insert into %s月 value(%s,%s,%s,%s,%s)"
        param1 = [int(i+1),data[0],data[1],data[2],data[3],data[4]]
        update(sql1,param1)
