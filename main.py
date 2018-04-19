# coding=gbk
from core import AutoMarx

a = AutoMarx()
result = a.auto_answer()
if len(result) == 0:
    print('全部成功 直接交卷吧!!无视他说只做了0题!!! 100了记得给我github点个星星啊!!! ')
else:
    print("有" + str(len(result)) + "题提交失败")
    for key in result.keys():
        print(key + '答案为', end=' ')
        for answer in result[key]:
            print(chr(answer+65), end=' ')
        print()
