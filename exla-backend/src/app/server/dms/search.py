from server.database.es import client, client_doctype, client_expert_index
import json
# helpers
def expert_es_helper(expert_data) -> dict:
    return {}

def search_expert(name=None, expertise_names='[]',organisation_name=None,sort_by='citation', default_size=1000):
    '''
    Search by name
    Search by expertise_names
    Search 
        Input: 
               sort by citation = True
               sort by h_index = False
               sort by i10_index = False
               expertise_names 
               organisation_name
               name
        Output: Expertise
    '''
    if sort_by=='citation':
        sort_by_citation = True
        sort_by_i10_index = False
        sort_by_h_index = False 
    elif sort_by=='i10_index':
        sort_by_citation = False
        sort_by_i10_index = True
        sort_by_h_index = False 
    elif sort_by=='h_index':
        sort_by_citation = False
        sort_by_i10_index = False
        sort_by_h_index = True 
    res = {}

    if not name:
        if expertise_names==[] and organisation_name == None: # search all
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            }
        elif expertise_names != [] and organisation_name != None: # search by expertise_names and organisation_names
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            }
        elif expertise_names != [] and organisation_name == None: # search by expertise_names
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            }
        elif expertise_names == [] and organisation_name != None: # search by organisation_name 
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            } 
    else: # search name match mot phan name 
        if expertise_names==[] and organisation_name == None: # search all by name
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            } 
        elif expertise_names != [] and organisation_name != None: # search by name, by expertise_names and organisation_names
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            }
        elif expertise_names != [] and organisation_name == None: # search by name, by expertise_names
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            }
        elif expertise_names == [] and organisation_name != None: # search by name, by organisation_name 
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            result = client.search(
                index=client_expert_index,
                body=query_body,
                size=default_size
            )
            size = result['hits']['total']
            result_body = result['hits']['hits']
            body_data = []
            for it in result_body:
                body_data.append(it['_source'])
            res = {
                'count': size,
                'data': body_data
            }  
    return res
