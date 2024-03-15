import json
import requests
import os
from tabulate import tabulate

def postPedido():
    pedido = {
        "codigo_pedido": int(input("Ingrese el codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada del pedido: "),
        "fecha_entrega": input("Ingrese la fecha de entrega del pedido: "),
        "estado": input("Ingrese el estado del pedido: "),
        "comentario": input("Ingrese los comentarios acerca del pedido: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
        }
    
   
    #json-server storage/pedido.json -b 5506
    peticion = requests.post("http://172.16.104.15:5506", data = json.dumps(pedido, indent =4).encode("UTF-8"))
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
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/     /_____/\__,_/\__/\____/____/  
       __        __              ____           ___     __                                
  ____/ /__     / /___  _____   / __ \___  ____/ (_)___/ /___  _____                      
 / __  / _ \   / / __ \/ ___/  / /_/ / _ \/ __  / / __  / __ \/ ___/                      
/ /_/ /  __/  / / /_/ (__  )  / ____/  __/ /_/ / / /_/ / /_/ (__  )                       
\__,_/\___/  /_/\____/____/  /_/    \___/\__,_/_/\__,_/\____/____/                        
                                                                                          


                                 1. Guardar un nuevo pedido
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postPedido(), headers="keys", tablefmt="github"))
        input("Presione alguna tecla para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
