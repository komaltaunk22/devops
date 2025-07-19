from flask import Flask, jsonify,render_template, request
import json
from dotenv import load_dotenv
import os

load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client['test']
collection = db['data']

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api')
def api():
    # return 'API ENdpoint'
    file= open("products.json", "r")
    json_data = file.read()
    file.close()
    return json_data

@app.route('/save', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username =request.form['username']
        password =request.form['password']
        res = collection.insert_one({"username": username, "password": password})
        if (res.inserted_id):
            return render_template("success.html", username=username)
        else:
            print("An Error Encounter. Please try again later")
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)