Bien vu ! Je te rajoute la partie pour `run.py` dans la structure et une petite explication dans la section installation. Voici la version mise à jour :

````markdown
# Système de Pointage par QR Code

Ce projet permet à des utilisateurs de pointer leur **heure d’arrivée** et **heure de sortie** en scannant un QR code, puis en saisissant leur nom et département via une interface web simple.

---

## Fonctionnement après scan du QR code

1. L’utilisateur scanne le QR code (contenant simplement l’URL de l’application).
2. Le navigateur s’ouvre sur un formulaire web où il saisit :  
   - Son **Nom** (en majuscules, avec suggestions automatiques).  
   - Son **Département** (en minuscules, avec suggestions automatiques).
3. À la première saisie du jour, le système enregistre automatiquement l’heure d’arrivée.
4. À la seconde saisie le même jour, le système enregistre l’heure de sortie.
5. Si la personne pointe plus de deux fois par jour, un message l’en informe.
6. Si la personne est arrivée la veille sans heure de sortie, elle peut l’enregistrer le lendemain.
7. Toutes les données sont stockées dans une base SQLite locale et exportées quotidiennement dans un fichier Excel situé dans le dossier `excel/`.

---

## Installation

### Prérequis

- Python 3.7 ou supérieur installé sur votre machine.  
- `pip`, le gestionnaire de paquets Python.

---

### Installation sur Linux / macOS

1. Ouvrez un terminal.
2. Clonez le projet ou copiez les fichiers dans un dossier.
3. Placez-vous dans ce dossier, par exemple :

   ```bash
   cd qr_pointage_system
````

4. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```
5. Lancez le serveur Flask accessible sur votre réseau local de plusieurs façons :

   * En direct (mode développement) :

     ```bash
     python main.py
     ```
   * Avec le script dédié `run.py` (plus flexible pour définir l’adresse IP) :

     ```bash
     python run.py --host 0.0.0.0
     ```
   * Pour un serveur plus robuste (production) :

     ```bash
     gunicorn -w 4 -b 0.0.0.0:5000 main:app
     ```
6. Trouvez votre adresse IP locale (exemple : `192.168.1.10`) :

   ```bash
   ip a       # Linux
   ifconfig   # macOS (ou ipconfig sur Windows)
   ```
7. Donnez l’URL `http://<votre_ip_locale>:5000` à vos utilisateurs pour qu’ils puissent pointer via le QR code.

---

### Installation sur Windows

1. Ouvrez PowerShell ou l’Invite de commandes.
2. Naviguez vers le dossier du projet :

   ```bash
   cd chemin\vers\qr_pointage_system
   ```
3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```
4. Lancez le serveur :

   * Directement :

     ```bash
     python main.py
     ```
   * Avec le script `run.py` :

     ```bash
     python run.py --host 0.0.0.0
     ```
   * Ou avec gunicorn (après installation via pip) :

     ```bash
     gunicorn -w 4 -b 0.0.0.0:5000 main:app
     ```
5. Trouvez votre IP locale :

   ```bash
   ipconfig
   ```
6. Donnez l’URL `http://<votre_ip_locale>:5000` pour accéder à l’application.

---

### Notes importantes

* Le serveur Flask lancé avec `python main.py` est en mode développement :
  **non sécurisé et non optimisé pour la production**.
* Pour un usage réel, privilégiez `gunicorn` ou un serveur WSGI dédié.
* Assurez-vous que votre firewall autorise les connexions entrantes sur le port utilisé (par défaut `5000`).
* Le dossier `excel/` contiendra chaque jour un fichier Excel nommé `pointage_YYYY-MM-DD.xlsx` avec les données du jour.

---

### Structure du projet

```plaintext
.
├── db.sqlite3           # Base SQLite stockant les données
├── excel/               # Dossier contenant les exports Excel quotidiens
├── main.py              # Application Flask principale
├── protection.py        # Module de protection / licence
├── requirements.txt     # Liste des dépendances Python
├── README.md            # Ce fichier d’information
├── run.py               # Script de lancement flexible (ex: définition host)
└── templates/
    ├── form.html        # Template HTML du formulaire de pointage
    └── message.html     # Template HTML pour les messages utilisateur
```

---

## Contact

⚠️ Ce système a été développé par **Abiye Enzo**
✉️ Email : [abiyeenzo@gmail.com](mailto:abiyeenzo@gmail.com)

