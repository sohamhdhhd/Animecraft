from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

# Initialize Flask app
app = Flask(__name__)

# MongoDB Atlas connection string (replace with your credentials)
mongo_uri = "mongodb+srv://bak01072007:bak123456@waifu2.5ahbyyu.mongodb.net/contactFormDB?retryWrites=true&w=majority"

# Initialize MongoDB Client
client = MongoClient(mongo_uri)

# Select the database
db = client.contactFormDB
# Select the collection where you want to store the form data
contact_collection = db.contacts

# Route to handle the form submission
@app.route('/contact', methods=['POST'])
def contact_form():
    # Get data from the form
    data = request.json

    # Prepare the data for MongoDB
    contact_data = {
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'subject': data['subject'],
        'message': data['message']
    }

    # Insert data into MongoDB
    contact_collection.insert_one(contact_data)

    return jsonify({"message": "Data saved successfully!"})

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
