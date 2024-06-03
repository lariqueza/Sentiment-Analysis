import pymongo
from pymongo.errors import ConnectionFailure
import pandas


try:
    #create a mongodb instance and disable certificate verification
    client = pymongo.MongoClient(
        "mongodb+srv://xxxxxxxx:xxxxxxxxx@xxxxxxxx.xw4iwxe.mongodb.net/?retryWrites=true&w=majority&appName=xxxxxxx",
        tls=True,
        tlsAllowInvalidCertificates=True
    )

    #verify connection
    client.admin.command('ping')
    print("Connection to MongoDB Atlas successful")

    #access the database
    db = client.droid

    #access the collection
    collection = db.signal

except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")

except Exception as e:
    print(f"An error occurred: {e}")


#load csv data
review_data1 = pandas.read_csv('review_data1.csv')
review_data1.head()

#insert data into dabase collection

#convert dataframe record into dictionary
review_data1 = review_data1.to_dict(orient='records')
#insert data into collection
collection.insert_many(review_data1)
print("data inserted successfully")

