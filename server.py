from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "running", "message": "Serveur Flask Fly.io opérationnel"})

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "Serveur Flask en ligne !"})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    # Ici on mettra plus tard l'appel à l'IA
    return jsonify({"response": f"Tu as demandé : {question}", "source": "Fly.io"})

if __name__ == "__main__":
    # ⚠️ Fly.io attend une appli qui écoute sur le port 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
