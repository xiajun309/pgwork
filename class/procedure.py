import re
from mystr import mystr
from my_excel import my_excel

# ORACLE 存储过程类
class procedure:
    def __init__(self,str):
        self.str=str  # procedure 字符内容
        self.rows = self.str.split('\n')
        self.name = self.getName()
        self.tb_names = []

    #获得过程名
    def getName(self):
        res=None
        for r in self.rows:
            res=mystr(r).get_str_betweenAB('PROCEDURE', '(')
            if res !=None:
                return res
        return res
        # mystr1 = mystr("PROCEDURE HOME21(I NUMBER  DEFAULT  0 )  IS ---晚上9点cur_date_dd varchar2(2)")

    def get_tb_names(self):
        pass

    #获得过程中的所有表名

    #生成HIVE库 过程SQL


if __name__ == '__main__':
    my_excel1 = my_excel('../base_data/ora_pac.xlsx', 'PAG_XWH_WG_MON')
    title, content = my_excel1.get_date_toStr()
    # print(title,content)
    arrs=my_excel1.get_procedures(content)
    for i,val in enumerate(arrs):
        procedure1 = procedure(val)
        print(i,procedure1.name)
        if i==9:
            print('9--》',val)
        if i==10:
            print('10--》',val)
    # rows=procedure1.rows

    # print(rows)
    print(procedure1.name)
    # print(procedure1.str)