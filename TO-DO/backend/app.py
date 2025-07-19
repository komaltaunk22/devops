import os
from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create Flask app instance
app = Flask(__name__)

# MongoDB connection
uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("❌ MongoDB Connection Error:", e)

db = client['test']
collection = db['to-do']

@app.route('/submittodoitem', methods=['GET','POST'])
def submit_todo_item():
    request_data = request.get_json()

    if request_data :
        collection.insert_one(request_data)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
