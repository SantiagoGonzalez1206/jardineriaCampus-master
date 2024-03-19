import json
import requests
import os
from tabulate import tabulate

import modules.getPago as getpag


def postPago():
    pago = {
            "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
            "forma_pago": input("Ingrese la forma de pago: "),
            "id_transaccion": input("Ingrese el id de la transaccion: "),
            "fecha_pago": input("Ingrese la fecha de pago (Año/Mes/dia): "),
            "total": int(input("Ingrese el total: ")),
        }

     # json-server storage/pago.json -b 5505
    peticion = requests.post("http://154.38.171.54:5006/pagos", data = json.dumps(pago, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]


def deletepago(id):
    data = getpag.getPagoId(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
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
  ____/ /__     / /___  _____   / __ \____ _____ _____  _____                             
 / __  / _ \   / / __ \/ ___/  / /_/ / __ `/ __ `/ __ \/ ___/                             
/ /_/ /  __/  / / /_/ (__  )  / ____/ /_/ / /_/ / /_/ (__  )                              
\__,_/\___/  /_/\____/____/  /_/    \__,_/\__, /\____/____/                               
                                         /____/                                           
       
                                 
            

                                 1. Guardar un nuevo registro de pago
                                 2. Eliminar un registro de pago
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postPago(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion == 2):
        idPago = input(("Ingrese el id del cliente que deseas eliminar: "))
        print(tabulate(deletepago(idPago)["body"], headers="keys", tablefmt="github"))
    
    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
