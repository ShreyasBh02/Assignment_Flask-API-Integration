from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods =['GET'])
def hello():
    return jsonify({'Message': 'Hello World'}), 200


@app.route('/api/add', methods =['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data ['b']
    return jsonify({'Result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)