# Orchestration d'une Stack Hybride avec Docker Compose

Ce projet consiste à déployer une architecture multi-services pilotant simultanément une base de données SQL (MySQL) et NoSQL (MongoDB) de manière orchestrée et résiliente.

## 🏗️ Architecture de la Solution

[cite_start]L'infrastructure est composée de 5 services interconnectés [cite: 111-120] :

1.  [cite_start]**db_mongo** : Image MongoDB personnalisée (non-root) gérant la base `blog_db`[cite: 117].
2.  [cite_start]**db_mysql** : Image officielle MySQL 8.0 pour le stockage des utilisateurs[cite: 118].
3.  [cite_start]**admin_mongo** : Interface web `mongo-express` pour le pilotage NoSQL[cite: 118].
4.  [cite_start]**admin_mysql** : Interface web `adminer` pour l'administration SQL[cite: 119].
5.  [cite_start]**api** : Application FastAPI (Python) faisant le pont entre les deux mondes[cite: 120].

## 🚀 Fonctionnalités Clés

### Résilience et Dépendances
* [cite_start]**Politique de redémarrage** : Configurée sur `on-failure` pour ne redémarrer automatiquement que si l'arrêt est dû à une erreur (crash)[cite: 124, 186].
* **Gestion des dépendances** : 
    * [cite_start]L'API ne démarre que lorsque les deux bases de données sont considérées comme saines (`healthy`) par leurs healthchecks respectifs[cite: 126].
    * [cite_start]Adminer attend que `db_mysql` soit saine[cite: 127].
    * [cite_start]Mongo-Express attend que `db_mongo` soit saine[cite: 128].

### Healthchecks "Métiers" Stricts
[cite_start]Les tests de santé valident l'intégrité des données et non seulement la présence d'un processus [cite: 153-155] :
* **MongoDB** : Vérifie l'accès à la base `blog_db` et confirme que la collection `posts` contient exactement 5 articles[cite: 159, 160].
* [cite_start]**MySQL** : Vérifie la connectivité et confirme que la table `utilisateurs` contient les données d'initialisation[cite: 162, 163].
* **API** : Interroge ses propres routes internes `/posts` et `/users`. [cite_start]Le statut n'est "OK" que si les deux bases répondent [cite: 164-166].

### Sécurité et Persistance
* **Isolation Réseau** : Les bases de données sont isolées du monde extérieur dans un réseau interne[cite: 178].
* [cite_start]**Volumes** : Persistance des données assurée pour les deux bases de données[cite: 175].
* [cite_start]**Secrets** : Utilisation impérative d'un fichier `.env` pour ne stocker aucun mot de passe en dur[cite: 176].

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