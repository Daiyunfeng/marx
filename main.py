# coding=gbk
from core import AutoMarx

a = AutoMarx()
result = a.auto_answer()
if len(result) == 0:
    print('ȫ���ύ�ɹ�')
else:
    print("��" + str(len(result)) + "���ύʧ��")

a.finish_exam()
print('���ύ�Ծ� ɨ���ά�� �鿴��Ϣ')