# **interface_Test ������˼ά����**
PS������Ŀ�� liwanlei/jiekou-python3 �޸�
*****

## **һ. ���л���**
- Linux��Windows��MacOS
- Python 3.7

## **��. ���lib��װ������**
```python
pip install requests
pip install logbook
pip install xlrd
pip install xlutils
```

��ֱ�����ն����У�
```base
[root@BenLam-vm_0 ~]# pip install -r requirements.txt
```

## **��. ����**
```
[root@BenLam-vm_0 ~]# python Run_http_Test.py
```

## **��. ��ӡ��޸Ĳ�������**
- ֱ���� .config//config.py �ļ��м������ò���������ַ
- ����������
    * Ϊ�˷����������������� test_case_data һ���ļ����У����� xls �����Խ��
    * ���в��Խ������д�� xls �ļ��С�ʵ�ʽ�����ֶ�
- ���ԣ�
    * Ŀǰ��֧�� Dict ��json ���ظ�ʽ�����ڿ���֧�ָ��ࣩ

## **��. Ŀ¼���**
1.config�ļ�������������ǵĲ��Ի���������Ϣ��
2.test_case_data�����洢���ǵĲ������ݣ�Excel�������������
3.requests�⣬��Excelȡ�������ݵķ�װ
4.Public չʾ���Ա�����صĽű�����������Լ���װ��Ҳ����ʹ���ֳɵģ��������ǻ������Լ���װ�ģ�������ɵĲ��Ա�������׶���������Ծ����Ų����ԭ��
5.test_case_data/report ��Ų��Ա��棬
6.Run_http_Test.py �������ļ������к����������Ӧ�Ĳ��Ա���

## **��. See you later......**
- ��һ�����£�
    * ���� Headers
    * ���������Ľӿ�
    * ���߳�
    * DB�洢��������
