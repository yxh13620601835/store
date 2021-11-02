'''
    数据库工具类
'''
import pymysql

class DBUtils:
    __host = "localhost"
    __user = "root"
    __password = "123456"
    __database = "company"

    def __init__(self,host,user,password,database):
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database

    def update(self,sql, param):
        con = pymysql.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database, charset='utf8')
        cur = con.cursor()
        cur.execute(sql, param)
        con.commit()
        cur.close()
        con.close()

    def select(self,sql, param, mode="all", size=1):
        con = pymysql.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database, charset="utf8")
        cur = con.cursor()
        cur.execute(sql, param)
        if mode == "all":
            return cur.fetchall()
        elif mode == "one":
            return cur.fetchone()
        elif mode == "many":
            return cur.fetchmany(size)
        cur.close()
        con.close()