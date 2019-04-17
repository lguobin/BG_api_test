#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 14:44:32
# @Author  : BenLam
# @Link    : https://www.cnblogs.com/BenLam/
# @File    : save_excel.py

import xlrd
from Public.log  import LOG,logger

# Setting xls column valuekey
test_id = 0
test_name = 1
test_key = 2
test_coneent = 3
test_url = 4
test_fangshi = 5
test_qiwang = 6
write_return_data = 7

@logger('保存测试用例文件')
def read(filrpath):
    try:
        file=xlrd.open_workbook(filrpath)
        me=file.sheets()[0]
        nrows=me.nrows
        ID=[]
        listkey=[]
        listconeent=[]
        listurl=[]
        listfangshi=[]
        listqiwang=[]
        listrelut=[]
        listname=[]
        for i in range(1,nrows):
            ID.append(me.cell(i,test_id).value)
            listname.append(me.cell(i,test_name).value)
            listkey.append(me.cell(i,test_key).value)
            listconeent.append(me.cell(i,test_coneent).value)
            listurl.append(me.cell(i,test_url).value)
            listfangshi.append((me.cell(i,test_fangshi).value))
            listqiwang.append((me.cell(i,test_qiwang).value))
        return ID,listkey,listconeent,listurl,listfangshi,listqiwang,listname
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)
        return

def _datacel(filrpath):
    try:
        all_case=[]
        file=xlrd.open_workbook(filrpath)
        me=file.sheets()[0]
        nrows=me.nrows
        for i in range(1,nrows):
            all_case.append({"id":me.cell(i,0).value,'key':me.cell(i,2).value,
                             'coneent':me.cell(i,3).value,'url':me.cell(i,4).value,
                             'name':me.cell(i,1).value,'fangshi':me.cell(i,5).value,
                             'assert':me.cell(i,6).value})
        return all_case
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)
        return


from xlutils.copy import copy
@logger('写入返回值')
def write(filrpath, row, value):
    '''
    # 写入到excel数据
    # 行,
    # 列,
    # 写入 value.
    '''
    try:
        read_data = xlrd.open_workbook(filrpath)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, write_return_data, str(value))
        write_data.save(filrpath)

    except Exception as e:
        LOG.info('写入测试用例返回值失败，原因是:%s' %e)
        return


if __name__ == '__main__':
    # print(datacel(a))
    a = r"..//test_case_data//case.xlsx"
    b = {"a":1}
    write_value(a,b)