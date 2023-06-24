# pip install openpyxl
import re

#获取EXCEL数据
def get_excel_date(path,sh):
    from openpyxl import load_workbook
    wb = load_workbook(path)
    sh1=wb[sh]
    content= {}
    title={}
    for i,row  in  enumerate(sh1.rows):
        if i==0 :
            for j,cell in enumerate(row):
                # content[cell.value]=[cell.value]
                content[cell.value] = []
                title[j]=cell.value
        else:
            for j,cell in enumerate(row):
                content[title[j]].append(cell.value)
    return title, content

def hive_to_pg(str):
    user =''
    user1=''
    tb_name =''
    hiveSql =''
    pgSql =''
    pgSql_chinese = ''
    # pg添加注解
    pg_comment =''
    arr1=str.split('\n')
    row=''
    rowi=0
    for i in range(len(arr1)):
        i_str=arr1[i].strip()
        # 首行 create ......
        if i_str[0:6]=='CREATE' and i_str[len(i_str)-1]=='(':
            #获取表的用户名
            try:
                user1 = re.search(r'\`(.+?)\.', i_str).group(0)
                user = user1[1:len(user) - 1]
            except:
                pass
            # 获取表名
            if re.search(r'\.(.+?)\`', i_str) !=None:
                tb_name = re.search(r'\.(.+?)\`', i_str).group(0)
            elif re.search(r'\`(.+?)\`', i_str) !=None:
                tb_name = re.search(r'\`(.+?)\`', i_str).group(0)
            tb_name = tb_name[1:len(tb_name) - 1]
            pgSql = '\n' +'drop  table if EXISTS   '+tb_name+';'
            pgSql += '\n' +i_str.replace(user1, '').replace("`", '')
            # pgSql_chinese=pgSql
        elif pgSql =='':
            pass
        # 添加列字段
        elif re.search(r'\`(.+?)COMMENT',i_str) !=None:
            tb_col, tb_colType, tb_colName=explain_col(i_str)
            if tb_col!=None and tb_colType!=None :
                pgSql +='\n' + tb_col+' '+tb_colType+','
                # 添加类注释  comment on column xttblog.id is '主键ID，自增';
                if tb_colName!=None:
                    pg_comment+='\n' +"comment on column "+tb_name+"."+tb_col+" is '"+tb_colName+"';"
        elif  re.search(r'\`(.+?)\`', i_str)!=None and i_str.strip().find(" string"):
            pgSql += '\n' + re.search(r'\`(.+?)\`', i_str).group().replace('`','') + ' ' + 'varchar,'


    pgSql+=');'
    pgSql=pgSql.replace(',)', ')').replace('string', 'varchar').replace('bigint', 'numeric').replace('int', 'integer')
    pgSql+=pg_comment
    print('user：',user,',tb_name：',tb_name,',hiveSql：',hiveSql)
    print('pgSql：',pgSql)
    return user,tb_name,pgSql

def ora_to_pg(str):
    print("进入ora_to_pg")
    newstring = ''.join([i for i in str if not i.isdigit()])
    newstring=newstring.split('\n')
    pgSql =''
    for i in range(len(newstring)):
        tmp_str=newstring[i].strip()
        tmp_str=tmp_str[0:-2]+','
        tmp_str=tmp_str.replace('()','')
        tmp_str=tmp_str.replace(' CHAR',' VARCHAR').replace('NUMBER','numeric')
        print(tmp_str)
        pgSql+=tmp_str


    # pgSql=pgSql.replace(',)', ')').replace('string', 'varchar').replace('bigint', 'numeric').replace('int', 'integer')
    return pgSql


#解释列    `subsname` string COMMENT '客户姓名',
def explain_col(str):
    tb_col=''
    tb_colType=''
    tb_colName=''
    tb_col=re.search(r'\`(.+?)\`', str).group(0).replace('`','')
    #列字段
    tb_colType=re.search(r'\`(.+?)COMMENT', str.strip()[2:])
    if tb_colType !=None:
        tb_colType=tb_colType.group(0).replace('`','').replace('COMMENT','').strip()
    #列字段类型
    tb_colName = re.search(r'\'(.+?)\',', str)
    if tb_colName!=None:
        tb_colName=tb_colName.group(0).replace('\'','').replace(',','')
    # print('tb_col', tb_col,'tb_colType', tb_colType,'tb_colName',tb_colName)
    return tb_col,tb_colType,tb_colName



#修改EXCEL数据
def update_excel_date(path,sh):
    title, content = get_excel_date(path,sh)
    print(title)
    print(content)
    hive_date=content['HIVE建表SQL'][0]
    user,tb_name,pgSql=hive_to_pg(hive_date)

def update_excel_date2(path,sh):
    title, content = get_excel_date(path,sh)
    print(title)
    print(content)
    ora_date=content['ora_sql'][3]
    pgSql=ora_to_pg(ora_date)


if __name__ == '__main__':
    update_excel_date('../base_data/我的HIVE表.xlsx', '汇总')
    # explain_col("`alarmtime` timestamp COMMENT '预警时间', ")
    # tb_col,tb_colType,tb_colName=explain_col(" `deal_date` string,  ")
    # print(tb_col,tb_colType,tb_colName)
    # update_excel_date2('../base_data/我的HIVE表.xlsx', 'ora_to_pg')
