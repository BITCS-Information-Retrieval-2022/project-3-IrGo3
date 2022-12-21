curl -X DELETE localhost:9200/ebook
curl -H 'Content-Type: application/json' -X PUT 'localhost:9200/ebook?pretty' -d'
{
    "mappings": {
        "dynamic": "strict",
        "properties": {
			"id": { "type": "text" },
			"title": { "type": "text" },
			"published": { "type": "text" },
            "authors": {"type": "text"},
			"on_sale_date": {"type": "text"}
        }
    }
}'