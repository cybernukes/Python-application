from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

num = int()

@app.route('/')
def index():
    return render_template("webpage.html", num=num)

@app.route('/hit', methods=['GET'])
def hit():
    data = request.get_json()
    global num
    num = data['Number']

    return jsonify({"Message": "Data Recieved", "Data": num})

if __name__ == "__main__":
    app.run(debug=True)
