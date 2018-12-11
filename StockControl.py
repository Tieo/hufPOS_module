# pos project module 03
# Stock system: Controller
import pymysql
from Control import *


conn = pymysql.connect(host='45.119.147.76', user='root', password='201400867', db='hufPOS', charset='utf8')
curs = conn.cursor()

class StockCtrl(Control):
    '''def __init__(self,Scode, Sname, Sstock, Sprice):
        self.scode = Scode
        self.sname = Sname
        self.sstock= Sstock
        self.sprice = Sprice'''

    def set_obj(self, Scode, Sname, Sstock, Sprice):
        try:
            curs.execute("""INSERT INTO t_stock (Scode, Sname, Sstock, Sprice)
                VALUES (%s, %s, %s, %s)""",
                     (Scode, Sname, Sstock, Sprice))
            conn.commit()
            print(curs.lastrowid)
        except:
            print('there is wrong data, try again')

    def search_obj(self, Sname):
        try:
            print(Sname)
            asterisk = '*'
            search_sql = ("""SELCECT %s FROM t_stock WHERE Sname = %s""", (asterisk, Sname))
            print(search_sql, Sname)
            #curs.execute(search_sql, Sname)
            curs.execute("""SELECT * FROM t_stock WHERE Sname = %s""", Sname)
            print(1)
            conn.commit()
            src_result = curs.fetchall()
            print(src_result)
            return (src_result)
        except:
            print('there is wrong data, try again')


    def update_obj(self, Sname, Sstock):
        try:
            curs.execute("""UPDATE t_product SET Sstock = %s WHERE Sname = %s""",
                      (Sstock,Sname))
            conn.commit()
            print(curs.lastrowid)
        except:
            print('there is wrong data, try again')

    def del_obj(self, Sname):
        try:
            curs.execute("""DELETE FROM t_stock WHERE Sname = %s""",
                         (Sname))
            conn.commit()
            print(curs.lastrowid)
        except:
            print('there is wrong data, try again')


