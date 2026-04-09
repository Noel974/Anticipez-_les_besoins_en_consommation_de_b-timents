import bentoml
import pandas as pd
from pydantic import BaseModel, Field
from typing import Literal

# Charger ton modèle EXACT
MODEL_TAG = "energy_model:jtb3njjthwpjj5gr"

model_ref = bentoml.sklearn.get(MODEL_TAG)
model = bentoml.sklearn.load_model(MODEL_TAG)

# Récupérer les noms de features dans l'ordre exact
feature_names = model_ref.custom_objects["feature_names"]


# -------------------------
# 1. Schéma d’entrée avec validation simple
# -------------------------
class BuildingInput(BaseModel):
    # --- Variables numériques ---
    BuildingAge: float = Field(ge=0, le=300, description="Âge du bâtiment en années")
    NumberofFloors: float = Field(ge=0, le=40, description="Nombre d'étages")
    PropertyGFATotal: float = Field(ge=1, description="Surface totale (>=1)")
    SecondLargestPropertyUseTypeGFA: float = Field(ge=0, description="Surface du second usage")
    
    ratio_floors: float = Field(ge=0, le=1)
    ratio_largest_use: float = Field(ge=0, le=1)
    ratio_second_use: float = Field(ge=0, le=1)
    ratio_two_largest: float = Field(ge=0, le=1)
    
    distance_center: float = Field(ge=0, description="Distance au centre en km")
    nb_energy_sources: float = Field(ge=0, le=3, description="Nombre de sources d'énergie")

    # --- Catégories contrôlées ---
    PropertyCategory: Literal[
        "Office", "Education", "Hospitality", "Industrial & Storage",
        "Mixed Use", "Other", "Public / Institutional", "Retail & Food"
    ]

    distance_group: Literal["Très proche", "Proche", "Moyen", "Éloigné"]

    age_group: Literal["Neuf", "Récent", "Ancien", "Très ancien"]


# -------------------------
# 2. Service BentoML
# -------------------------
@bentoml.service
class EnergyService:

    @bentoml.api
    def ping(self) -> str:
        return f"Model loaded with {len(feature_names)} features"

    @bentoml.api
    def predict(self, data: BuildingInput):
        # Convertir les données brutes en DataFrame
        df = pd.DataFrame([data.model_dump()])

        # Prédiction via le pipeline sklearn
        pred = model.predict(df)[0]

        return {"prediction": float(pred)}
