from pymongo import MongoClient
from pymongo.database import SystemJS

url = "mongodb+srv://admin:admin@cluster0.ggu9b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

studentData = {
    "student_id": "1007",
    "first_name": "Tony",
    "last_name": "Stark"
     }

result = db.students.insert_one(studentData)
print("-- INSERT STATEMENTS --")
print(f"Inserted student record {studentData['first_name']} {studentData['last_name']} into students collection with document_id {result.inserted_id}")


studentData = {
    "student_id": "1008",
    "first_name": "Steve",
    "last_name": "Rodgers"
     }
result = db.students.insert_one(studentData)
print(f"Inserted student record {studentData['first_name']} {studentData['last_name']} into students collection with document_id {result.inserted_id}")


studentData = {
    "student_id": "1009",
    "first_name": "Bucky",
    "last_name": "Barnes"
     }
result = db.students.insert_one(studentData)
print(f"Inserted student record {studentData['first_name']} {studentData['last_name']} into students collection with document_id {result.inserted_id}")
print()
print()
input("End of program, press any key to exit...")