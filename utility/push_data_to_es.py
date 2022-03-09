from pprint import pprint
import requests
import urllib
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer
import os,sys

directory = './data/dump/author_es.json'

es = Elasticsearch([{'host': '127.0.0.1', 'port': '9200'}])

res = [] 
with open(directory, 'r', encoding='utf-8') as f:
    lst_dct = json.load(f)

helpers.bulk(es, lst_dct, index='experts', doc_type='_doc',raise_on_error=False)