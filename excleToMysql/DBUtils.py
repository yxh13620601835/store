import pymysql

host="localhost"
user="root"
password="123456"
database="company"

def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cur = con.cursor()

    cur.execute(sql,param)
    con.commit()
    cur.close()
    con.close()


def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()

    cur.execute(sql, param)
    if mode == "all":
        return cur.fetchall()
    elif mode=="one":
        return cur.fetchone()
    elif mode=="many":
        return cur.fetchmany(size)
    con.commit()
    cur.close()
    con.close()
