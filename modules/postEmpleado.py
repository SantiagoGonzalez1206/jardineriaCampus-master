import json
import requests
import os
from tabulate import tabulate

def postEmpleado():
    empleado = {
            "codigo_empleado": int(input("Ingrese el codigo de empleado: ")),
            "nombre": input("Ingrese el nombre de empleado: "),
            "apellido1": input("Ingrese el primer apellido del empleado: "),
            "apellido2": input("Ingrese el segundo apellido del empleado: "),
            "extension": input("Ingrese la extension del empleado: "),
            "email": input("Ingrese el email del empleado: "),
            "codigo_oficina": input("Ingrese el codigo de oficina del empleado: "),
            "codigo_jefe": int(input("Ingrese el codigo del jefe del empleado: ")),
            "puesto": input("Ingrese el puesto asignado al empleado: "),
        }
   
   
     # json-server storage/empleado.json -b 5504
    peticion = requests.post("http://172.16.104.15:5504", data = json.dumps(empleado, indent =4).encode("UTF-8"))
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
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/__   /_____/\__,_/\__/\____/____/  
  ____/ /__     / /___  _____   / ____/___ ___  ____  / /__  ____ _____/ /___  _____      
 / __  / _ \   / / __ \/ ___/  / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/      
/ /_/ /  __/  / / /_/ (__  )  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )       
\__,_/\___/  /_/\____/____/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/        
                                            /_/                                           
                                 
            

                                 1. Guardar un nuevo empleado
                                 0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
        input("Presione alguna tecla para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")
