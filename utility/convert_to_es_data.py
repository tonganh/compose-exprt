import json

data = '../data/dump/author.json'
data_out = '../data/dump/author_es.json'
with open(data, 'r') as f:
    js = json.load(f)

res = []
for dct in js:
    del dct['_id']
    del dct['avatar_url']
    if 'profile_urls' in dct.keys():
        del dct['profile_urls']
    del dct['description_html']
    del dct['is_crawled']
    if 'aff' in dct.keys():
        del dct['aff']
    res.append(dct)

# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

with open(data_out, "a") as log_file:
    msgs = [json.loads(msg) if type(msg) is str else msg for msg in res]
    json.dump(msgs, log_file, ensure_ascii=False)
    # for msg in msgs:
    #     json.dump(msg, log_file, ensure_ascii=False)
    #     log_file.write('\n')