
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ggu9b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
 print(f"Student ID: {doc['student_id']}")
 print(f"First Name: {doc['first_name']}")
 print(f"Last Name:  {doc['last_name']}\n")

print ("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name:  {doc['last_name']}\n")


print("End of Program, press any key to continue...")
