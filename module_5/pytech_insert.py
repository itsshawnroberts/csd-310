# Shawn Roberts
# 06/19/2021
# Module 5
# Pytech Insert
# my GitHub: git@github.com:itsshawnroberts/csd-310.git


# This function allows us to coneect to my MongoDB server cluster.
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ggu9b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

# My studentData variables store the information to want to push to my MongoDB cluster.
studentData = {
    "student_id": "1007",
    "first_name": "Tony",
    "last_name": "Stark"
     }
# This function allows Python to push my studentData information to my MongoDB cluster called students.
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
print(f"Inserted student record {studentData['first_name']} {studentData['last_name']} into students collection with document_id {result.inserted_id}\n\n")

input("End of program, press any key to exit...")