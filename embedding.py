from sentence_transformers import SentenceTransformer
import db

#create instance for text embedding
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#split review dataset into 50, create and store vector embeddings
review_documents = db.collection.find({'review': {"$exists": True}}).limit(50)
for doc in review_documents:
    review_embedding = model.encode(doc['review'])
    doc['vector_review'] = review_embedding.tolist()
    db.collection.replace_one({'_id': doc['_id']}, doc)

print("review embdeddings updated for the first 50 documents where 'review' exists")



