from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/led", methods=["POST"])
def led_control():
    data = request.get_json()
    estado = data.get("estado")
    
    if estado == "encender":
        # Aquí pondrías el código para encender el LED en el ESP8266
        print("Encender LED")
        return jsonify({"message": "LED encendido"})
    
    elif estado == "apagar":
        # Aquí pondrías el código para apagar el LED en el ESP8266
        print("Apagar LED")
        return jsonify({"message": "LED apagado"})
    
    return jsonify({"message": "Comando no válido"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
