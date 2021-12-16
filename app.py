from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic.main import Model
from model_personne import ModelPersonne

app = FastAPI()

# @app.get("/personnes", response_model=ModelPersonne)
# def getPersonnesList():
#     if (db.findOrFail(ssn)):
#         return HTTPException
#     return ModelPersonne(nom, prenom, ssn)


# @app.post("/personnes", response_model=ModelPersonne)
# def createPersonne(nom: str, prenom: str, ssn: str):
#     db = MongoClient....etc
#     if (db.findOrFail(ssn)):
#         return HTTPException
#     return ModelPersonne(nom, prenom, ssn)