from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import time


app = Flask(__name__)
CORS(app)



@app.route("/api/status", methods = ["GET"])
def status():
    address_ip = "169.254.225.36"
    port = 29999
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((address_ip, port))
                client_socket.send("robotmode\n".encode())
                time.sleep(1)
                response = client_socket.recv(4096).decode()
                if "RUNNING" in response:
                    response = "Green"
                else:
                    response = "Red"
    except ConnectionError as e:
        print(f"error => {e}")
    return jsonify({"status": response}), 200


@app.route("/api/safety", methods = ["GET"])
def safety():
    address_ip = "169.254.225.36"
    port = 29999
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((address_ip, port))
                client_socket.send("safetystatus\n".encode())
                time.sleep(1)
                response = client_socket.recv(4096).decode()
    except ConnectionError as e:
        print(f"error => {e}")
    return jsonify({"Safety": response}), 200

@app.route("/api/report", methods = ["GET"])
def report():
    address_ip = "169.254.225.36"
    port = 29999
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((address_ip, port))
                client_socket.send(" generate flight report\n".encode())
                time.sleep(1)
                response = client_socket.recv(4096).decode()
    except ConnectionError as e:
        print(f"error => {e}")
    return jsonify({"Report": response}), 200

@app.route('/api/power_on', methods=['POST'])
def power_on():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Aucune donnée reçue")
        else:
            address_ip = "169.254.225.36"
            port = 29999
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((address_ip, port))
                client_socket.send("power on\n".encode())
                time.sleep(5)
                client_socket.send("brake release\n".encode())
                time.sleep(5)
        return jsonify({"message": "Power on command received"}), 200

    except Exception as e:
        app.logger.error(f"Une erreur est survenue: {str(e)}")
        return jsonify({"error": "Une erreur est survenue", "details": str(e)}), 500

@app.route('/api/power_off', methods=['POST'])
def power_off():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Aucune donnée reçue")
        else:
            address_ip = "169.254.225.36"
            port = 29999
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((address_ip, port))
                client_socket.send("power off\n".encode())
                time.sleep(5)

        return jsonify({"message": "Power off command received"}), 200

    except Exception as e:
        app.logger.error(f"Une erreur est survenue: {str(e)}")
        return jsonify({"error": "Une erreur est survenue", "details": str(e)}), 500



@app.route('/api/play_program', methods=['POST'])
def play_program():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Aucune donnée reçue")
        else:
            address_ip = "169.254.225.36"
            port = 29999
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((address_ip, port))
                client_socket.send(("load photo2.urp\n").encode())
                time.sleep(20)
                client_socket.send(("play\n").encode())
                time.sleep(20)

        return jsonify({"message": "Play command received"}), 200

    except Exception as e:
        app.logger.error(f"Une erreur est survenue: {str(e)}")
        return jsonify({"error": "Une erreur est survenue", "details": str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)



