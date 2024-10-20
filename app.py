from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route('/add/<int:numberA>/<int:numberB>', methods=['GET'])
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify(status=200, result=result)

@app.route('/divide/<int:numberA>/<int:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify(status=400, result='Division by zero error')
    result = numberA / numberB
    return jsonify(status=200, result=result)


@app.route('/minus/<int:numberA>/<int:numberB>', methods=['GET'])
def minus(numberA, numberB):
    result = numberA - numberB
    return jsonify(status=200, result=result)

@app.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify(status=200, result=result)

@app.route('/mod/<int:numberA>/<int:numberB>', methods=['GET'])
def mod(numberA, numberB):
    result = numberA % numberB
    return jsonify(status=200, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
