from flask import Flask
import os

app = Flask(__name__)

# Seu PC
MAC = "f4:b5:20:4d:bb:1e"

# Porta WOL padrão (normalmente 9 ou 7)
WOL_PORT = 9

@app.route("/wake")
def wake():
    # envia magic packet
    os.system(f"wakeonlan -p {WOL_PORT} {MAC}")
    return "PC ligando via Wake-on-LAN..."

@app.route("/")
def home():
    return "servidor online 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)