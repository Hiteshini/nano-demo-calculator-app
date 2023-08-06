from flask import Flask,request, jsonify

app = Flask(__name__)

# Endpoint: GET /calculator/greeting
@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return jsonify(message='Hello world!'), 200

# Endpoint: POST /calculator/add
@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    first = data.get('first', None)
    second = data.get('second', None)

    if first is None or second is None or not isinstance(first, (int, float)) or not isinstance(second, (int, float)):
        return jsonify(error='Invalid input. Both first and second must be numbers.'), 400

    result = first + second
    return jsonify(result=result), 200

# Endpoint: POST /calculator/subtract
@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    first = data.get('first', None)
    second = data.get('second', None)

    if first is None or second is None or not isinstance(first, (int, float)) or not isinstance(second, (int, float)):
        return jsonify(error='Invalid input. Both first and second must be numbers.'), 400

    result = first - second
    return jsonify(result=result), 200

if __name__ == '__main__':
    app.run(debug=True)
