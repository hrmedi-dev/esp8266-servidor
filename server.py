from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Responde con un JSON de ejemplo
    return jsonify({"message": "Hola, prueba hrm"})

@app.route('/data', methods=['POST'])
def post_data():
    # Obtiene los datos enviados en la solicitud POST
    data = request.get_json()
    temperature = data.get('temperatura')
    humidity = data.get('humedad')
    
    # Responde con los datos recibidos
    return jsonify({
        "received": {
            "temperatura": temperatura,
            "humedad": humedad
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
