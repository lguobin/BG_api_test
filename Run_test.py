#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-02 10:33:53
# @Author  : BenLam (864551538@qq.org)
# @Link    : https://www.cnblogs.com/BenLam/
# @Version : $Id$


# from Public.log import LOG, logger
# @logger("11111")
# def a():
# 	LOG.debug("22222")
# a()


# from testCase.case import testinterface
# from Public.test_requests import requ, TestApi
# a = TestApi("http://192.168.2.100:5001/v1/operators/login","key",{"name":"15920150690","password":"saiyao1234"},"POST")
# a.testapi()
# testinterface()


# from Public.save_excel import datacel
# from Public.get_excel import datacel
# import os
# path = os.getcwd() + '\\test_case_data\\case.xlsx'
# print(datacel(path))


# from Public.check import assert_in
# print(assert_in("code","code"))
# print(assert_in("code",{'code': 0, 'result': '{\n    "code": 2002,\n    "message": "Login required"\n}'}))


# from config.config import test_case_data
# from Public.get_excel import datacel
# print(datacel(test_case_data))


# from Public.requests import _request
# a = "https://api.saiyaoyun.com/v2/operators/login"
# b = ""
# c = '{"name":"13430367235","password":"saiyao1234"}'
# d = "get"
# aa = _request(a,b,c,d)
# cc = aa.methods()

# from Public.save_excel import write, datacel
# a = r"C:\1\api_automation_test-master\BG_api_test\test_case_data\case.xlsx"
# d='{"header":null,"a":1}'
# # write(a, 1, 7, str(cc))
# datacel(a)




# import unittest
# class test(unittest.TestCase):
# 	def setUp(self):
# 		pass
# 	def test_A(self):
# 		a = '{\n    "code": 2002,\n    "message": "Login required"\n}'
# 		b = self.assertIs(a, '{\n    "code": 2002,\n    "message": "Login required"\n}')
# if __name__ == '__main__':
# 	unittest.main()


from Public.panduan import assert_in
from Public.fengzhuang_dict import res

asserqiwang = "code=2002"
fj={'code': 0, 'result': {'message': 'Login required', 'code': 2002}}

# if len(asserqiwang.split('=')) > 1:
# 	data = asserqiwang.split('&')
# 	result = dict([(item.split('=')) for item in data])
# 	value1=[value for value in result.keys()]
# 	return_result = [k for k,v in [v for k,v in fj.items()][1].items()]


# 	print(value1)
# 	print(return_result)
# 	if set(value1).issubset(set(return_result)):
# 		print("1111111111111111111111")
# 	else:
# 		print("22222222")
# print(assert_in(asserqiwang, fj))


if len(asserqiwang.split('=')) > 1:
	result = dict([(item.split('=')) for item in asserqiwang.split('&')])
	if result.keys() & fj.keys() or result.value() & fj.value():
		print("1111111111111111111111")
	else:
		print("22222222")

