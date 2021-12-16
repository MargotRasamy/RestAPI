from typing import Dict
from fastapi import FastAPI, HTTPException
from model_personne import ModelPersonne
from pymongo import MongoClient

app = FastAPI()

host = 'mongodb'
client = MongoClient(host=f'{host}')
db = client.registre

@app.get("/personnes", response_model=list<ModelPersonne>())
def getPersonnesList():
    return db.personnes.find({})
    
    # if (db.findOrFail(ssn)):
    #     return HTTPException
    # return ModelPersonne(nom, prenom, ssn)


# @app.post("/personnes", response_model=ModelPersonne)
# def createPersonne(nom: str, prenom: str, ssn: str):
#     db = MongoClient....etc
#     if (db.findOrFail(ssn)):
#         return HTTPException
#     return ModelPersonne(nom, prenom, ssn)