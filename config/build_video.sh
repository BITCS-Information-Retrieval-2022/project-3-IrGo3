curl -X DELETE localhost:9200/video
curl -H 'Content-Type: application/json' -X PUT 'localhost:9200/video?pretty' -d'
{
    "mappings": {
        "dynamic": "strict",
        "properties": {
			"bvid": { "type": "text" },
			"title": { "type": "text" },
			"description": { "type": "text" }
        }
    }
}'