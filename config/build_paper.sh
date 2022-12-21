curl -X DELETE localhost:9200/paper
curl -H 'Content-Type: application/json' -X PUT 'localhost:9200/paper?pretty' -d'
{
    "mappings": {
        "dynamic": "strict",
        "properties": {
			"id": { "type": "text" },
			"title": { "type": "text" },
			"published": { "type": "text" },
            "authors": {"type": "text"}
        }
    }
}'