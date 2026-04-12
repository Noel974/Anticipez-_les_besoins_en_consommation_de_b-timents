 # Anticipez les besoin en consomation 

 ## 👤 Auteur

Projet réalisé par **Noel Emmanuel**  

- 🔗 GitHub : https://github.com/Noel974 
- 💼 LinkedIn : https://www.linkedin.com/in/Antoine-Noel/ 
- 📧 Email : noelantoine974@outlook.fr  

 ## Sommaire 
-[Description](#descritption)
-[Technologie](#technologie)
-[Deroulement](#deroulement)
-[Docker](#docker)
-[Deployment](#depoyment)

## Description

Ce projet propose un modèle de machine learning permettant de prédire la consommation énergétique d’un bâtiment à partir de ses caractéristiques structurelles (âge, nombre d’étages, surface, type d’usage, etc.).
Le modèle génère une estimation globale de la consommation, généralement exprimée en kWh/an, utile pour des analyses énergétiques et des comparaisons entre bâtiments.

## Technologie
### Analyse et préparation feature

| Catégorie              | Outil / Librairie       | Rôle dans le projet                                      |
|-----------------------|------------------------|----------------------------------------------------------|
| Langage               | Python                 | Développement global du projet                           |
| Manipulation données  | Pandas                 | Chargement, nettoyage et transformation des données      |
| Calcul scientifique   | NumPy                  | Opérations mathématiques et gestion des tableaux         |
| Visualisation         | Matplotlib             | Création de graphiques                                  |
| Visualisation         | Seaborn                | Visualisation statistique avancée                        |
| Préprocessing         | Scikit-learn           | Encodage, normalisation et transformation des features   |
| Feature Engineering   | ColumnTransformer      | Pipeline de transformation des variables                 |
| Encodage             | OneHotEncoder          | Transformation des variables catégorielles               |
| Normalisation         | StandardScaler         | Mise à l’échelle des données                             |
| Modélisation          | LinearRegression       | Modèle de régression linéaire                            |
| Modélisation          | SVR                    | Support Vector Regression                               |
| Modélisation          | RandomForestRegressor  | Modèle d’ensemble basé sur des arbres                    |
| Baseline              | DummyRegressor         | Modèle de référence pour comparaison                     |
| Évaluation            | Scikit-learn Metrics   | MSE, MAE, R² pour évaluer les performances               |
| Validation            | train_test_split       | Séparation des données train/test                        |
| Optimisation          | GridSearchCV           | Recherche des meilleurs hyperparamètres                  |
| Validation croisée    | cross_validate         | Évaluation robuste du modèle                             |
| Interprétabilité      | permutation_importance | Importance des variables                                 |
| Pipeline              | Pipeline               | Chaînage des étapes ML                                  |

### API & Déploiement

| Technologie     | Rôle                                         |
|-----------------|----------------------------------------------|
| BentoML         | Déploiement et service du modèle ML          |
| Scikit-learn    | Chargement et utilisation du modèle entraîné |
| Pandas          | Manipulation des données en entrée           |
| Joblib          | Sérialisation du modèle                      |
| Pydantic        | Validation des données d’entrée API          |

## Deroulement
Le Déroulement du projet se fait en deux partie. Dans la premiere partie on retrouvera les analyse, les features, les préparé pour la modélisation, Comparaison de différents modèles supervisés et Optimisation et interprétation du modèle
Pour la partie deux sera la création de l'API avec bentoML
### Partie 1 Préparation analyse des features 
Pour l'analyse on va utilisé jupyter de anaconda notebook pour se projet un template a été donnée avec toute les librairaires utilisé sur les quel vous pouvez retrouver la liste en haut dans la partie technologie analyse et préparation feature. Dans le notebook on retrouvera la partie analyse Exploratoire sur les quel on explorer le fichier CSV qui nous a ete transmi. Se qui sera réaliser c'est comprendre le jeux donnée nettoyage l'analyse et la préparation pour le feature. Une fois c'est action terminé on obtient un nouveau jeux donnée nettoyer et filtrer dans se cas précis on commence la réalisation feature engineering, suivi de la préparation a la modélisation, de faire des train test  avec une validation croisée et de terminé par l’optimisation du modèle à l’aide de GridSearchCV, suivie de l’interprétation des performances.
### Partie 2 Creation L'API 
Pour la création de l'API  plusieur étape a suivre.
Voici son déroulement.
#### Installation python et environement 
Installer python selon la version recommandé pour se projet l'utilisation de bentoML n'était pas adapté pour la dernier version python pour cela je suis partie sur python v3.11 pour l'installation suivre l'introduction du site web https://www.python.org/downloads/windows/
puis de verifier avec la commande 
```bash
python --version 
```
par la suite d'installer et activé l'environnement 
```bash
py -3.11 -m venv venv311
```
activé l'environnement
```bash
venv311\Scripts\activate
```
#### installation des packages 
BentoML
Pydantic 
joblib
scikit-learn
avec la commande suivante 
```bash 
pip install bentoml pandas scikit-learn pydantic
```
et la commande pour créer le fichier requirements.txt avec tous les packages installer 
```bash 
pip freeze > requirements.txt
```
#### Code 
La structure du code elle composé d'un fichier save_model.py et de service.py.

**save_model.py** : ce script permet de charger le modèle entraîné (pipeline complet) et de l’enregistrer avec BentoML.
Il inclut également des informations supplémentaires comme les noms des features (custom_objects) pour faciliter le suivi et le déploiement.
**service.py** : ce fichier définit le service API. Il permet de charger le modèle sauvegardé et d’exposer des endpoints (comme /predict) afin de réaliser des prédictions à partir de nouvelles données
Cette commande permet Sauvegarde du modèle :
```bash 
python save_model.py
```
cette commande permet au lancement du service en local
```bash 
bentoml serve service:EnergyService --reload
```

## Docker
deux methode pour depoyement sur docker 
### premier version via bento 
```bash
    bentoml build
```
on obtien un tag qui se présente comme tel  
``` bash
energy_service:fpq4zozug2bpp5gr
```
par la suite on va Containerisation du Bento avec cette commande 
```bash
bentoml containerize energy_service:fpq4zozug2bpp5gr
```
cela va nous gerer une image 
```bash
energy_service:fpq4zozug2bpp5gr
```
et grace a cette commande on peut naviguer sur le localhost http://localhost:3000
```bash
docker run --rm -p 3000:3000 energy_service:fpq4zozug2bpp5gr
```
### Deuxieme version via Docker
Créer un fichier docker-compose.yml et de renseigner les elements qui concerne la creation 
```bash
version: "3.9"

services:
  energy_service:
    image: energy_service:fpq4zozug2bpp5gr
    ports:
      - "3000:3000"
    restart: always
```
Une fois le fichier créer Lancer le service avec cette commande 
```bash
docker-compose down
```
## Deployment
1. Build & push de l’image vers ECR
```bash
docker build -t energy-service .
docker tag energy-service:latest 415472784063.dkr.ecr.eu-west-1.amazonaws.com/energy-service:latest
docker push 415472784063.dkr.ecr.eu-west-1.amazonaws.com/energy-service:latest
```
2. Connexion à l’instance EC2
```bash
ssh -i "energy-key.pem" ubuntu@35.180.32.247
```
3. Installation Docker
```bash
sudo apt update
sudo apt install docker.io -y
sudo usermod -aG docker ubuntu
```
4. Installation AWS CLI
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
5. Connexion à ECR
```bash
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 415472784063.dkr.ecr.eu-west-1.amazonaws.com
```
6. Pull & run du conteneur
```bash
docker pull 415472784063.dkr.ecr.eu-west-1.amazonaws.com/energy-service:latest
docker run -d -p 80:3000 415472784063.dkr.ecr.eu-west-1.amazonaws.com/energy-service:latest
```
une fois tous l'étapes réalisé l'API est en ligne sous "http://35.180.32.247" 

