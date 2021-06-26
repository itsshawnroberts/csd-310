# Shawn Roberts
# 06/26/2021
# Module 6
# 6.3 Pytech: Deleting Documents
# my GitHub: git@github.com:itsshawnroberts/csd-310.git


# Establishing connection to MongoDB to retrieve data.
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ggu9b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

# Telling Python to find the documents we want to we in the output.
docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

studentData = {
    "student_id": "1010",
    "first_name": "Peggy",
    "last_name": "Carter"
     }
result = db.students.insert_one(studentData)
print("-- INSERT STATEMENTS --")
print(f"Inserted student record {studentData['first_name']} {studentData['last_name']} into students collection with document_id {result.inserted_id}\n")

# Printing the updated data for student_id: 1007.
print("-- DISPLAYING STUDENT TEST DOC --")
doc = db.students.find_one({"student_id": "1010"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n\n")

# This deletes the student_id 1010 from the document.
result = db.students.delete_one({"student_id": "1010"})

# Print all documents from students document.
docs = db.students.find({})
print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
 print(f"Student ID: {doc['student_id']}")
 print(f"First Name: {doc['first_name']}")
 print(f"Last Name:  {doc['last_name']}\n")


print("End of Program, press any key to continue...")