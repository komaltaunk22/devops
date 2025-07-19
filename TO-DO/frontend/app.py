from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def to_do():
    if request.method == 'POST':
        form_data ={
            "item_name" : request.form.get('item_name'),
            "item_desc" : request.form.get('item_desc')
        }
        
               # Send to backend
        response = requests.post('http://localhost:8000/submittodoitem', json=form_data)
        print(response.json())  # Optional: Debug print

    return render_template('index.html')  # No leading slash

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
