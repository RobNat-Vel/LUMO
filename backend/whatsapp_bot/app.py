from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()  # carga .env automáticamente

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "lumo-verify-12345")

print(f"[BOOT] VERIFY_TOKEN cargado: {VERIFY_TOKEN!r}")

@app.get("/webhook")
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("[OK] Verificación correcta")
        return challenge or "", 200
    else:
        print(f"[FAIL] 403: token recibido={token!r} esperado={VERIFY_TOKEN!r}, mode={mode!r}")
        return "Error de verificación", 403

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True) or {}
    print("Mensaje recibido:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
