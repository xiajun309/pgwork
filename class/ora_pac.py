from my_excel import my_excel
from mystr import mystr



class ora_pac:
    def __init__(self):
        pass

    def sql_o_to_pg(self,str):
        arrs=[]
        if isinstance(str, list)==True:
            arrs = str
        else :
            arrs = str.split('\n')
        #定义字典
        result=""
        dict_all = {}
        my_excel1 = my_excel('../base_data/ora_pac.xlsx', '字典')
        title, content=my_excel1.get_date_toDict()
        O_USER=content["O_USER"]
        O_TB = content["O_TB"]
        PG_USER = content["PG_USER"]
        PG_TB = content["PG_TB"]
        for i in range(len(O_TB)):
            # print(O_TB[i],PG_USER[i],PG_TB[i])
            if PG_USER[i] !=None  and  PG_TB[i] !=None :
                dict_all[O_TB[i]]=PG_USER[i]+"."+PG_TB[i]
                dict_all[O_USER[i]+"."+O_TB[i]]=PG_USER[i]+"."+PG_TB[i]
        print("--------------------dict_all---------------------------------------")
        print(dict_all)
        print("--------------------dict_all  end---------------------------------------")
        dict_tb= {}
        for  i,arr  in  enumerate(arrs):
            arr_new=self.sql_o_to_pg_row(arr,dict_tb,dict_all)
            result+=arr_new+'\n'
        return  result,dict_tb

    # 处理一行
    def sql_o_to_pg_row(self, arr ,dict_tb ={},dict_all={}):
        arr_new = ""
        str_tb = ""
        flag = False
        # 定义分隔指针
        vi = 0
        str_tb_start = -1
        str_tb_end = -1
        for j, s in enumerate(arr):
            # print("j,s  ",j,s)
            if flag == True:
                if s.strip() != "":
                    str_tb += s.strip()
                    if len(str_tb) == 1:
                        str_tb_start = j
                        str_tb_end = j
                    else:
                        str_tb_end += 1
                elif s.strip() == "":
                    if str_tb.strip() == "":
                        pass
                    elif str_tb != "" and len(str_tb) >= 1:
                        flag = False
                        if str_tb_end > str_tb_start and str_tb_start >= 0:
                            tmp_str = arr[str_tb_start:str_tb_end + 1]
                            if tmp_str[-1]==")":
                                try:
                                    dict_tb[tmp_str[0:-1].upper()] = dict_all[tmp_str[0:-1].upper()]
                                    tmp_str = dict_all[tmp_str[0:-1].upper()] + ")"
                                except:
                                    dict_tb[tmp_str.upper()] = ""
                            else :
                                try:
                                    dict_tb[tmp_str.upper()] = dict_all[tmp_str.upper()]
                                    tmp_str = dict_all[tmp_str.upper()]
                                except:
                                    dict_tb[tmp_str.upper()] = ""
                                    # 替换arr
                            arr_new += arr[vi:str_tb_start] + tmp_str + s
                            vi = str_tb_end + 1
                        # print("进来啦  flag ：", flag)
            elif flag == False:
                if j >= 3:
                    tmp_str = arr[j - 3] + arr[j - 2] + arr[j - 1] + arr[j]
                    if tmp_str.upper() == "FROM" and (j == 3 or (j >= 4 and arr[j - 4] == " ")):
                        flag = True

        # print(arr)
        arr_new += arr[vi:len(arr) + 1]
        return  arr_new





if __name__ == '__main__':
    str = my_excel.date_toStr('../base_data/ora_pac.xlsx', 'PAG_XWH_WG_MON')
    str+= my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XJ_SMALLMODULE')
    str+= my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XN_MARKETING_PAC')
    str+= my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XN_MARKETING_PAC_Eight')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'serv_mon_yyyymm_t')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'xn_backup')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'xj_jifei_check')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XJ')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'a_boss_serv_counrty')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XN_ZZ_PAC_ONE')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XN_ZQ_PAC_ONE')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XN_KPI')
    str += my_excel.date_toStr('../base_data/ora_pac.xlsx', 'XJ_OFFER')
    ora_pac1=ora_pac()
    result, dict_tb=ora_pac1.sql_o_to_pg(str)
    print("--------------------dict_tb---------------------------------------")
    print(dict_tb)
    print("--------------------dict_tb2---------------------------------------")
    for key  in dict_tb:
        if key[0:2].upper()!="XJ" and key[0:2].upper()!="LS" and key[0:1].upper()!="]" \
                and key[0:3].upper() != "XN_" and key[0:4].upper() != "HSP_" and key[0:3].upper() != "LC_" \
                and key[0:4].upper() != "XWH_" and key[0:4].upper() != "HSP_" and key[0:3].upper() != "LC_" \
                and key[0:5].upper() != "XNHEJ" and key[0:4].upper() != "LJP_"  and key[0:2].upper() != "T_" \
                and key[0:3].upper() != "UR_" and key[0:2].upper() != "S_" and key[0:2].upper() != "'|" \
                and key[0:2].upper() != "S0" and key[0:2].upper() != "S1" \
                and key[0:2].upper() != "S2" and key[0:2].upper() != "S3" :
            if dict_tb[key]==None or dict_tb[key]=="":
                print(key,dict_tb[key])

