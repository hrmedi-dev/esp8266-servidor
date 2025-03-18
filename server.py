from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Servidor en Railway funcionando! 🚀"

@app.route("/led", methods=["POST"])
def led():
    data = request.json
    if not data or "estado" not in data:
        return jsonify({"error": "Falta el parámetro 'estado'"}), 400

    estado = data["estado"]
    if estado == "encender":
        print("LED ENCENDIDO")  # Aquí iría la lógica para encender el LED
    elif estado == "apagar":
        print("LED APAGADO")  # Aquí iría la lógica para apagar el LED
    else:
        return jsonify({"error": "Comando no válido"}), 400

    return jsonify({"mensaje": f"LED {estado} correctamente"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
