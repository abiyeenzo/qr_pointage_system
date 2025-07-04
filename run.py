import sys
from main import app, init_db

def main():
    init_db()

    host = "0.0.0.0"  # valeur par défaut : écoute toutes interfaces
    port = 5000       # port par défaut

    # Si on passe un argument IP, on l’utilise
    if len(sys.argv) > 1:
        host = sys.argv[1]

    print(f"Lancement du serveur Flask sur http://{host}:{port}")
    app.run(debug=False, host=host, port=port)

if __name__ == "__main__":
    main()
