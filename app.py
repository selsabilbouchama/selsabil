from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<float:a>/<float:b>', methods=['GET'])
def add(a, b):
    return jsonify({'status': 200, 'result': a + b})

# Similarly, define other operations like subtract, multiply, divide
@app.route('/subtract/<float:a>/<float:b>', methods=['GET'])
def subtract(a, b):
    return jsonify({'status': 200, 'result': a - b})

@app.route('/multiply/<float:a>/<float:b>', methods=['GET'])
def multiply(a, b):
    return jsonify({'status': 200, 'result': a * b})

@app.route('/divide/<float:a>/<float:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return jsonify({'status': 400, 'error': 'Division by zero'})
    return jsonify({'status': 200, 'result': a / b})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
