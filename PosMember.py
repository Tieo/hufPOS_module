# pos project module 03
# Stock system

import pymysql
from MemberControl import MemberCtrl

conn = pymysql.connect(host='45.119.147.76', user='root', password='201400867', db='hufPOS', charset='utf8')
curs = conn.cursor()
##########

MemberController = MemberCtrl
memberCtrl = MemberController()

class Memberinfo:
    def getdata(self):
        curs.execute("""SELECT * FROM t_member """)
        conn.commit()
        all_table = curs.fetchall()
        return all_table

   # def cal_netsales(self):
##########

# main
membernotdone = True


while membernotdone:
    command = ''
    addp = ''
    this_member = Memberinfo()
    show_table = this_member.getdata()
    '''for idx_i, val_i in enumerate(show_table):
        for idx_j, val_j in enumerate(val_i):
            print (val_j)'''
    print (show_table)
    print('select function')
    print('1) add Member into a Membertable')
    print('2) find Member')
    print('3) update Member')
    print('4) delete Member')
    command = input('type user command: ')

    if command == '1': # 1) add Stock into a Stocktable
        Scode, Sname, Sstock, Sprice = map(str, input('다음을 차례로 입력하세요: 재고번호, 재고이름, 재고수량, 재고가격\n:::').split())
        Scode = Scode.strip(',')
        Sname = Sname.strip(',')
        Sstock = Sstock.strip(',')
        stockCtrl.set_obj(Scode, Sname, Sstock, Sprice)
        set_result = curs.execute("""SHOW FULL COLUMNS FROM t_product """)
        print('the added stock is:', set_result)
        print('\n\n\n')

    elif command == '2': # 2) find Stock
        Sname = input('검색하고자 하는 재고 이름을 입력하세요:')
        print(Sname)
        Sname = Sname.strip('')
        search_result = stockCtrl.search_obj(Sname)
        print('검색결과:', search_result)
        print('\n\n\n')

    elif command == '3': # 3) update Stock
        Sname, Sstock = map(str,input('수정하고자 하는 재고 이름, 수량을 입력하세요:').split())
        Sname = Sname.strip(',')
        Sstock = int(Sstock)
        stockCtrl.update_obj(Sname, Sstock)
        update_result = stockCtrl.search_obj(Sname)
        print('수정결과: %s', update_result)
        print('\n\n\n')

    elif command == '4': # 4) delete Stock
        Sname= input('삭제하고자 하는 재고 이름을 입력하세요:')
        stockCtrl.del_obj(Sname)
        del_result = stockCtrl.search_obj(Sname)
        print('삭제결과: %s', del_result)
        print('\n\n\n')

    else:
        print('unexpected command is detected')
        break

exit(1) #error exit
conn.close()

