import json
import requests

def getAllGama():
    peticion= requests.get("")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre= []
    for val in getAllGama:
        gamaNombre.append(val.get("gama"))
    return gamaNombre