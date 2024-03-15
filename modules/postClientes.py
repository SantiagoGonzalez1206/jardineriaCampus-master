import json
import requests
import os
from tabulate import tabulate 

def postCliente():
    cliente = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre de contacto: "),
        "apellido_contacto": input("Ingrese el apellido de contacto: "),
        "telefono": input("Ingrese el telefono del cliente: "),
        "fax": input("Ingrese el fax cliente: "),
        "linea_direccion1": input("Ingrese la linea de direccion 1: "),
        "linea_direccion2": input("Ingrese la linea de direccion 2: "),
        "ciudad": input("Ingrese la ciudad del cliente: "),
        "region": input("Ingrese la region del cliente: "),
        "pais": input("Ingrese el pais del cliente: "),
        "codigo_postal": input("Ingrese el codigo postal del cliente: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representante de ventas del cliente: ")),
        "limite_credito": int(input("Ingrese el limite de credito del cliente: "))
        }
     
    #json-server storage/cliente.json -b 5502
    peticion = requests.post("http://172.16.100.142:5502", data = json.dumps(cliente, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]

def menu():
  while True:
    os.system("clear")
    print("""

    ___       __          _       _      __                     ____        __                
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____    
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/    
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/_    /_____/\__,_/\__/\____/____/      
  ____/ /__     / /___  _____   / ____/ (_)__  ____  / /____  _____                           
 / __  / _ \   / / __ \/ ___/  / /   / / / _ \/ __ \/ __/ _ \/ ___/                           
/ /_/ /  __/  / / /_/ (__  )  / /___/ / /  __/ / / / /_/  __(__  )                            
\__,_/\___/  /_/\____/____/   \____/_/_/\___/_/ /_/\__/\___/____/                             
                                                                                              


                                 1. Guardar un nuevo cliente
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postCliente(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
