import sys
import os
import qrcode
from main import app, init_db

def generate_qr_code(url, path="static/qr_code.png"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img = qrcode.make(url)
    img.save(path)
    print(f"[QR] QR code généré : {path}")

def main():
    init_db()

    # Valeurs par défaut
    host = "0.0.0.0"
    port = 5000

    # Vérifie si on fournit host:port
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if ":" in arg:
            host, port = arg.split(":")
            port = int(port)
        else:
            host = arg

    url = f"http://{host}:{port}"
    generate_qr_code(url)

    print(f"[FLASK] Lancement sur {url}")
    app.run(debug=False, host=host, port=port)

if __name__ == "__main__":
    main()
