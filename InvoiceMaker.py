# pos project
# Invoice maker

import pymysql
import time, datetime

conn = pymysql.connect(host='45.119.147.76', user='root', password='201400867', db='hufPOS', charset='utf8')
curs = conn.cursor()

class Payinfo:
    def getdata(self):
        curs.execute("""SELECT * FROM t_payinfo """)
        conn.commit()
        all_table = curs.fetchall()
        return all_table

    def search_obj(self, Pnumb):
        try:
            curs.execute("""SELECT * FROM t_payinfo WHERE Pnumb = %s""", Pnumb)
            conn.commit()
            src_result = curs.fetchall()
            print(src_result)
            return src_result
        except :
            print('there is wrong data, try again')

    def get_pmenu(self, Pnumb):
        try:
            curs.execute("""SELECT Pmenu FROM t_payinfo WHERE Pnumb = %s""", Pnumb)
            conn.commit()
            src_result = curs.fetchall()
            print(src_result)
            return src_result
        except :
            print('there is wrong data, try again')

    def get_mns(self, MNcode):
        try:
            curs.execute("""SELECT MNname, MNprice FROM t_product WHERE MNcode = %s""", MNcode)
            conn.commit()
            src_result = curs.fetchall()
            print(src_result)
            return src_result
        except :
            print('there is wrong data, try again')

invo_notdone = True

while invo_notdone:
    this_member = Payinfo()
    show_table = this_member.getdata()
    print(show_table)
    print('영수증을 검색하시겠습니까? Y or N')

    command = input('type user command: ')

    if command == 'y' or command == 'Y':  # 2) find payinfo
        Pnumb = input('검색하고자 하는 주문번호를 입력하세요:')
        search_result = str(this_member.search_obj(Pnumb))
        search_result = search_result.strip('(,)')

        Pnumb = search_result.split(',')[0]

        ptime_slice = search_result.split('(')[1]
        ptime_list = ptime_slice.split('),')[0]
        ptime_list = ''.join(ptime_list)
        ptime_list_year = ''.join(ptime_list.split(',')[0])
        ptime_list_mon = ''.join(ptime_list.split(',')[1])
        ptime_list_day = ''.join(ptime_list.split(',')[2])
        ptime_list_hr = ''.join(ptime_list.split(',')[3])
        ptime_list_mn = ''.join(ptime_list.split(',')[4])
        Ptime = ptime_list_year+ ptime_list_mon + ptime_list_day + ptime_list_hr + ptime_list_mn

        pclass = ptime_slice.split('),')[1]
        pclass_list = pclass.strip(''' ',',"' ''')
        if pclass_list.count('카드'):
            Pclass_card = pclass_list.split(',')[0]
            P_card = int(Pclass_card.split(':')[1])
        else:
            P_card = 0
        if pclass_list.count('현금'):
            if P_card != 0:
                Pclass_cash = pclass_list.split(',')[1]
            else:
                Pclass_cash = pclass_list.split(',')[0]
            P_cash = int(Pclass_cash.split(':')[1])
        else:
            P_cash = 0
        pay_total = P_card + P_cash
        tax = int(pay_total*0.1)
        ohne_zoll = pay_total - tax

        pmenu_ls = str(this_member.get_pmenu(Pnumb))
        pmenu_ls =  pmenu_ls.strip('(("",),)')
        print(pmenu_ls)
        '''mns = pmenu_ls.split(',')
        for idx, val in enumerate(mns):
            if idx % 2 == 1:
                qt = []
                qt.append(val)
            else:
                mn = []
                val = val.strip("''")
                mn.append(val)
            print(qt, mn)'''

        #get_mns()
        #pmenu_qt = pmenu_mn.split(',')[1]
        #print(pmenu_qt)
        '''상품명과 단가는 t_product에서 가져오고 수량은 payinfo에서 금액은 단가*수량
        상품명 찾기:
        pmenu 리스트 각 요소의 앞쪽 두글자 앞에 M 을 붙여서 t_product 테이블에 검색 쿼리를 보내고
        받아온 정보를 이름, 단가로 변수별로 나눠서 저장한다.
        리스트 각 요소 , 뒤 숫자가 수량으로 저장되면 된다.
        금액은 단가 * 수량
        리스트로 만들어서 상품명 단가 수량 금액 \n 
        문자열로 만들려면 마지막에 ''.join()'''

        print(""""     
    영	    	    수		     증
       	동네카페 외대 본점
인터넷:www.dongne-cafe.onilne
주소: 서울시 동대문구 이문로 107
사업자: 201-81-20323 대표: dmkim
TEL: 02-2173-2216	FAX: 02-2173-0114
주문시간:""", Ptime, """
포스No:1	담당자:카페4조	    주문번호: """, Pnumb, """
--------------------------------------------
상품명		  단가         수량       금액
--------------------------------------------
""", pmenu_ls, """

--------------------------------------------
카드계						          """, P_card, """
현금계					              """, P_cash, """
총판매계			                  """, pay_total, """       
--------------------------------------------
과세상품금액				          """, ohne_zoll, """   
부가가치세				              """, tax, """    
--------------------------------------------
	Vielen Dank! Wiedersehen!
	
""")

    else:
        print('영수증 검색을 취소했습니다.')
        Invo_notdone = True