# 📌 Système de Pointage par QR Code

Ce projet propose une solution simple et efficace pour enregistrer l’heure d’arrivée et de sortie des utilisateurs via un **formulaire web accessible par QR code**. Idéal pour les environnements professionnels et les suivis de présence au sein des entreprises.

---

## 🚀 Fonctionnement

1. L’utilisateur scanne un QR code pointant vers l’application web.
2. Un formulaire s’ouvre et lui demande :
   - Son **Nom** (en majuscules, avec saisie assistée).
   - Son **Département** (en minuscules, avec saisie assistée).
3. ➕ À la première saisie du jour : l’**heure d’arrivée** est enregistrée.
4. ➕ À la seconde saisie : l’**heure de sortie** est enregistrée.
5. ❌ Un message s’affiche si l’utilisateur tente de pointer une 3ᵉ fois.
6. 🕒 Si une sortie n’a pas été enregistrée la veille, elle peut l’être le lendemain.
7. 🧾 Les données sont :
   - Stockées en base **SQLite locale**.
   - Exportées **chaque jour** dans un fichier Excel (`excel/pointage_YYYY-MM-DD.xlsx`).

---

## 💻 Installation

### 🔧 Prérequis

- **Python** 3.7 ou supérieur
- `pip` installé

---

### 🐧 Linux / macOS

1. Ouvrir un terminal et se placer dans le dossier du projet :

   ```bash
   cd qr_pointage_system
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Démarrer le serveur :

   * Mode développement :

     ```bash
     python main.py
     ```

   * Avec le script de lancement personnalisé :

     ```bash
     python run.py --host 192.168.X.X
     ```

   * Mode production avec Gunicorn :

     ```bash
     gunicorn -w 4 -b 0.0.0.0:5000 main:app
     ```

4. Trouver votre IP locale :

   ```bash
   ip a  # Linux
   ifconfig  # macOS
   ```

5. Distribuer l’URL `http://<votre_ip_locale>:5000` via QR code.

---

### 🪟 Windows

1. Ouvrir PowerShell ou CMD :

   ```bash
   cd chemin\vers\qr_pointage_system
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Démarrer le serveur :

   ```bash
   python main.py
   ```

   ou :

   ```bash
   python run.py --host 192.168.X.X
   ```

   ou avec Gunicorn :

   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 main:app
   ```

4. Trouver l’IP locale :

   ```bash
   ipconfig
   ```

---

## ⚠️ Remarques

* Le serveur Flask (`main.py`) **n’est pas sécurisé** pour un déploiement en production.
* Pour un environnement professionnel, privilégiez **Gunicorn** ou un déploiement WSGI avec **Nginx** ou **Apache**.
* Le dossier `excel/` est généré automatiquement avec les données journalières.
* Le projet contient un système de **protection activable** via `protection.py` et une vérification distante via `run.py`.

---

## 🧭 Structure du projet

```plaintext
qr_pointage_system/
├── db.sqlite3            # Base de données locale
├── excel/                # Fichiers Excel générés par jour
├── main.py               # Application principale (Flask)
├── protection.py         # Système de verrouillage/licence
├── README.md             # Fichier d’explication
├── requirements.txt      # Dépendances
├── run.py                # Script de démarrage + QR code
├── static/
│   └── qr_code.png       # QR code généré automatiquement
├── templates/
│   ├── form.html         # Formulaire utilisateur
│   └── message.html      # Message de notification
```

---

## 📩 Contact

> Développé par **Abiye Enzo**

📧 Email : [abiyeenzo@gmail.com](mailto:abiyeenzo@gmail.com)

