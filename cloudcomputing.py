# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:35:05 2020

@author: Alexandre
"""

from pymongo import MongoClient
from pprint import pprint 
import requests
import json

client = MongoClient('mongodb+srv://alexandreblarel:Chipie62!@cluster0.fr6rj.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.test_database # or db = client['test-database']

collection = db.test_collection # or collection = db['test-collection']

# pip install dnspython==2.0.0

def getVilleLille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"  
    response = requests.request("GET",url)
    response_json = json.loads(response.text.encode('utf8'))
    return(response_json.get("records",[]))

def getVilleLyon():
    url = "https://download.data.grandlyon.com/ws/grandlyon/pvo_patrimoine_voirie.pvostationvelov/all.json?maxfeatures=10&start=1"  
    response = requests.request("GET",url)
    response_json = json.loads(response.text.encode('utf8'))
    return(response_json.get("records",[]))

def getVilleParis():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"  
    response = requests.request("GET",url)
    response_json = json.loads(response.text.encode('utf8'))
    return(response_json.get("records",[]))

def getVilleRennes():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=stations_vls&q="  
    response = requests.request("GET",url)
    response_json = json.loads(response.text.encode('utf8'))
    return(response_json.get("records",[]))



L_lille =getVilleLille()
print(L_lille)
print(len(L_lille))