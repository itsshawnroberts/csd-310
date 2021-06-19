# Shawn Roberts
# 06/18/2021
# 5.2 Pytech: Collection Creation

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ggu9b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

print(db.list_collection_names())
