from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_example():
    return jsonify({'message': 'GET request received'}), 200

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()  # Obtiene los datos enviados en el cuerpo del POST
    return jsonify({'message': 'POST request received', 'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

