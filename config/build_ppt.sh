curl -X DELETE localhost:9200/ppt
curl -H 'Content-Type: application/json' -X PUT 'localhost:9200/ppt?pretty' -d'
{
    "mappings": {
        "dynamic": "strict",
        "properties": {
			"title": { "type": "text" },
			"paper": { "type": "text" }
        }
    }
}'