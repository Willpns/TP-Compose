# Orchestration d'une Stack Hybride avec Docker Compose

Ce projet consiste à déployer une architecture multi-services pilotant simultanément une base de données SQL (MySQL) et NoSQL (MongoDB) de manière orchestrée et résiliente.

## 🏗️ Architecture de la Solution

L'infrastructure est composée de 5 services interconnectés :

1.  **db_mongo** : Image MongoDB personnalisée (non-root) gérant la base `blog_db`.
2.  **db_mysql** : Image officielle MySQL 8.0 pour le stockage des utilisateurs.
3.  **admin_mongo** : Interface web `mongo-express` pour le pilotage NoSQL.
4.  **admin_mysql** : Interface web `adminer` pour l'administration SQL.
5.  **api** : Application FastAPI (Python) faisant le pont entre les deux mondes.

## 🚀 Fonctionnalités Clés

### Résilience et Dépendances
* **Politique de redémarrage** : Configurée sur `on-failure` pour ne redémarrer automatiquement que si l'arrêt est dû à une erreur (crash).
* **Gestion des dépendances** : 
    * L'API ne démarre que lorsque les deux bases de données sont considérées comme saines (`healthy`) par leurs healthchecks respectifs.
    * Adminer attend que `db_mysql` soit saine.
    * Mongo-Express attend que `db_mongo` soit saine.

### Healthchecks "Métiers" Stricts
Les tests de santé valident l'intégrité des données et non seulement la présence d'un processus :
* **MongoDB** : Vérifie l'accès à la base `blog_db` et confirme que la collection `posts` contient exactement 5 articles.
* **MySQL** : Vérifie la connectivité et confirme que la table `utilisateurs` contient les données d'initialisation.
* **API** : Interroge ses propres routes internes `/posts` et `/users`. Le statut n'est "OK" que si les deux bases répondent.

### Sécurité et Persistance
* **Isolation Réseau** : Les bases de données sont isolées du monde extérieur dans un réseau interne.
* **Volumes** : Persistance des données assurée pour les deux bases de données.
* **Secrets** : Utilisation impérative d'un fichier `.env` pour ne stocker aucun mot de passe en dur.

## 🛠️ Installation et Lancement

1.  Clonez le dépôt.
2.  Créez votre fichier `.env` à partir du fichier `.env.example`.
3.  Lancez l'orchestration :
    `docker compose up -d --build`

## 📊 Preuves de fonctionnement

### 1. Statut des services (Healthcheck)
Tous les services sont opérationnels et les services critiques sont marqués comme sains.

![alt text](</img/checkhealth.png>)

### 2. Route Hybride - MongoDB (/posts)
Récupération réussie des articles depuis MongoDB via l'API.

![alt text](</img/posts.png>)

### 3. Route Hybride - MySQL (/users)
Récupération réussie des utilisateurs depuis MySQL via l'API.

![alt text](</img/users.png>)

---
*Projet réalisé dans le cadre du module Conteneurisation - B2 INFO CYBER - YNOV Sophia Antipolis.*