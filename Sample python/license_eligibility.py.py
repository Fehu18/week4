from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the License Eligibility Checker!"

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.get_json()
    age = data.get('age')
    
    if not age:
        return jsonify({"error": "Age is required"}), 400
    
    try:
        age = int(age)
    except ValueError:
        return jsonify({"error": "Invalid age format. Age should be an integer."}), 400
    
    if age >= 18:
        return jsonify({"eligible": True, "message": "You are eligible for a driver's license."})
    else:
        return jsonify({"eligible": False, "message": "You are not eligible for a driver's license."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
