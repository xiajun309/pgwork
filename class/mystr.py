import re
# CREATE TABLE `hbgz_yf2_sjgx.KF_BAS_PROBLEMPROCESS_DAY_1008`(

class mystr:
    def __init__(self,str):
        self.str=str
        self.len=len(str)


    def get_CnPlugin(self, str, n=5):
        arrs = str.split('\n')
        result = "\n" + "("
        print(arrs)
        for i, val in enumerate(arrs):
            if val.strip() != None and val.strip() != '':
                result += "'" + val.strip() + "',"
                if i % n == 0:
                    result += "\n"
        result += ")"
        result = result.replace(",)", ")")
        print(result)
    # 查找一个字符Next位置
    def getNextIndex(self,s:str):
        result=None
        l=len(s)
        try:
            result=self.str.index(s)
            result+=l
        except:
            pass
        return result

    # 查找一个字符上一个位置
    def getPreIndex(self,s:str):
        result=None
        try:
            result=self.str.index(s)
        except:
            pass
        return result

    # 获取2个字符之间的字符串
    def get_str_betweenAB(self,A,B):
        # String pat = "(?<=\\@\\$\\{)(.+?)(?=\\})";
        result=None
        index1 = self.getNextIndex(A)
        # get_index(A)
        index2 = self.getPreIndex(B)
        if index1!=None and index2!=None :
            result=self.str[index1:index2]
        return  result

    # 找一个字符串中所有表表名
    def get_tableName(self,str):
        v=""
        for i in range(len(str)):
            pass
        print(str)




if __name__ == '__main__':
    mystr1=mystr("PROCEDURE HOME21(I NUMBER  DEFAULT  0 )  IS ---晚上9点cur_date_dd varchar2(2)")
    # get_table_name('CREATE TABLE `hbgz_yf2_sjgx.KF_BAS_PROBLEMPROCESS_DAY_1008`(')
    # ss=mystr1.getNextIndex("PROCEDURE")
    # ss=mystr1.get_str_betweenAB('PROCEDURE','(')
    str1="""
HBXNA1900226CGN00
HBXNA1900576CGN00
HBXNA2000222CGN00
HBXNA2000196CGN00
 
    """
    mystr1.get_CnPlugin(str1)

    str2 = """     
        """
    mystr1.get_tableName(str2)
