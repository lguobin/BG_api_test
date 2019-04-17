# **interface_Test 帮助与思维导入**
PS：此项目由 liwanlei/jiekou-python3 修改
*****

## **一. 运行环境**
- Linux，Windows，MacOS
- Python 3.7

## **二. 相关lib安装及配置**
```python
pip install requests
pip install logbook
pip install xlrd
pip install xlutils
```

或直接在终端运行：
```base
[root@BenLam-vm_0 ~]# pip install -r requirements.txt
```

## **三. 运行**
```
[root@BenLam-vm_0 ~]# python Run_http_Test.py
```

## **四. 添加、修改测试用例**
- 直接在 .config//config.py 文件中即可配置测试用例地址
- 测试用例：
    * 为了方便管理测试用例均在 test_case_data 一个文件夹中，包含 xls 、测试结果
    * 所有测试结果均会写入 xls 文件中“实际结果”字段
- 断言：
    * 目前仅支持 Dict 、json 返回格式（后期考虑支持更多）

## **五. 目录简介**
1.config文件夹用来存放我们的测试环境配置信息，
2.test_case_data用来存储我们的测试数据，Excel管理测试用例。
3.requests库，从Excel取测试数据的封装
4.Public 展示测试报告相关的脚本，这里可以自己封装，也可以使用现成的，我这里是基于我自己封装的，最后生成的测试报告更加易懂，出错可以尽快排查相关原因
5.test_case_data/report 存放测试报告，
6.Run_http_Test.py 主运行文件。运行后可以生成相应的测试报告

## **六. See you later......**
- 下一波更新：
    * 定制 Headers
    * 联动上下文接口
    * 多线程
    * DB存储用例与结果
