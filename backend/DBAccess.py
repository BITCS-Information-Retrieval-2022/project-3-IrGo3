#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Jinyu Liu
# @email: 1564556307@qq.com
# @datetime: 2022/11/12 9:56
# @file: DBAccess
# @IDE: PyCharm


import pymongo
from bson.objectid import ObjectId
import time


class DBAccess:
    def __init__(self, **kwargs):
        hosts = kwargs["hosts"]
        port = kwargs["port"]
        db_name = kwargs["db_name"]
        doc_name = kwargs["doc_name"]
        con_str = "mongodb://{}:{}/{}".format(hosts, port, db_name)
        self.db_client = pymongo.MongoClient(con_str)
        self.db = self.db_client[db_name]
        self.doc = self.db[doc_name]

    def search(self, query):
        res = self.search_by_paper_id_list(query)
        return res

    def search_by_id_list(self, id_list):
        res = []
        for id in id_list:
            db_query = {"_id": id if isinstance(id, ObjectId) else ObjectId(id)}
            db_res = self.doc.find_one(db_query)
            db_res["_id"] = 0
            res.append(db_res)
            # print(res)
        return res

    def search_by_paper_id_list(self, query):
        res = self.search_by_id_list(query["hits"]["hit"])
        # DBAccess.reformat_id(res)
        query["hits"]["hit"] = res
        return query
