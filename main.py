# coding=gbk
from core import AutoMarx

a = AutoMarx()
result = a.auto_answer()
if len(result) == 0:
    print('全部提交成功')
else:
    print("有" + str(len(result)) + "题提交失败")

a.finish_exam()
print('已提交试卷 扫描二维码 查看信息')