#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Jinyu Liu
# @email: 1564556307@qq.com
# @datetime: 2022/12/2 18:16
# @file: ESUtils
# @IDE: PyCharm

# from flask import request
from flask import request


def reformat_title(args):
    args["from"] = int("0")
    args["size"] = int("10")
    return args


def genQuery():
    query = {}
    args = request.args
    print(args)
    # args = {"type": "SEARCH_PAPER", "from": "0", "size": "10", "query": "python"}

    for arg in args:
        query[arg] = args[arg]
    query = reformat_title(query)
    return query


# reformat_map = {
#     "SEARCH_PAPER": reformat_title,
#     "SEARCH_VIDEO": reformat_title,
#     "SEARCH_PPT": reformat_title,
#     "SEARCH_EBOOK": reformat_title
# }
