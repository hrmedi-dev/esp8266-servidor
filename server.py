from flask import Flask, request, jsonify

app = Flask(__name__)

# Estado inicial del LED
led_state = "off"

@app.route('/led', methods=['GET'])
def control_led():
    global led_state
    state = request.args.get('state')  # Obtiene el parámetro 'state' de la URL

    if state in ["on", "off"]:
        led_state = state
        return jsonify({"message": f"LED turned {led_state}"}), 200
    else:
        return jsonify({"error": "Invalid state. Use 'on' or 'off'"}), 400

@app.route('/led/status', methods=['GET'])
def led_status():
    return jsonify({"led_state": led_state})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
