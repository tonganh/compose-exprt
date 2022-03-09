import pymongo
import json

MONGO_USERNAME="root"
MONGO_PASSWORD="98859B9980A218F6DAD192B74781E15D"
MONGO_URI="mongodb://root:98859B9980A218F6DAD192B74781E15D@0.0.0.0:27017"
# myclient = pymongo.MongoClient("mongodb://{}:{}@localhost:27017/".format(MONGO_USERNAME, MONGO_PASSWORD))
myclient = pymongo.MongoClient("mongodb://root:98859B9980A218F6DAD192B74781E15D@0.0.0.0:27017")
mydb = myclient["expert_landscape"]

mycol = mydb['author']

data = '../data/dump/author.json'

with open(data, 'r') as f:
    js = json.load(f)

res = []
for dct in js:
    del dct['_id']
    res.append(dct)

mycol.insert_many(res)
