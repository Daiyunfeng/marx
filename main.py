# coding=gbk
from core import AutoMarx

a = AutoMarx()
result = a.auto_answer()
if len(result) == 0:
    print('ȫ���ɹ� ֱ�ӽ����!!������˵ֻ����0��!!! 100�˼ǵø���github������ǰ�!!! ')
else:
    print("��" + str(len(result)) + "���ύʧ��")
    for key in result.keys():
        print(key + '��Ϊ', end=' ')
        for answer in result[key]:
            print(chr(answer+65), end=' ')
        print()
