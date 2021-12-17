# Dockerfile pour seeder la bdd

# Image python
FROM python:3.6.4-alpine3.7

# Dependances dont on doit avoir bwsoin
RUN pip install -U pymongo
RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install --upgrade pip

# copy ce qu'on a dans l'image
# WORKDIR /app // ca permet de mettre tous dans ce dossier lorsqu'on copie

COPY . .

# run 
CMD python ./app.py

# build l'image du docker file
# docker image build -t nomImage .

# run
# docker run -it --network mynet nomImage