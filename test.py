import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['terminal_blog']
collection = database['students']

#students = collection.find({})
#for student in students:
#    print(student)

students = [student['mark'] for student in collection.find({})]
print(students)