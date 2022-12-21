#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Jinyu Liu
# @email: 1564556307@qq.com
# @datetime: 2022/11/12 9:51
# @file: main
# @IDE: PyCharm
import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from settings import parameters
from ESUtils import genQuery
from ESClient import PaperClient, VideoClient, PPTClient, EbookClient
from DBAccess import DBAccess
import json

app = Flask(__name__)
CORS(app)


paper_es = PaperClient(hosts=parameters["host"],
                       port=parameters["es_port"],
                       user=parameters["es_user"],
                       password=parameters["es_password"],
                       index=parameters["papers_index"])

paper_db = DBAccess(hosts=parameters["host"],
                    port=parameters["db_port"],
                    db_name=parameters["db_name"],
                    doc_name=parameters["papers_doc"])

video_es = VideoClient(hosts=parameters["host"],
                       port=parameters["es_port"],
                       user=parameters["es_user"],
                       password=parameters["es_password"],
                       index=parameters["video_index"])

video_db = DBAccess(hosts=parameters["host"],
                    port=parameters["db_port"],
                    db_name=parameters["db_name"],
                    doc_name=parameters["video_doc"])

ppt_es = PPTClient(hosts=parameters["host"],
                   port=parameters["es_port"],
                   user=parameters["es_user"],
                   password=parameters["es_password"],
                   index=parameters["ppt_index"])

ppt_db = DBAccess(hosts=parameters["host"],
                  port=parameters["db_port"],
                  db_name=parameters["db_name"],
                  doc_name=parameters["ppt_doc"])

ebook_es = EbookClient(hosts=parameters["host"],
                       port=parameters["es_port"],
                       user=parameters["es_user"],
                       password=parameters["es_password"],
                       index=parameters["ebook_index"])

ebook_db = DBAccess(hosts=parameters["host"],
                    port=parameters["db_port"],
                    db_name=parameters["db_name"],
                    doc_name=parameters["ebook_doc"])


# @app.route('/paper', methods=['GET'])
def search_paper():
    query = genQuery()
    query["hits"] = paper_es.search(query)
    res = paper_db.search(query)
    return json.dumps(res["hits"]["hit"])


# @app.route('/ebook', methods=['GET'])
def search_ebook():
    query = genQuery()
    query["hits"] = ebook_es.search(query)
    res = ebook_db.search(query)
    return json.dumps(res["hits"]["hit"])


# @app.route('/ppt', methods=['GET'])
def search_ppt():
    query = genQuery()
    query["hits"] = ppt_es.search(query)
    res = ppt_db.search(query)
    return json.dumps(res["hits"]["hit"])


# @app.route('/video', methods=['GET'])
def search_video():
    query = genQuery()
    query["hits"] = video_es.search(query)
    res = video_db.search(query)
    print(res)
    return json.dumps(res["hits"]["hit"])


@app.route('/search', methods=['GET', 'POST'])
def search():
    dtype = request.args.get('dtype', '')
    if dtype == "1":
        return search_paper()
    elif dtype == "2":
        return search_video()
    elif dtype == "3":
        return search_ppt()
    else:
        return search_ebook()


@app.route('/', methods=['GET'])
def index():
    return jsonify("IrGoGoGo")


if __name__ == "__main__":
    app.run(debug=True)
