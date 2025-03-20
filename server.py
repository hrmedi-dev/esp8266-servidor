from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Responde con un JSON de ejemplo
    return jsonify({"message": "Hola, prueba HRM!"})

@app.route('/data', methods=['POST'])
def post_data():
    # Obtiene los datos enviados en la solicitud POST
    data = request.get_json()
    temperatura = data.get('temperature')
    humedad = data.get('humidity')
    
    # Responde con los datos recibidos
    return jsonify({
        "received": {
            "temperatura": temperature,
            "humedad": humidity
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
