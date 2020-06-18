#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 14:44:32
# @Author  : BenLam
# @Link    : https://www.cnblogs.com/BenLam/
# @File    : assertion.py


from Public.log import LOG,logger


@logger('断言测试结果')
def assert_in(asserqiwang, fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1 = [value for value in result.keys()]
        # return_result = [k for k,v in [v for k,v in fanhuijson.items()][1].items()]

        return_result = [v for k,v in fanhuijson.items()][1]
        for k, v in result.items():
            if k in return_result.keys():
                if str(v) == str(return_result[k]):
                    print("通过检查")
                    return  { 'code':0,"result":'pass'}
                else:
                    print("Keys 检查通过，但 Value 检查未过")
                    return {'code':1,'result':'fail'}
            else:
                print("检查未过")
                return {'code':1,'result':'fail'}


        # 废弃代码
        # if set(value1).issubset(set(return_result)):
        #     print("通过检查")
        # else:
        #     print("检查未过")
        # if set(value1).issubset(set(return_result)):
        #     return  { 'code':0,"result":'pass'}
        # else:
        #     return {'code':1,'result':'fail'}
    else:
        LOG.info('填写测试预期值')
        return {"code":2,'result':'填写测试预期值'}