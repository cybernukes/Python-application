from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

received_number = None
reply_number = None

@app.route('/post', methods=['POST'])
def receive_from_hardware():
    global received_number, reply_number
    data = request.get_json()
    received_number = data.get('number')
    reply_number = None
    return jsonify({"message": "Number received!"})

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", number=received_number)

@app.route('/reply', methods=['POST', 'GET'])
def handle_reply():
    global reply_number
    if request.method == 'POST':
        reply_number = request.form['reply_input']
        return "Reply received from user"
    return jsonify({"reply": reply_number})


if __name__ == "__main__":
    app.run(debug=True)
