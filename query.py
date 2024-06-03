import db
import embedding

query = 'positive'

query_results = db.collection.aggregate([
    {
        "$vectorSearch": {
        "queryVector": embedding.model.encode(query).tolist(),
        "index": "ReviewSemanticSearch",
        "path": "vector_review",
        "numCandidates": 50,
        "limit": 4
    }}
])

for document in query_results:
    print(f'Review: {document["sentiment"]}')

