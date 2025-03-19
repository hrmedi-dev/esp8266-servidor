from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Responde con un JSON de ejemplo
    return jsonify({"message": "Hello, this is a GET response!"})

@app.route('/data', methods=['POST'])
def post_data():
    # Obtiene los datos enviados en la solicitud POST
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    
    # Responde con los datos recibidos
    return jsonify({
        "received": {
            "temperature": temperature,
            "humidity": humidity
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
