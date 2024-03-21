from tabulate import tabulate 
import time
import requests

def getAllOficina():
    # json-server storage/oficina.json -b 5501
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data

def getOficinaId(id):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    return[peticion.json()] if peticion.ok else []


def getOficinaCodigos2(codigo):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas?codigo_oficina={codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data

def getTelFromTel(telefono):
     Officecode=[]
     for val in getAllOficina():
        if val.get("telefono")==telefono:
            return[val]




#obtener oficinca segun la que se meta por consola
def getCodeOfficeCode(codigo):
     Officecode=[]
     for val in getAllOficina():
        if val.get("codigo_oficina")==codigo:
            return[val]

#obtener direcciones a partir de direcciones
def getDireccion1FromDireccion(direccion):
     linea1=[]
     for val in getAllOficina():
        if val.get("linea_direccion1")==direccion:
            return[val]
        
def getDireccion2FromDireccion(direccion):
     line2=[]
     for val in getAllOficina():
        if val.get("linea_direccion2")==direccion:
            return[val]




def getCodigoOfiCiudadName():
    CodigoOfiCiudad = list()
    for val in getAllOficina():
        codigoNames = dict({
            "codigo_oficina": val.get('codigo_oficina'),
            "ciudad": val.get('ciudad')
        })
        CodigoOfiCiudad.append(codigoNames)
    return CodigoOfiCiudad

def getCiudadTelefonoEspaña():
    ciudadTelefonoEspaña = []
    for val in getAllOficina():
        if val.get('pais') == "España" :
            ciudadTelefonoEspaña.append(
                {
                    "ciudad": val.get("ciudad"),
                    "telefono": val.get("telefono")
                }
            )  
    return ciudadTelefonoEspaña

def menu():
    while True:
        print("""

    ____                        __                   __        __               _____      _            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___ _   ____  / __(_)____(_)___  ____ _
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ `/  / __ \/ /_/ / ___/ / __ \/ __ `/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ /  / /_/ / __/ / /__/ / / / / /_/ / 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\__,_/   \____/_/ /_/\___/_/_/ /_/\__,_/  
          /_/                                                                                           


                                 1. Codigo de oficina y ciudad donde hay oficinas
                                 2. Ciudad y telefono de las oficinas de España
                                 0. Salir
""")
        try:
            opcion= int(input("\nSeleccione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(getCodigoOfiCiudadName(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getCiudadTelefonoEspaña(), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break
            else:
                print("elija una opcion valida")
        except ValueError: 
                print("Caracteres incorrectos, elija una opcion del 0 al 2")
                time.sleep(3)