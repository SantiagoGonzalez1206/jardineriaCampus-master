import json
import requests
import os
from tabulate import tabulate

import modules.getOficina as getofi
import modules.updateOficina as upOfi

def postOficina():
    oficina = {
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese la ciudad de la oficina: "),
        "pais": input("Ingrese el pais de la oficina: "),
        "region": input("Ingrese la region de la oficina: "),
        "codigo_postal": input("Ingrese el codigo postal de la oficina: "),
        "telefono": input("Ingrese el numero de telefono de la oficina: "),
        "linea_direccion1": input("Ingrese la linea de direccion 1: "),
        "linea_direccion2": input("Ingrese la linea de direccion 2: ")
        }
    
   
    #json-server storage/oficina.json -b 5501
    peticion = requests.post("http://154.38.171.54:5005/oficinas", data = json.dumps(oficina, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]


def deleteoficina(id):
    data = getofi.getOficinaId(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "cliente eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"cliente no encontrado",
                "id": id
            }],
            "status": 400,
        }


def menu():
  while True:
    os.system("clear")
    print("""


    ___       __          _       _      __                     ____        __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_____/\__,_/\__/\____/____/  
       __        __                    _____      _                                       
  ____/ /__     / /___ ______   ____  / __(_)____(_)___  ____ ______                      
 / __  / _ \   / / __ `/ ___/  / __ \/ /_/ / ___/ / __ \/ __ `/ ___/                      
/ /_/ /  __/  / / /_/ (__  )  / /_/ / __/ / /__/ / / / / /_/ (__  )                       
\__,_/\___/  /_/\__,_/____/   \____/_/ /_/\___/_/_/ /_/\__,_/____/                        
                                                                                          


                                 1. Guardar un nuevo dato de oficina
                                 2. Eliminar un dato de oficina
                                 3. Actualizar datos de oficina
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postOficina(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")
        
    elif(opcion == 2):
        idOficina = input(("Ingrese el id del cliente que deseas eliminar: "))
        print(tabulate(deleteoficina(idOficina)["body"], headers="keys", tablefmt="github"))

    elif(opcion == 3):
        
        upOfi.menu()

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
