from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "Serveur Flask en ligne !"})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    # Ici, on mettra plus tard l'appel à l'IA
    return jsonify({"response": f"Tu as demandé : {question}", "source": "Render"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
