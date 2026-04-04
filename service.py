import bentoml
import pandas as pd
from pydantic import BaseModel, Field

# Charger ton modèle EXACT
MODEL_TAG = "energy_model:caixl5bqjwtcrxvd"

model_ref = bentoml.sklearn.get(MODEL_TAG)
model = bentoml.sklearn.load_model(MODEL_TAG)

# Récupérer les noms de features dans l'ordre exact
feature_names = model_ref.custom_objects["feature_names"]


# -------------------------
# 1. Schéma d’entrée corrigé
# -------------------------
class BuildingInput(BaseModel):
    is_Office: int
    is_School: int
    is_Hospital: int
    is_Hotel: int
    is_Warehouse: int
    is_Retail: int
    is_Residential: int
    is_Restaurant: int
    is_Worship: int
    is_Laboratory: int

    # ⚠️ Correction critique : alias pour correspondre au modèle
    is_Mixed_Use: int = Field(..., alias="is_Mixed Use")

    is_Other: int
    BuildingAge: float
    ratio_main_building: float
    ratio_parking: float
    floors_per_1000sf: float
    buildings_per_1000sf: float
    ratio_largest_use: float
    ratio_second_use: float
    Latitude_std: float
    Longitude_std: float
    nb_energy_sources: int


# -------------------------
# 2. Service BentoML
# -------------------------
@bentoml.service
class EnergyService:

    @bentoml.api
    def ping(self) -> str:
        return f"Model loaded with {len(feature_names)} features"

    @bentoml.api
    def predict(self, input_data: BuildingInput):
        # Convertir en DataFrame avec les bons noms de colonnes
        df = pd.DataFrame([input_data.dict(by_alias=True)], columns=feature_names)

        # Prédiction
        pred = model.predict(df)[0]

        return {"prediction": float(pred)}
