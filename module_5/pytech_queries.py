
# Shawn Roberts
# 06/19/2021
# Module 5
# 5.3 Pytech Queries
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

# This function allows us to find a certain piece of data within our student document.
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY -- ")
doc = db.students.find_one({"student_id": "1007"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}\n\n")

print("End of Program, press any key to continue...")
