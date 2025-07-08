from flask import Flask, request, jsonify, render_template

from flask_cors import CORS

app = Flask(name)

CORS(app)

num = int()

@app.route('/')

def index():

return render_template("webpage.html", num=num)

@app.route('/hit', methods=['POST'])

def hit():

data = request.get_json()

global num

num = data['Number']



return jsonify({"Message": "Data Recieved", "Data": num})

if name == "main":

app.run(debug=True)
