#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 14:44:32
# @Author  : BenLam
# @Link    : https://www.cnblogs.com/BenLam/
# @File    : case.py

import os

from config.config import Config_Try_Num, test_case_data

from Public.requests import _request
from Public.log import LOG, logger
from Public.save_excel import read, write

from Public.assertion import assert_in

listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = read(test_case_data)

@logger("******** {} ********".format(__name__))
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_weizhi = 0
    list_exption = 0
    error_num=0

    a = 0

    for i in range(len(listurl)):

        while error_num <= Config_Try_Num+1:

            api = _request(url=listurl[i], key=listkey[i], connent=listconeent[i], method=listfangshi[i])
            apijson = api.methods()
            LOG.warning(listqiwang[i])
            LOG.warning(apijson)

            write(test_case_data, listid[i] , apijson['result'])

            LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listconeent[i], listurl[i], apijson, listqiwang[i]))

            if apijson['code'] == 0:
                assert_re = assert_in(asserqiwang=listqiwang[i], fanhuijson=apijson)
                LOG.warning(assert_re)
                
                if assert_re['code'] == 0:
                    list_json.append(apijson['result'])
                    listrelust.append('pass')
                    list_pass += 1
                    error_num=0
                    # continue
                    break
                elif assert_re['code'] == 1:
                    if error_num <=Config_Try_Num:
                        error_num+=1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num=0
                        list_fail += 1
                        listrelust.append('fail')
                        list_json.append(apijson['result'])
                        break
                elif assert_re['code'] == 2:
                    if error_num <Config_Try_Num:
                        error_num+=1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num=0
                        list_exption += 1
                        listrelust.append('exception')
                        list_json.append(assert_re['result'])
                        break
                else:
                    if error_num < Config_Try_Num:
                        error_num+=1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num=0
                        list_weizhi += 1
                        listrelust.append('未知错误')
                        list_json.append('未知错误')
                        break
            else:
                if error_num <Config_Try_Num:
                    error_num+=1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num=0
                    list_exption += 1
                    listrelust.append('exception')
                    list_json.append(apijson['result'])
                    break
    return listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi
