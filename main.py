# ==========================================================
# Développé par Abiye Enzo pour le projet de pointage QR
# Contact : abiyeenzo@gmail.com
# Toute réutilisation non autorisée est interdite
# ==========================================================

# === BLOC DE PROTECTION - à ne pas modifier ===
import os
import requests
import hashlib
from datetime import datetime

def check_and_clean():
    DEADLINE = datetime(2025, 7, 13)
    today = datetime.now()
    protection_file = "protection.py"
    url_check = "https://verrou-check.vercel.app/check"

    # Avant la deadline : intégrité minimale
    if today < DEADLINE:
        if not os.path.exists(protection_file):
            print("❌ protection.py manquant.")
            exit(1)
        try:
            with open(__file__, "rb") as f:
                content = f.read()
            keywords = [
                b'import protection',
                b'if protection.is_locked()',
                b'protection.prompt_unlock()'
            ]
            for word in keywords:
                if word not in content:
                    print("❌ Code modifié. Blocage.")
                    exit(1)
        except Exception as e:
            print("Erreur vérification : ", e)
            exit(1)

    # Après deadline : vérif en ligne
    try:
        r = requests.get(url_check, timeout=5)
        if r.status_code == 200 and r.json().get("status") == True:
            print("✅ Paiement validé. Nettoyage du code.")
            remove_block()
            try:
                os.remove(protection_file)
            except:
                pass
        elif today >= DEADLINE:
            print("❌ Logiciel verrouillé. Paiement requis.")
            exit(1)
    except Exception as e:
        print("❌ Erreur réseau ou réponse : ", e)
        exit(1)

def remove_block():
    start_flag = "# === BLOC DE PROTECTION - à ne pas modifier ==="
    end_flag = "check_and_clean()"
    try:
        with open(__file__, "r") as f:
            lines = f.readlines()
        with open(__file__, "w") as f:
            skip = False
            for line in lines:
                if start_flag in line:
                    skip = True
                elif skip and end_flag in line:
                    skip = False
                    continue
                if not skip:
                    f.write(line)
    except Exception as e:
        print("Erreur nettoyage : ", e)

check_and_clean()
# === FIN DU BLOC DE PROTECTION ===

from flask import Flask, request, render_template, redirect, jsonify
import sqlite3
import os
from datetime import datetime, timedelta
import pandas as pd
import protection

if protection.is_locked():
    protection.prompt_unlock()

app = Flask(__name__)
DB_FILE = 'db.sqlite3'
EXCEL_FOLDER = 'excel'

os.makedirs(EXCEL_FOLDER, exist_ok=True)

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE,
                        department TEXT
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS pointages (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        date TEXT,
                        heure_arrivee TEXT,
                        heure_sortie TEXT
                    )''')
        conn.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].upper()
        dept = request.form["department"].lower()
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        hour = now.strftime("%H:%M:%S")
        yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")

        with sqlite3.connect(DB_FILE) as conn:
            c = conn.cursor()

            # Enregistrement utilisateur
            c.execute("SELECT * FROM users WHERE name = ?", (name,))
            if not c.fetchone():
                c.execute("INSERT INTO users (name, department) VALUES (?, ?)", (name, dept))

            # Chercher pointage du jour
            c.execute("SELECT * FROM pointages WHERE name = ? AND date = ?", (name, today))
            record_today = c.fetchone()

            # Chercher pointage d'hier sans sortie
            c.execute("SELECT * FROM pointages WHERE name = ? AND date = ? AND heure_sortie IS NULL", (name, yesterday))
            record_yesterday = c.fetchone()

            if record_today:
                if record_today[4] is None:
                    c.execute("UPDATE pointages SET heure_sortie = ? WHERE id = ?", (hour, record_today[0]))
                else:
                    return render_template("message.html", message="Tu as déjà pointé deux fois aujourd'hui.")
            elif record_yesterday:
                c.execute("UPDATE pointages SET heure_sortie = ? WHERE id = ?", (hour, record_yesterday[0]))
            else:
                c.execute("INSERT INTO pointages (name, date, heure_arrivee) VALUES (?, ?, ?)", (name, today, hour))

            conn.commit()

        # Générer Excel du jour
        excel_file = os.path.join(EXCEL_FOLDER, f"pointage_{today}.xlsx")
        data = []
        with sqlite3.connect(DB_FILE) as conn:
            c = conn.cursor()
            c.execute("SELECT name, department FROM users")
            users = {row[0]: row[1] for row in c.fetchall()}
            c.execute("SELECT name, date, heure_arrivee, heure_sortie FROM pointages WHERE date = ?", (today,))
            rows = c.fetchall()
            for row in rows:
                data.append({
                    "Nom": row[0],
                    "Département": users.get(row[0], ''),
                    "Heure Arrivée": row[2],
                    "Heure Sortie": row[3] or ""
                })

        df = pd.DataFrame(data)
        df.to_excel(excel_file, index=False)

        return redirect("/?success=1")

    return render_template("form.html")

@app.route("/autocomplete")
def autocomplete():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT DISTINCT name FROM users")
        names = sorted([row[0] for row in c.fetchall()])
        c.execute("SELECT DISTINCT department FROM users")
        depts = sorted([row[0] for row in c.fetchall()])
    return jsonify({"names": names, "departments": depts})

if __name__ == "__main__":
    init_db()
    app.run(debug=False, host="0.0.0.0", port=5000)