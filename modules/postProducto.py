import json

def postproducto(producto):
    import requests
    #json-server storage/producto.json -b 5503
    peticion = requests.post("http://172.16.100.142:5503", data = json.dump(producto))
    res=peticion.json()
    return res