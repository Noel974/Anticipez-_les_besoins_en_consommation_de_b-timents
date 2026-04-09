# save_model.py
import bentoml
import joblib

# Charger ton modèle entraîné
model = joblib.load("model.pkl")

# Liste des features dans l'ordre exact utilisé à l'entraînement
feature_names = [
    "num__BuildingAge",
    "num__NumberofFloors",
    "num__PropertyGFATotal",
    "num__SecondLargestPropertyUseTypeGFA",
    "num__ratio_floors",
    "num__ratio_largest_use",
    "num__ratio_second_use",
    "num__ratio_two_largest",
    "num__distance_center",
    "num__nb_energy_sources",
    "cat__PropertyCategory_Education",
    "cat__PropertyCategory_Hospitality",
    "cat__PropertyCategory_Industrial & Storage",
    "cat__PropertyCategory_Mixed Use",
    "cat__PropertyCategory_Office",
    "cat__PropertyCategory_Other",
    "cat__PropertyCategory_Public / Institutional",
    "cat__PropertyCategory_Retail & Food",
    "cat__distance_group_Moyen",
    "cat__distance_group_Proche",
    "cat__distance_group_Trés proche",
    "cat__distance_group_Éloigné",
    "cat__age_group_Ancien",
    "cat__age_group_Neuf",
    "cat__age_group_Récent",
    "cat__age_group_Trés ancien"
]

bentoml.sklearn.save_model(
    "energy_model",
    model,
    custom_objects={
        "feature_names": feature_names,
    },
)
