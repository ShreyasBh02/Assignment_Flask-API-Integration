from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/info')
def get_info():
    return jsonify({"id": request.args.get("id"), "name": "Test User"})

@app.route('/api/add', methods=['POST'])
def add():
    data = request.json
    result = data['a'] + data['b']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)