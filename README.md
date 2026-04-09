création d'environement  python  py -3.11 -m venv venv311  venv311\Scripts\activate

installation des dépendances  pip install bentoml pandas scikit-learn pydantic  puis creer le requirement.txt  pip freeze > requirements.txt"# Anticipez-_les_besoins_en_consommation_de_b-timents" 

commande pour créer un model 
python save_model.py
commande pour executer l'api 
bentoml serve service:EnergyService --reload
pour builder 
commande 
bentoml build
