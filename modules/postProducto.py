import json
import requests
import os
from tabulate import tabulate

def postProducto():
    producto = {
            "codigo_producto": input("Ingrese el codigo del producto: "),
            "nombre": input("Ingrese el nombre del producto: "),
            "gama": input("Ingrese la gama del producto: "),
            "dimensiones": input("Ingrese las dimensiones del producto: "),
            "proveedor": input("Ingrese el proveedor del producto: "),
            "descripcion": input("Ingrese la descripcion del producto: "),
            "cantidad_en_stock": int(input("Ingrese la cantidad del producto: ")),
            "precio_venta": int(input("Ingrese el precio de venta del producto: ")),
            "precio_proveedor": int(input("Ingrese el precio de proveedor del producto: "))
        }
    
   
    #json-server storage/producto.json -b 5503
    peticion = requests.post("http://172.16.104.15:5503", data = json.dumps(producto, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]

def menu():
  while True:
    os.system("clear")
    print("""


    ___       __          _       _      __                     ____        __                    __   
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   / __ \____ _/ /_____  _____   ____/ /__ 
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / / / / __ `/ __/ __ \/ ___/  / __  / _ |
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/
/_/ _|_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/_    /_____/\__,_/\__/\____/____/   \__,_/\___/ 
   / /___  _____   / __ \_________  ____/ /_  _______/ /_____  _____                                   
  / / __ \/ ___/  / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                   
 / / /_/ (__  )  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                    
/_/\____/____/  /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/                                     
                                                                                                       
            

                                 1. Guardar un nuevo producto
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postProducto(), headers="keys", tablefmt="github"))
        input("Presione alguna tecla para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
