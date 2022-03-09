from elasticsearch import Elasticsearch
from decouple import config
client = Elasticsearch("http://{}:{}".format(config('HOST'), config('ES_PORT')))
client_doctype = '_doc'
client_expert_index=config('ES_EXPERT_INDEX')