# convert bson to json 
bsondump --pretty --outFile author.json author.bson
# push to db 
python utils/add_data.py

# convert mongodb data to es data
python convert_to_es_data.py

# bulk insert
curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/_bulk?pretty' --data-binary @author_es.json