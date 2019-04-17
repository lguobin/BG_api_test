#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-02 10:33:53
# @Author  : BenLam (864551538@qq.org)
# @Link    : https://www.cnblogs.com/BenLam/
# @Version : $Id$

import os, datetime, time


from config.config import report_title, test_case_data, Report
from test_case_data.case import testinterface
from Public.log import logger, LOG
from Public.py_Html import createHtml
from Public.save_excel import read


@logger("******** {} ********".format(__name__))
def Run_interface_Test():
    '''执行测试'''
    starttime=datetime.datetime.now()

    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = read(test_case_data)
    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testinterface()

    if os.path.exists(Report) is False:
        os.system(r'touch %s' % Report)

    endtime=datetime.datetime.now()

    createHtml(titles = report_title,
                filepath = Report,
                starttime = starttime,
                endtime = endtime,
                passge = list_pass,
                fail = list_fail,
                id = listid,
                name = listname,
                key = listkey,
                coneent = listconeent,
                url = listurl,
                meth = listfangshi,
                yuqi = listqiwang,
                json = list_json,
                relusts = listrelust,
                weizhi = list_weizhi,
                exceptions = list_exption
            )
if __name__ == '__main__':
    Run_interface_Test()