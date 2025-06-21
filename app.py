from flask import Flask, request, jsonify

app = Flask(__name__)

def get_operands():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return None, None
    return a, b

@app.route('/add', methods=['GET'])
def add():
    a, b = get_operands()
    if a is None:
        return jsonify({'error': 'Invalid parameters; provide numeric a and b'}), 400
    return jsonify({'result': a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    a, b = get_operands()
    if a is None:
        return jsonify({'error': 'Invalid parameters; provide numeric a and b'}), 400
    return jsonify({'result': a - b})

@app.route('/multiply', methods=['GET'])
def multiply():
    a, b = get_operands()
    if a is None:
        return jsonify({'error': 'Invalid parameters; provide numeric a and b'}), 400
    return jsonify({'result': a * b})

if __name__ == '__main__':
    # listen on port 5000 by default
    app.run(host='0.0.0.0', port=5000, debug=True)