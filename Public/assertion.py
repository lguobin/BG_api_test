#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 14:44:32
# @Author  : BenLam
# @Link    : https://www.cnblogs.com/BenLam/
# @File    : assertion.py


from Public.log import LOG,logger



@logger('断言测试结果')
def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=[value for value in result.keys()]
        return_result = [k for k,v in [v for k,v in fanhuijson.items()][1].items()]


        if set(value1).issubset(set(return_result)):
            print("通过检查")
        else:
            print("检查未过")

        if set(value1).issubset(set(return_result)):
            return  { 'code':0,"result":'pass'}
        else:
            return {'code':1,'result':'fail'}
    else:
        LOG.info('填写测试预期值')
        return  {"code":2,'result':'填写测试预期值'}
