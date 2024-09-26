from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['certificate_db']

# Access the collection
certificates_collection = db['certificates']

# Insert the certificate document
certificate = {
    'certificate_id': '12345',
    'image_path': 'D:/again/certificate_project/static/certificates/12345.png'
}

result = certificates_collection.insert_one(certificate)

# Print the result
print(f'Inserted document with id: {result.inserted_id}')
