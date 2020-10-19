# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:35:05 2020

@author: Alexandre
"""

from pymongo import MongoClient
from pprint import pprint 
import requests
import json
import time
import dateutil.parser

client = MongoClient('mongodb+srv://alexandreblarel:Chipie62!@cluster0.fr6rj.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority')

db = client.bicycle # or db = client['test-database']
db.datas.create_index([('station_id', 1),('date', -1)], unique=True)
#collection = db.test_collection # or collection = db['test-collection']

# pip install dnspython==2.0.0


db.stations2.create_index([('geometry','2dsphere')])

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



#L_lille =getVilleLille()
#print(L_lille)
#print(len(L_lille))

#posts=db.posts
#post_Lille=posts.insert_many(L_lille)




def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

def get_station_id(id_ext):
    tps = db.stations2.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
    return tps['_id']


def nearStation(lat,lon):
    
    near_station = db.stations2.find({'geometry':{
        '$near':{'$geometry':{
            'type': "Point",
            'coordinates': [lon,lat]},
            '$maxDistance':1000,
            '$minDistance':0
            }
        }})
    return(list(near_station))
    

print(nearStation(50.66026,3.087568))

# while True:
#     print('update')
#     vlilles = get_vlille()
#     datas = [
#         {
#             "bike_availbale": elem.get('fields', {}).get('nbvelosdispo'),
#             "stand_availbale": elem.get('fields', {}).get('nbplacesdispo'),
#             "date": dateutil.parser.parse(elem.get('fields', {}).get('datemiseajour')),
#             "station_id": get_station_id(elem.get('fields', {}).get('libelle'))
#         }
#         for elem in vlilles
#     ]

#     try:
#         db.datas.insert_many(datas, ordered=False)
#     except:
#         pass

#     time.sleep(10)

    

