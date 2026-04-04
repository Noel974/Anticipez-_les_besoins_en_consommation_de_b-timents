# save_model.py
import bentoml
import joblib

# Charger ton modèle entraîné
model = joblib.load("model.pkl")

# Liste des features dans l'ordre exact utilisé à l'entraînement
feature_names = [
    "is_Office",
    "is_School",
    "is_Hospital",
    "is_Hotel",
    "is_Warehouse",
    "is_Retail",
    "is_Residential",
    "is_Restaurant",
    "is_Worship",
    "is_Laboratory",
    "is_Mixed Use",
    "is_Other",
    "BuildingAge",
    "ratio_main_building",
    "ratio_parking",
    "floors_per_1000sf",
    "buildings_per_1000sf",
    "ratio_largest_use",
    "ratio_second_use",
    "Latitude_std",
    "Longitude_std",
    "nb_energy_sources",
]

bentoml.sklearn.save_model(
    "energy_model",
    model,
    custom_objects={
        "feature_names": feature_names,
    },
)
