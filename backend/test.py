import pymongo
from bson.objectid import ObjectId
import time

from settings import parameters

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
        res = self.search_by_id(query)
        return res

    def search_by_id(self, id):
        db_query = {"_id": id if isinstance(id, ObjectId) else ObjectId(id)}
        db_res = self.doc.find_one(db_query)
        db_res["_id"] = str(db_res["_id"])
        # print(res)
        return db_res

paper_db = DBAccess(hosts=parameters["host"],
                    port=parameters["db_port"],
                    db_name=parameters["db_name"],
                    doc_name=parameters["papers_doc"])

id="63a316fcd51c00004700da35"

paper_db.search_by_id(id)