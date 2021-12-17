from typing import Dict
from fastapi import FastAPI, HTTPException
from model_personne import ModelPersonne
from pymongo import MongoClient

app = FastAPI()

host = 'mongodb'
client = MongoClient(host=f'{host}')
db = client.registre

@app.get("/personnes")
def getPersonnesList():
    return db.personnes.findAll({})
    
    # if (db.findOrFail(ssn)):
    #     return HTTPException
    # return ModelPersonne(nom, prenom, ssn)


# @app.post("/personnes", response_model=ModelPersonne)
# def createPersonne(nom: str, prenom: str, ssn: str):
#     db = MongoClient....etc
#     if (db.findOrFail(ssn)):
#         return HTTPException
#     return ModelPersonne(nom, prenom, ssn)

# Pour lancer le serveur uvicorn, on met en ligne de commande : avec hello le nom du fichier
# uvicorn hello:app --reload