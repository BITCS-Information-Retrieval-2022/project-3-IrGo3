#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Jinyu Liu
# @email: 1564556307@qq.com
# @datetime: 2022/11/12 9:55
# @file: ESClient
# @IDE: PyCharm
import time

from elasticsearch import Elasticsearch


class ESClient:
    def __init__(self, **kwargs):
        self.hosts = kwargs['hosts']
        self.port = kwargs['port']
        self.user = kwargs['user']
        self.password = kwargs['password']
        self.index = kwargs['index']
        self.es = Elasticsearch(hosts=[{'host': self.hosts, 'port': self.port}], http_auth=(self.user, self.password))

    def delete_index(self):
        return self.es.indices.delete(index=self.index)

    def put_mapping(self, body):
        self.es.indices.put_mapping(index=self.index, body=body)

    def search(self, query):
        raise NotImplementedError

    def __del__(self):
        self.es.transport.close()
        print("Elasticsearch is closed!")


class PaperClient(ESClient):
    def search(self, query):
        return self.search_paper(query)

    def search_paper(self, query):
        es_query = {
            "track_total_hits": "true",
            "from": query["size"] * query["from"],
            "size": query["size"],
            "query": {
                "bool": {
                    "must": [
                        {
                            "function_score": {
                                "query": {
                                    "bool": {
                                        "should": [
                                            {
                                                "match": {
                                                    "title": {
                                                        "query":
                                                            query["query"],
                                                            "boost": 2.0,
                                                            "operator": "or",
                                                            "minimum_should_match": "80%"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        }
        # if query["sort"] != "false":
        #     es_query["sort"] = [{"published": "true"}]
        res = self.es.search(index=self.index, body=es_query)
        print(res)
        id_list = [item["_id"] for item in res["hits"]["hits"]]
        print("id_list:", id_list, "\n")
        hit = dict()
        hit["total"] = res["hits"]["total"]["value"]
        hit["hit"] = id_list
        return hit


class EbookClient(ESClient):
    def search(self, query):
        return self.search_ebook(query)

    def search_ebook(self, query):
        es_query = {
            "track_total_hits": "true",
            "from": query["size"] * query["from"],
            "size": query["size"],
            "query": {
                "match": {
                    "title": {
                        "query": query["query"],
                        "operator": "or",
                        "minimum_should_match": 2
                    }
                }
            }
        }
        # if query["sort"] != "false":
        #     es_query["sort"] = [{"on_sale_date": "true"}]
        res = self.es.search(index=self.index, body=es_query)
        print(res)
        id_list = [item["_id"] for item in res["hits"]["hits"]]
        print("id_list:", id_list, "\n")
        hit = dict()
        hit["total"] = res["hits"]["total"]["value"]
        hit["hit"] = id_list
        return hit


class PPTClient(ESClient):
    def search(self, query):
        return self.search_ppt(query)

    def search_ppt(self, query):
        es_query = {
            "track_total_hits": "true",
            "from": query["size"] * query["from"],
            "size": query["size"],
            "query": {
                "match": {
                    "title": {
                        "query": query["query"],
                        "operator": "or",
                        "minimum_should_match": 2
                    }
                }
            }
        }
        res = self.es.search(index=self.index, body=es_query)
        print(res)
        id_list = [item["_id"] for item in res["hits"]["hits"]]
        print("id_list:", id_list, "\n")
        hit = dict()
        hit["total"] = res["hits"]["total"]["value"]
        hit["hit"] = id_list
        return hit


class VideoClient(ESClient):
    def search(self, query):
        return self.search_video(query)

    def search_video(self, query):
        es_query = {
            "track_total_hits": "true",
            "from": query["size"] * query["from"],
            "size": query["size"],
            "query": {
                "multi_match": {
                    "query": query["query"],
                    "type": "best_fields",
                    "fields": ["title^2", "description"],
                    "operator": "and"
                }
            }
        }
        res = self.es.search(index=self.index, body=es_query)
        print(res)
        id_list = [item["_id"] for item in res["hits"]["hits"]]
        print("id_list:", id_list, "\n")
        hit = dict()
        hit["total"] = res["hits"]["total"]["value"]
        hit["hit"] = id_list
        return hit


