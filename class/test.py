from typing import List




def test1(str):
    if isinstance(str, list)==True:
        print("数组")
    else:
        print("字符串")



print(test1("sdsd"))
print(test1([1,2,3]))




