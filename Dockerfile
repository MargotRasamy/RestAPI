# Dockerfile pour seeder la bdd

# Image python
FROM python:alpine

# Dependances dont on doit avoir bwsoin
RUN pip install pymongo

# copy ce qu'on a dans l'image
# WORKDIR /app // ca permet de mettre tous dans ce dossier lorsqu'on copie

COPY . .

# run 
CMD python ./mongoseeder.py

# build l'image du docker file
# docker image build -t nomduFichier