# protection.py

import os
import requests
from datetime import datetime

# === CONFIGURATION ===
DEADLINE = datetime(2025, 7, 13)
CHECK_URL = "https://verrou-check.vercel.app/check"  # Ton lien Vercel
MAIN_FILE = "main.py"

# === FONCTIONS ===

def is_locked():
    """Détermine si le logiciel doit être bloqué."""
    today = datetime.now()
    if today < DEADLINE:
        return False

    try:
        response = requests.get(CHECK_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == True:
                remove_self()
                return False
            else:
                print("🔒 Licence désactivée à distance.")
                return True
        else:
            print("⚠️ Erreur de communication avec le serveur distant.")
            return True
    except Exception as e:
        print(f"⚠️ Connexion impossible : {e}")
        return True


def prompt_unlock():
    """Bloque tout si la licence est invalide."""
    print("⛔ L'utilisation de ce logiciel est bloquée. Merci de contacter le développeur.")
    exit(1)


def remove_self():
    """Supprime le fichier protection.py et nettoie main.py automatiquement."""
    print("✅ Licence validée. Suppression du verrou...")
    try:
        os.remove(__file__)
    except Exception as e:
        print(f"Erreur suppression protection.py : {e}")

    try:
        with open(MAIN_FILE, "r") as f:
            lines = f.readlines()

        with open(MAIN_FILE, "w") as f:
            for line in lines:
                if "import protection" in line:
                    continue
                if "if protection.is_locked()" in line or "protection.prompt_unlock()" in line:
                    continue
                f.write(line)
        print("🧹 Nettoyage terminé.")
    except Exception as e:
        print(f"Erreur nettoyage main.py : {e}")
