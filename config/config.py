#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 14:44:32
# @Author  : BenLam
# @Link    : https://www.cnblogs.com/BenLam/
# @File    : config.py


import os, time

Config_Try_Num = 1	# 失败重试

report_title = "http接口自动化测试报告"
# ******************
# 配置测试文件路径
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
test_case_data = basedir + "\\test_case_data\\case.xlsx"

current_time = time.strftime(f"%Y%m%d_%H%M", time.localtime(time.time()))
Report = (basedir + "\\test_case_data\\test_Report\\%s-result.html" %current_time)
# Report = (basedir + "\\test_case_data\\test_Report\\%s-result.html" %"Debug")
# ******************



# headers={
# 	"Accept": "application/json",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3760.0 Safari/537.36",
# 	"Authorization": Null,
# 	"Content-Type": "application/json",
# 	"Accept-Encoding": "gzip, deflate"
# }

