# Changelog

Toutes les modifications notables de ce projet sont documentées ici.

---

## \[1.0.0] - 2025-07-04

### Ajoutées

* Application Flask fonctionnelle pour le système de pointage par QR code.
* Base SQLite pour stocker utilisateurs, départements et pointages.
* Formulaire web avec autocomplétion pour nom (majuscules) et département (minuscules).
* Gestion automatique des heures d’arrivée et de sortie, incluant pointage sur plusieurs jours.
* Limitation stricte à deux pointages par jour (arrivée + sortie).
* Export quotidien automatique des données dans des fichiers Excel.
* Endpoint `/autocomplete` fournissant les listes de noms et départements existants.
* Normalisation des saisies utilisateurs pour cohérence des données.
* Interface utilisateur simple, responsive et accessible.

### Changements

* Optimisation de la structure des tables SQLite pour performance et intégrité.
* Validation côté serveur renforcée sur les saisies utilisateur.

### Corrections

* Gestion correcte des pointages en cas de sortie reportée au lendemain.
* Écriture fiable des fichiers Excel pour éviter tout conflit d’accès.

---

## \[À venir]

* Mise en place d’un système d’authentification pour sécuriser l’accès.
* Interface d’administration pour la consultation et la modification des pointages.
* Notifications automatiques par email ou SMS lors du pointage.
* Application mobile dédiée pour scanner le QR code et pointer directement.
* Optimisation de la gestion multi-utilisateurs simultanés et montée en charge.

---

*Ce changelog suit la [convention Keep a Changelog](https://keepachangelog.com/fr/).*
