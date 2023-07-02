from my_excel import my_excel
from mystr import mystr
import pandas as pd

class mytable:
    def __init__(self):
        pass

    # read_excel 方法返回类型为 DataFrame，
    def read_excel_to_DataFrame(xlsx_file,sheet_name):
        # read_excel方法返回类型为DataFrame，不需要再次转换
        feature = pd.read_excel(xlsx_file, sheet_name)
        target = pd.read_excel(xlsx_file,sheet_name,usecols=[3])
        print(feature)
        print("-------------------------")
        print(target)



if __name__ == '__main__':
    mytable.read_excel_to_DataFrame(r"","")