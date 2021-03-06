#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-10 14:44:32
# @Author  : BenLam
# @Link    : https://www.cnblogs.com/BenLam/
# @File    : requests.py


import requests,json
from Public.log import LOG,logger


@logger("******** {} ********".format(__name__))
class _request(object):

    def __init__(self, url, key, connent, method, headers={}):
        self.url = url
        self.key = key
        self.connent = connent
        self.method = method
        self.headers = headers

    def methods(self):
        try:
            if self.method=="POST" or self.method=="post":
                self.parem = {"key": self.key, "info": self.connent}
                json_data = self.post(self.url, self.connent)

            elif self.method=="GET" or self.method=="get":
                self.parem = {"key": self.key, "info": self.connent}
                json_data = self.get(url=self.url)

            else:
                print("暂不支持这个请求模式~~~")
            return json_data
        except Exception as e:
            LOG.info("请求返回值出错，出错原因:%s"%e)

    def get(self, url):
        # get消息
        try:
            r = requests.get(url, headers=self.headers)
            r.encoding = "UTF-8"
            json_response = json.loads(r.text)
            return {"code":0,"result":json_response}
        except Exception as e:
            LOG.info("get请求出错，出错原因:%s"%e)
            return {"code": 1, "result": "get请求出错，出错原因:%s"%e}

    def post(self, url, params):
        # post消息
        data = json.loads(params)
        try:
            r =requests.post(url=url, json=data, headers=self.headers)
            json_response = json.loads(r.text)
            return {"code": 0, "result": json_response}
        except Exception as e:
            LOG.info("post请求出错，出错原因:%s" % e)
            return {"code": 1, "result": "post请求出错，出错原因:%s" % e}


    def putfile(self,url,params):
        # put请求
        try:
            data=json.dumps(params)
            me=requests.put(url,data)
            json_response=json.loads(me.text)
            return {"code": 0, "result": json_response}
        except Exception as e:
            LOG.info("put请求出错，出错原因:%s" % e)
            return {"code": 1, "result": "put请求出错，出错原因:%s" % e}

    def delfile(self,url,params):
        # 删除的请求
        try:
            del_word=requests.delete(url,params=params,headers=self.headers)
            json_response=json.loads(del_word.text)
            return {"code": 0, "result": json_response}
        except Exception as e:
            LOG.info("del请求出错，出错原因:%s" % e)
            return {"code": 1, "result": "del请求出错，出错原因:%s" % e}
